"""Mirrored dataset entries record original_urls (possibly empty)."""
from __future__ import absolute_import

import pods


def test_mirrored_datasets_have_original_urls_list():
    """Every datasets_mirror download entry has an original_urls list."""
    lacking = []
    bad_type = []
    for name, rec in pods.access.data_resources.items():
        urls = rec.get("urls") or []
        if not any("datasets_mirror" in (u or "") for u in urls):
            continue
        if "original_urls" not in rec:
            lacking.append(name)
            continue
        originals = rec["original_urls"]
        if not isinstance(originals, list) or any(
            not isinstance(u, str) for u in originals
        ):
            bad_type.append(name)

    assert lacking == [], (
        "mirrored datasets missing original_urls: " + ", ".join(sorted(lacking))
    )
    assert bad_type == [], (
        "mirrored datasets with non-list original_urls: "
        + ", ".join(sorted(bad_type))
    )
