"""AgentLoom — executable governance framework for builder agents.

Python code lives under ``src/agentloom/``. Data and content (knowledge graphs,
docs, ``.clinerules``) live at the repository root.

``REPO_ROOT`` resolution order:

1. ``$AGENTLOOM_REPO_ROOT`` if set — required when AgentLoom is installed as a
   dependency of a *domain* agent repo (e.g. a marketing or research agent).
   Without it the walk-up below finds AgentLoom's own root, so the validators
   would check the framework's knowledge graphs instead of the consumer's.
   Same variable name as ``agentloom_runtime.kg.paths``.
2. Walk up from this file to the nearest directory containing
   ``agents/knowledge-graphs`` — the in-repo case, unchanged.
"""

from __future__ import annotations

import os
from pathlib import Path

__version__ = "3.0.0"


def _find_repo_root() -> Path:
    override = os.environ.get("AGENTLOOM_REPO_ROOT", "").strip()
    if override:
        return Path(override).resolve()
    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if (candidate / "agents" / "knowledge-graphs").is_dir():
            return candidate
    # Fallback: src/agentloom/__init__.py -> repo root is parents[2]
    return here.parents[2]


REPO_ROOT = _find_repo_root()
KG_DIR = REPO_ROOT / "agents" / "knowledge-graphs"
DOCS_DIR = REPO_ROOT / "docs"
CLINERULES_DIR = REPO_ROOT / ".clinerules"

__all__ = ["REPO_ROOT", "KG_DIR", "DOCS_DIR", "CLINERULES_DIR", "__version__"]
