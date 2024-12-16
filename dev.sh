#!/bin/bash

# Start a new tmux session named 'dev' if it doesn't exist
tmux new-session -d -s dev

# Split the window vertically
tmux split-window -h

# In the left pane, run bun dev
tmux send-keys -t dev:0.0 'bun dev' C-m

# In the right pane, navigate to src/app/api/ai and run uv run fastapi dev
tmux send-keys -t dev:0.1 'cd src/app/api/ai && uv run fastapi dev' C-m

# Attach to the tmux session
tmux attach-session -t dev