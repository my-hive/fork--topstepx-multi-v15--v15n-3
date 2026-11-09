# v15n-3 explorer notes

Best: E9 (SHA ecfa104a...), MNQ pre-open continuation (adopted from v15n-2). dev 0.2983, eras +1747/+9381/+1790, posyr 0.8, 5 knobs. Dev screen only, no null.
Entry risk must be declared PER CONTRACT (evaluator multiplies by opened contracts).

Rejected (dev_score 0 or era-fail):
- ES 30m ORB continuation; NQ/ES/YM ORB, Donchian, overnight/gap fade, last-hour fade, EU-continuation: all negative after stressed costs.
- Long-only overnight drift: NQ/ES/YM positive in lab only because of backfilled-gap artifacts; official eval NQ negative (gap/roll flatten churn pre-2018).
- MNQ-MES / MNQ-MYM / M2K-MYM pre-open relative-value spread: negative.
- MNQ pre-open variants: min-move 20pt (0.161, era0 fail), 5pt (0.233), ATR-stop sized (risk cap fail), exit 15:00 / 13:30 (era fail), 5ct/30pt (years 0.6), 3ct/30pt 0.238, 2ct/60pt 0.268, long-only 0.234, short-only 0.064.
- MNQ+MES agreement 0.283, MNQ+MYM agreement 0.285 (era blocks +3754/+9009/+3815, more even but lower score).
Caveat: MNQ history 2019-05+ only; same rule on NQ 2010-2023 eras -24k/-22k/+87k. 2019 loses every variant.
