import json, sys, subprocess, datetime
# usage: python3 record.py EXPID report.json "hypothesis" "mechanism" [notes]
i, path, hyp, mech = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
notes = sys.argv[5] if len(sys.argv) > 5 else ""
r = json.load(open(path))
s = r["stressed"]
e = s["eligibility"]
null = r["null"]
row = dict(
    id=i,
    agent="v15n-3",
    ts=datetime.datetime.utcnow().isoformat() + "Z",
    hypothesis=hyp, mechanism=mech, notes=notes,
    sha256=r["strategy_sha256"], symbols=r["symbols"],
    dev_score=s["dev_score"], fold_score=s["fold_score"],
    folds=s["folds"], positive_year_fraction=s["positive_year_fraction"],
    econ_grade=s["econ_grade"], knobs=s["knobs"],
    era_blocks={k: v["pnl"] for k, v in s["era_blocks"].items()},
    worst_era_block_pnl=e["worst_era_block_pnl"],
    total_pnl=s["total_pnl"], pnl_per_year=s["pnl_per_year"],
    worst_three_mean=s["worst_three_mean"],
    eligible=e["passed"], checks=e["checks"],
    yearly_pnl=s["yearly"],
    null=(None if not null else {"seeds": null["seeds"], "p_value": null["p_value"], "provisional": null["provisional"]}),
    entry_0830_0930_share=s["entry_0830_0930_share"],
    max_entry_risk=s["max_entry_risk"], max_exposure=s["max_exposure"],
)
with open("experiments.jsonl", "a") as f:
    f.write(json.dumps(row) + "\n")
print("recorded", i, "dev_score", s["dev_score"], "worst_era", e["worst_era_block_pnl"])
