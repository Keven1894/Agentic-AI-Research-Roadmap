"""REPO_ROOT resolution — the seam that makes AgentLoom reusable by other repos.

A domain agent (marketing, research, …) installs AgentLoom as a dependency and
expects the inherited validators to check *its* knowledge graphs. Before
``$AGENTLOOM_REPO_ROOT`` was honored, resolution walked up from the installed
package's own location, so those validators silently checked AgentLoom's graphs
and reported PASS. Silently passing the wrong target is the worst failure mode a
governance framework can have, hence a test.
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

_PRINT_ROOT = "import agentloom; print(agentloom.REPO_ROOT)"


def _resolve(env_extra: dict[str, str] | None = None, cwd: Path | None = None) -> str:
    import os

    env = dict(os.environ)
    env.pop("AGENTLOOM_REPO_ROOT", None)
    if env_extra:
        env.update(env_extra)
    out = subprocess.run(
        [sys.executable, "-c", _PRINT_ROOT],
        env=env, cwd=cwd, capture_output=True, text=True, check=True,
    )
    return out.stdout.strip()


def test_walk_up_when_env_unset():
    """Unchanged in-repo behavior: find the nearest ancestor holding the KG dir."""
    assert _resolve() == str(REPO_ROOT)


def test_env_override_wins(tmp_path):
    """A consumer repo points resolution at itself."""
    (tmp_path / "agents" / "knowledge-graphs").mkdir(parents=True)
    assert _resolve({"AGENTLOOM_REPO_ROOT": str(tmp_path)}) == str(tmp_path.resolve())


def test_override_need_not_contain_a_kg_dir_yet(tmp_path):
    """Bootstrapping a new domain repo must not require the KG dir to exist first.

    The override is taken at face value; a missing KG dir is then reported by the
    validators themselves, which name the missing file. Falling back to the
    walk-up here would resurrect the silent-wrong-target bug.
    """
    assert _resolve({"AGENTLOOM_REPO_ROOT": str(tmp_path)}) == str(tmp_path.resolve())


def test_blank_override_is_ignored():
    assert _resolve({"AGENTLOOM_REPO_ROOT": "   "}) == str(REPO_ROOT)


def test_resolution_is_independent_of_cwd(tmp_path):
    """Validators are invoked from many places; cwd must not change the target."""
    assert _resolve(cwd=tmp_path) == str(REPO_ROOT)
