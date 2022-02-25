from fastapi import FastAPI, APIRouter, Body

from pydantic import BaseModel, HttpUrl

from typing import Sequence, List


class SKUs(BaseModel):
    skuKey: str
    demandFactor: int = None
    maxQuantity: int = None
    minQuantity: int = None


class SinkLocations(BaseModel):
    locationKey: str
    skus: SKUs


class SourceLocations(BaseModel):
    locationKey: str
    skus: SKUs


class Groups(BaseModel):
    groupKey: str
    sourceLocations: List[SourceLocations]
    sinkLocations: List[SinkLocations]


app = FastAPI(title="aifora API", openapi_url="/openapi.json")

api_router = APIRouter()


@app.put("/optimization/{groupKey}")
async def update_group(*, groupKey: str, groups: Groups = Body(..., embed=True)):
    results = {"groups": groups}
    return results

app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
