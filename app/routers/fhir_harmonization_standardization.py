from fastapi import APIRouter

router = APIRouter(
    prefix="/fhir/harmonization/standardization",
    tags=["fhir/harmonization"],
)


@router.post("/standardize_names")
async def standardize_names_endpoint(body) -> dict:
    return body


@router.post("/standardize_phones")
async def standardize_phones_endpoint(body) -> dict:
    return body
