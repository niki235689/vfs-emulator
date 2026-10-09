#!/usr/bin/env bash
set -e
echo "=== Test 1: Minimal VFS ==="
python3 src/main.py --vfs vfs_samples/minimal --script scripts/startup_stage3.txt &
PID=$!
sleep 2
kill $PID 2>/dev/null || true

echo "=== Test 2: Deep 3-level VFS ==="
python3 src/main.py --vfs vfs_samples/deep --script scripts/startup_stage3.txt &
PID=$!
sleep 2
kill $PID 2>/dev/null || true
echo "VFS tests completed."