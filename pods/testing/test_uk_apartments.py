"""Tests for uk_apartments monthly Price Paid loading."""
from __future__ import absolute_import

import os

import numpy as np
import pytest
from unittest.mock import patch

import pods
import pods.datasets


def _write_monthly(path, rows, header=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = []
    if header:
        lines.append(
            "Unique ID,Price,date,Postcode,Property type,old/new,Duration,"
            "PAON,SAON,Street,Locality,Town,District,County,Record Status"
        )
    lines.extend(rows)
    with open(path, "w", encoding="latin-1") as fh:
        fh.write("\n".join(lines) + "\n")


ROW_F_A = (
    "{AAAAAAAA-AAAA-AAAA-AAAA-AAAAAAAAAAAA},250000,15/03/2012 00:00,"
    "SW1A 1AA,F,N,L,1,,DOWNING STREET,WESTMINSTER,LONDON,WESTMINSTER,"
    "GREATER LONDON,A"
)
ROW_T_A = (
    "{BBBBBBBB-BBBB-BBBB-BBBB-BBBBBBBBBBBB},400000,16/03/2012 00:00,"
    "SW1A 2AA,T,N,F,2,,WHITEHALL,WESTMINSTER,LONDON,WESTMINSTER,"
    "GREATER LONDON,A"
)
ROW_F_C = (
    "{CCCCCCCC-CCCC-CCCC-CCCC-CCCCCCCCCCCC},260000,17/03/2012 00:00,"
    "SW1A 3AA,F,N,L,3,,KING CHARLES ST,WESTMINSTER,LONDON,WESTMINSTER,"
    "GREATER LONDON,C"
)
ROW_F_POUND = (
    '{DDDDDDDD-DDDD-DDDD-DDDD-DDDDDDDDDDDD},"£13,500,000",14/06/2012 00:00,'
    "SW1A 1RA,F,N,L,1,,THE MALL,WESTMINSTER,LONDON,WESTMINSTER,"
    "GREATER LONDON,A"
)


def test_uk_apartments_resource_and_url_pattern():
    resource = pods.access.data_resources["uk_apartments"]
    base = resource["urls"][0]
    assert "datasets_mirror" in base
    assert base.endswith("uk_apartments/")
    assert isinstance(resource["original_urls"], list)
    assert resource["original_urls"]
    season_url = base + "monthly_2012/"
    assert season_url.endswith("monthly_2012/")


def test_uk_apartments_month_range():
    months = pods.datasets._uk_apartments_month_range("2012-11", "2013-02")
    assert months == ["2012-11", "2012-12", "2013-01", "2013-02"]
    with pytest.raises(ValueError):
        pods.datasets._uk_apartments_month_range("2012-10", "2012-02")
    with pytest.raises(ValueError):
        pods.datasets._uk_apartments_month_range("2012-01", "2012-10")


def test_uk_apartments_filters_and_encodings(tmp_path):
    y2012 = os.path.join(str(tmp_path), "uk_apartments_2012")
    _write_monthly(
        os.path.join(y2012, "2012-02.csv"),
        [ROW_F_A, ROW_T_A, ROW_F_C],
        header=True,
    )
    _write_monthly(
        os.path.join(y2012, "2012-06.csv"),
        [ROW_F_POUND],
        header=False,
    )
    with patch.object(pods.access, "DATAPATH", str(tmp_path)), patch.object(
        pods.access, "data_available", return_value=True
    ):
        flats = pods.datasets.uk_apartments(
            start="2012-02", end="2012-02", property_type="F"
        )
        assert flats["months"] == ["2012-02"]
        assert len(flats["frame"]) == 2
        assert set(flats["frame"]["record_status"]) == {"A", "C"}
        assert flats["Y"].shape == (2, 1)

        additions = pods.datasets.uk_apartments(
            start="2012-02", end="2012-02", property_type="F", record_status="A"
        )
        assert len(additions["frame"]) == 1
        assert additions["frame"]["record_status"].iloc[0] == "A"

        all_types = pods.datasets.uk_apartments(
            start="2012-02", end="2012-02", property_type=None
        )
        assert len(all_types["frame"]) == 3

        pricey = pods.datasets.uk_apartments(
            start="2012-06", end="2012-06", property_type="F"
        )
        assert pricey["Y"][0, 0] == 13500000
        assert np.isclose(pricey["logY"][0, 0], np.log(13500000))


def test_uk_apartments_spans_years(tmp_path):
    _write_monthly(
        os.path.join(str(tmp_path), "uk_apartments_2012", "2012-12.csv"),
        [ROW_F_A],
    )
    _write_monthly(
        os.path.join(str(tmp_path), "uk_apartments_2013", "2013-01.csv"),
        [ROW_F_C],
    )
    with patch.object(pods.access, "DATAPATH", str(tmp_path)), patch.object(
        pods.access, "data_available", return_value=True
    ):
        data = pods.datasets.uk_apartments(
            start="2012-12", end="2013-01", property_type="F"
        )
    assert data["months"] == ["2012-12", "2013-01"]
    assert len(data["frame"]) == 2
    assert "uk_apartments_2012" in pods.access.data_resources
    assert pods.access.data_resources["uk_apartments_2012"]["urls"][0].endswith(
        "monthly_2012/"
    )
    assert pods.access.data_resources["uk_apartments_2013"]["urls"][0].endswith(
        "monthly_2013/"
    )
