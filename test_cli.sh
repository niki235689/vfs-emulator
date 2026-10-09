#!/usr/bin/env bash
set -e
echo "=== 1. Launch with all parameters ==="
python3 src/main.py --vfs vfs_samples/deep --script scripts/startup_stage2.txt &
PID=$!
sleep 2
kill $PID 2>/dev/null || true

echo "=== 2. Launch without parameters ==="
python3 src/main.py &
PID=$!
sleep 2
kill $PID 2>/dev/null || true
echo "CLI tests completed."