"""Pytest scaffolding for the standalone snapshot.

The workspace only ships ``beets/metadata_plugins.py``, so the beets package
is expected to be installed in the environment to provide the remaining
modules (``beets.plugins``, ``beets.test.helper``, ...). Loading the snapshot
module under the ``beets.metadata_plugins`` name here ensures the tests
exercise the workspace copy instead of the installed one.
"""

import importlib.util
import sys
from pathlib import Path

import beets
import pytest

from beets.test.helper import ConfigMixin

_snapshot_path = Path(__file__).parent / "beets" / "metadata_plugins.py"
_spec = importlib.util.spec_from_file_location(
    "beets.metadata_plugins", _snapshot_path
)
_module = importlib.util.module_from_spec(_spec)
sys.modules["beets.metadata_plugins"] = _module
_spec.loader.exec_module(_module)
beets.metadata_plugins = _module


@pytest.fixture
def config():
    """Provide a fresh beets configuration when requested."""
    return ConfigMixin().config
