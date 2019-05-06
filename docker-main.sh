#!/usr/bin/env bash
set -e

TASK_PID=0

term_handler() {
    if ps -p ${TASK_PID} > /dev/null; then
        kill -SIGTERM "$TASK_PID"
        # Wait returns status of the killed process and with set -e this breaks the script
        wait "$TASK_PID" || true
    fi

    # SIGTERM comes from docker stop so treat it as normal signal
    exit 0
}

trap 'term_handler' SIGTERM

python -u demo.py &
TASK_PID=$!
wait "$TASK_PID"
