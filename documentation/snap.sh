#!/usr/bin/env bash
# usage: snap.sh red|green <increment> <test id>
set -u
phase=$1; n=$2; test=$3
out="documentation/shots/inc$(printf %02d "$n")"; mkdir -p "$out"

# Run a command and save its output as an image, even if the command fails
shot() { freeze --execute "bash -c 'COLUMNS=90 $1 || true'" --wrap 90 -o "$2"; }
git add -A
if [ "$phase" = red ]; then
  git diff --staged -- tests | freeze -l diff -o "$out/1-test-code.png"
  shot "uv run pytest $test" "$out/2-test-fails.png"
  git add "$out"
  git commit -qm "inc$n RED: $test"
else
  git diff --staged -- src | freeze -l diff -o "$out/3-code-change.png"
  shot "uv run pytest $test" "$out/4-test-passes.png"
  shot "uv run pytest"       "$out/5-all-tests-pass.png"
  git add "$out"
  git commit -qm "inc$n GREEN: $test"
fi
echo "saved to $out"