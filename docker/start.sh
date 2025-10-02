#!/bin/sh
set -eu

python -m http.server 8000 --directory /app/src
