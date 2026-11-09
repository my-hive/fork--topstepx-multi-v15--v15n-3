"""Attribution v15n-2 (SHA 2d2eb5c0 family): MNQ pre-open drift continuation.

Side = sign(10:00 close - 07:00 open) on MNQ; hold 10:00-14:30 CT; close-based stop of
`stop_pts` against entry. Fixed `contracts`, declared risk is PER CONTRACT.
Mechanism: overnight European-session news drift persists into the US morning.
"""
import numpy as np

PARAMS = {"signal_start": 25200, "entry_sec": 36000, "exit_sec": 52200,
          "stop_pts": 45.0, "contracts": 3}
POINT_VALUE = 2.0


def signals(panel):
    out = {}
    for symbol, df in panel.items():
        t = np.zeros(len(df), dtype=np.int64)
        if symbol == "MNQ":
            o = df.open.to_numpy(); c = df.close.to_numpy(); sec = df.ct_sec.to_numpy()
            for ids in df.groupby("session", sort=False).indices.values():
                ids = ids[np.argsort(sec[ids], kind="stable")]
                a = int(np.searchsorted(sec[ids], PARAMS["signal_start"]))
                b = int(np.searchsorted(sec[ids], PARAMS["entry_sec"]))
                e = int(np.searchsorted(sec[ids], PARAMS["exit_sec"]))
                if not (a < b < len(ids)) or e <= b:
                    continue
                side = int(np.sign(c[ids[b - 1]] - c[ids[a]]))
                if not side:
                    continue
                entry_px = o[ids[b]]
                for j in range(b, e):
                    i = ids[j]
                    if side > 0 and c[i] <= entry_px - PARAMS["stop_pts"]:
                        break
                    if side < 0 and c[i] >= entry_px + PARAMS["stop_pts"]:
                        break
                    t[i] = side * PARAMS["contracts"]
        out[symbol] = t
    return out


def entry_risk(panel):
    declared = PARAMS["stop_pts"] * POINT_VALUE  # per contract
    return {s: np.full(len(df), declared, dtype=float) for s, df in panel.items()}
