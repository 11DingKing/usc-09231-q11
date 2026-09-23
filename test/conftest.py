"""Shared pytest fixtures for the standalone defect-reproduction snapshot.

This snapshot only keeps the sources required to reproduce the defect, so the
full ``beets`` package (plugins, helpers, configuration) is expected to be
installed. Before tests are collected, the snapshot's own
``beets/metadata_plugins.py`` is loaded in place of the installed copy. This
ensures ``python3 -m pytest`` exercises the source under test instead of a
possibly older file shipped in the installed package.

The ``config`` fixture reproduces the one provided by the upstream test
infrastructure, which is not part of the installed package.
"""

import importlib.util
import sys
from pathlib import Path

import beets
import pytest
from beets.test.helper import ConfigMixin

_SNAPSHOT_SOURCE = (
    Path(__file__).resolve().parent.parent
    / "beets"
    / "metadata_plugins.py"
)

_spec = importlib.util.spec_from_file_location(
    "beets.metadata_plugins", _SNAPSHOT_SOURCE
)
_snapshot_module = importlib.util.module_from_spec(_spec)
sys.modules["beets.metadata_plugins"] = _snapshot_module
_spec.loader.exec_module(_snapshot_module)
setattr(beets, "metadata_plugins", _snapshot_module)


class _ConfigProvider(ConfigMixin):
    pass


@pytest.fixture
def config():
    """Yield an isolated, reset global beets configuration."""
    yield _ConfigProvider().config
