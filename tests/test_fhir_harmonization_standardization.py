import sys
import json
import copy
from unittest import mock
from fastapi.testclient import TestClient

sys.path.append("../")
sys.path.append("../app/")

from app.main import app

client = TestClient(app)

test_bundle = json.load(open("assets/single_patient_bundle.json"))


def test_standardize_names_success():

    expected_response = copy.deepcopy(test_bundle)
    expected_response["entry"][0]["resource"]["name"][0]["family"] = "SMITH"
    expected_response["entry"][0]["resource"]["name"][0]["given"][0] = "DEEDEE"

    actual_response = client.post(
        "/fhir/harmonization/standardization/standardize_names",
        json={"data": test_bundle},
    )

    assert actual_response.json() == expected_response


def test_standardize_phones_success():

    expected_response = copy.deepcopy(test_bundle)
    expected_response["entry"][0]["resource"]["telecom"][0]["value"] = "+18015557777"

    actual_response = client.post(
        "/fhir/harmonization/standardization/standardize_names",
        json={"data": test_bundle},
    )

    assert actual_response.json() == expected_response
