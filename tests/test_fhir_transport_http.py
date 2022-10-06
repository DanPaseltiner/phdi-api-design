import sys
import json
import copy
from fastapi.testclient import TestClient

sys.path.append("../")
sys.path.append("../app/")

from app.main import app

client = TestClient(app)

test_bundle = json.load(open("assets/single_patient_bundle.json"))

