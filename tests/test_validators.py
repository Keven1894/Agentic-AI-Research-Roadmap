"""Governance gate as a pytest suite.

These tests are thin wrappers over AgentLoom's own validators so that the full
KG + Tier-A governance gate runs under `pytest` (and therefore in CI) exactly as
it does via `make validate-all`.
"""
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

GATES = [
    pytest.param("agentloom.kg.validate_all", id="kg-validate-all"),
    pytest.param("agentloom.validators.run_all", id="tier-a-validators"),
]


@pytest.mark.parametrize("module", GATES)
def test_governance_gate(module):
    # Pin the target explicitly. A developer working on a downstream domain agent
    # will have AGENTLOOM_REPO_ROOT exported in their shell, and inheriting it here
    # would point AgentLoom's own gate at that other repo.
    env = dict(os.environ)
    env["AGENTLOOM_REPO_ROOT"] = str(REPO_ROOT)
    result = subprocess.run(
        [sys.executable, "-m", module],
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, (
        f"{module} failed (exit {result.returncode}).\n"
        f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}"
    )
