#!/usr/bin/env python3
"""
Pytest configuration and path setup to ensure 'src' package is importable
when running tests directly from the repository root or CI.
"""

from __future__ import annotations

import sys
from pathlib import Path
import warnings

# Add project root and 'src' to sys.path for imports like 'from src...'
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"


def _ensure_path(p: Path) -> None:
    sp = str(p)
    if sp not in sys.path:
        sys.path.insert(0, sp)


_ensure_path(PROJECT_ROOT)
_ensure_path(SRC_DIR)

# Suppress deprecation noise from test fixtures using utcnow() while
# production code uses timezone-aware datetime.now(timezone.utc)
warnings.filterwarnings(
    "ignore",
    message=r"datetime\.utcnow\(\) is deprecated",
    category=DeprecationWarning,
)