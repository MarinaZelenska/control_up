import pytest

pytestmark = pytest.mark.api


def test_airport_count_is_30(api):
    data = api.get_json("/airports")
    airports = data.get("data", [])
    assert len(airports) == 30


def test_specific_airports_present(api):
    data = api.get_json("/airports")
    airports = data.get("data", [])
    airport_names = {airport.get("attributes", {}).get("name") for airport in airports}
    expected = {"Akureyri Airport", "St. Anthony Airport", "CFB Bagotville"}
    missing = expected - airport_names
    assert not missing, f"Missing expected airports: {missing}"


def test_distance_kix_nrt_gt_400_km(api):
    payload = {"from": "KIX", "to": "NRT"}
    data = api.post_json("/airports/distance", json=payload)
    km = (
        data.get("data", {})
        .get("attributes", {})
        .get("kilometers")
    )
    assert km is not None
    assert float(km) > 400.0
