#!/usr/bin/env bash
set -e

echo "===== Customizing AI Environment ====="

# Setup local Python environment parameters dynamically
if [ ! -d .venv ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install --upgrade pip
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

if ! grep -q "source \$(pwd)/.venv/bin/activate" ~/.bashrc; then
    echo "source \$(pwd)/.venv/bin/activate" >> ~/.bashrc
fi

# Synclink workspace skills natively - pull latest and re-symlink
SUPERPOWERS_DIR="$HOME/.superpowers"
if [ -d "$SUPERPOWERS_DIR" ]; then
    git -C "$SUPERPOWERS_DIR" pull --rebase --ff-only 2>/dev/null || git -C "$SUPERPOWERS_DIR" pull --rebase
fi

OPENCODE_SKILLS="$HOME/.config/opencode/skills"
mkdir -p "$OPENCODE_SKILLS"
rm -f "$OPENCODE_SKILLS"/*

if [ -d "$SUPERPOWERS_DIR/skills" ]; then
    find "$SUPERPOWERS_DIR/skills" -mindepth 1 -maxdepth 1 -exec ln -sfn {} "$OPENCODE_SKILLS/" \;
fi

if [ ! -f .env ] && [ -f .env.template ]; then
    cp .env.template .env
fi

echo "Environment operational."
