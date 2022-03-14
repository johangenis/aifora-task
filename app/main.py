from fastapi import FastAPI, APIRouter, Body

from pydantic import BaseModel, HttpUrl

from typing import Sequence, Optional

app = FastAPI(title="aifora API", openapi_url="/openapi.json")

OPTIMIZE_GROUPS = []
MOVEMENTS_GROUPS = []


class SKUs(BaseModel):
    skuKey: str
    demandFactor: Optional[int]
    maxQuantity: Optional[int]
    minQuantity: Optional[int]


class SinkLocations(BaseModel):
    locationKey: str
    skus: list[SKUs]


class SourceLocations(BaseModel):
    locationKey: str
    skus: list[SKUs]


class Group(BaseModel):
    groupKey: str
    sourceLocations: list[SourceLocations]
    sinkLocations: list[SinkLocations]


class Movement(BaseModel):
    allocationQuantity: int
    sinkLocationKey: str
    skuKey: str
    sourceLocationKey: str


class Movements(BaseModel):
    groupKey: str
    movements: list[Movement]


class OptimizeGroups(BaseModel):
    groups: list[Group]


class MovementsGroups(BaseModel):
    groups: list[Movements]


@app.post("/optimize/")
async def create_optimize_groups(groups: OptimizeGroups):
    OPTIMIZE_GROUPS.append(groups)
    return groups


@app.post("/movements/")
async def create_movements_groups(groups: MovementsGroups):
    MOVEMENTS_GROUPS.append(groups)
    return groups


@app.get("/optimize/")
async def list_optimize_groups():
    return OPTIMIZE_GROUPS


@app.get("/movements/")
async def list_movements_groups():
    return MOVEMENTS_GROUPS

api_router = APIRouter()

app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
