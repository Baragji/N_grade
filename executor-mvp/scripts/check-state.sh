#!/usr/bin/env bash
set -euo pipefail
[ -f docs/state_management/NOW.md ] || { echo "Missing docs/state_management/NOW.md"; exit 1; }
[ -f docs/state_management/NEXT.md ] || { echo "Missing docs/state_management/NEXT.md"; exit 1; }
[ -f docs/state_management/DECISIONS.md ] || { echo "Missing docs/state_management/DECISIONS.md"; exit 1; }
[ -d docs/state_management/session ] || { echo "Missing docs/state_management/session"; exit 1; }
latest="$(ls -1 docs/state_management/session/*.json 2>/dev/null | tail -n 1 || true)"
[ -n "$latest" ] || { echo "No session JSON found in docs/state_management/session"; exit 1; }
echo "STATE OK: $latest"
