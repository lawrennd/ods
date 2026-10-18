"""Tests for the East Timor language-regions dataset."""
from __future__ import absolute_import

import mock
import numpy as np
import pods


def test_east_timor_load_and_shape():
    """east_timor downloads from the mirror and returns X, Y, polygons."""
    pods.access.clear_cache("east_timor")
    with mock.patch("builtins.input", return_value="Y"):
        data = pods.datasets.east_timor()

    assert "X" in data
    assert "Y" in data
    assert "polygons" in data
    assert data["X"].shape == (67, 2)
    assert data["Y"].shape[0] == 67
    assert len(data["polygons"]) == 67
    assert set(np.unique(data["Y"]).tolist()).issubset({0, 1})
    assert "citation" in data
    assert "Zwiessele" in (data.get("citation") or "")
