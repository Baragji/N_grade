#!/bin/bash
set -euo pipefail

python -m http.server 8000 --directory /app/src
