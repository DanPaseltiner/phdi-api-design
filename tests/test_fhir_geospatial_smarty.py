import sys
import json
from unittest import mock
from fastapi.testclient import TestClient

sys.path.append("../")
sys.path.append("../app/")

from app.main import app

client = TestClient(app)

test_bundle = json.load(open("assets/single_patient_bundle.json"))

@mock.patch("app.router.fhir_geospatial_smarty.get_smartystreets_client")
@mock.patch("app.routers.fhir_geospatial_smarty.geocode_patients")
def test_geocode_bundle_success(patched_geocode_patients, patched_get_smartystreets_client):

    request_body = {"data":test_bundle, "auth_id": "some-auth-id", "auth_token": "some-auth-toke"}

    geocoder = mock.Mock()
    patched_get_smartystreets_client.return_value = geocoder

    client.post("/fhir/geospatial/smarty/gecode_bundle", json=request_body)

    assert patched_geocode_patients.called_with(bundle=test_bundle, client=geocoder)
