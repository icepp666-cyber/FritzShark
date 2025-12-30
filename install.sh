#!/bin/bash

# ──────────────────────────────────────────────
# 🚫 BLOCK: Deny Root execution
# ──────────────────────────────────────────────
if [ "$(id -u)" -eq 0 ]; then
    echo "❌ Do NOT run this script as root (e.g. with sudo, sudo su, or GUI root terminal)."
    echo "   Please run it as a regular user. Root access will be requested automatically."
    exit 1
fi

# ──────────────────────────────────────────────
# ▶️ Run builder
# ──────────────────────────────────────────────
chmod +x "$PWD/scripts/builder"
HELLO=1 bash "$PWD/scripts/builder"

