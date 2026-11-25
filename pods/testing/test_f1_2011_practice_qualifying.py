"""Offline tests for pods.datasets.f1_2011_practice_qualifying (CIP-0005)."""

from __future__ import annotations

import os
from pathlib import Path
from unittest import mock

import numpy as np
import pytest

import pods

FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "f1_2011_practice_qualifying"


@pytest.fixture
def fixture_datapath(tmp_path, monkeypatch):
    """Point DATAPATH at a cache seeded from tiny GreatBritain fixtures."""
    cache = tmp_path / "datasets"
    dest = cache / "f1_2011_practice_qualifying_GreatBritain" / "GreatBritain"
    dest.mkdir(parents=True)
    for name in ("FP3_laps.csv", "Q_laps.csv"):
        (dest / name).write_text((FIXTURE_ROOT / "GreatBritain" / name).read_text())
    monkeypatch.setattr(pods.access, "DATAPATH", str(cache))
    monkeypatch.setattr(pods.datasets, "DATAPATH", str(cache))
    return cache


def test_f1_2011_rejects_unknown_grand_prix():
    with pytest.raises(ValueError, match="Unknown grand_prix"):
        pods.datasets.f1_2011_practice_qualifying(grand_prix="NotARace")


def test_f1_2011_rejects_belgium_fp1():
    with pytest.raises(ValueError, match="Belgium has no FP1"):
        pods.datasets.f1_2011_practice_qualifying(
            grand_prix="Belgium", practice="FP1"
        )


def test_f1_2011_from_fixtures(fixture_datapath):
    with mock.patch.object(pods.access, "download_data", side_effect=AssertionError("network")):
        data = pods.datasets.f1_2011_practice_qualifying(
            grand_prix="GreatBritain", practice="FP3"
        )

    assert data["X"].shape == (2, 1)
    assert data["Y"].shape == (2, 3)
    assert list(data["driver_number"]) == [1, 2]
    assert list(data["abbreviation"]) == ["Vet", "Web"]
    np.testing.assert_allclose(data["X"].ravel(), [91.5, 91.8])
    np.testing.assert_allclose(data["Y"][0], [92.9, 91.2, 90.5])
    np.testing.assert_allclose(data["Y"][1], [92.5, 91.0, 90.4])
    assert len(data["practice_laps"]) == 5
    assert len(data["qualifying_laps"]) == 6
    assert data["grand_prix"] == "GreatBritain"
    assert data["year"] == 2011


def test_f1_2011_catalogue_points_at_mirror():
    resource = pods.access.data_resources["f1_2011_practice_qualifying"]
    assert "datasets_mirror" in resource["urls"][0]
    assert "f1_2011_practice_qualifying" in resource["urls"][0]
    assert resource["size"] > 0
