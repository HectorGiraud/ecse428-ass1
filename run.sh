#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

if command -v uv >/dev/null 2>&1; then
    exec uv run --quiet python -m ass1.ui "$@"
else
    PYTHONPATH=src exec python3 -m ass1.ui "$@"
fi