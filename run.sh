#!/bin/bash
# usage: ./run.sh EXPID SYM1,SYM2 "hypothesis" [null-seeds]
set -e
ID=$1; SYMS=$2; HYP=$3; NS=${4:-0}
SYMLIST=$(echo $SYMS | tr ',' ' ')
OUT=/tmp/w/$ID.json
/usr/bin/time -f "%e s" python3 eval/sim.py --data /data/dev --symbols $SYMLIST \
  --strategy strategy.py --output $OUT --null-seeds $NS --mode dev > /tmp/w/$ID.out 2> /tmp/w/$ID.err || { tail -20 /tmp/w/$ID.err; exit 1; }
head -6 /tmp/w/$ID.out
grep -o '^year [0-9]*: {.*}' /tmp/w/$ID.out | sed 's/"attempts".*"rate"/rate/; s/"sessions".*"pnl"/pnl/' | head -20
