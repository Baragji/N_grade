#!/usr/bin/env python3
import sys
import urllib.request

URL = "http://localhost:8000/"

try:
    with urllib.request.urlopen(URL, timeout=3) as r:
        sys.exit(0 if 200 <= r.status < 400 else 1)
except Exception:
    sys.exit(1)
