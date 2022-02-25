from pydantic import BaseModel, HttpUrl

from typing import Sequence


class SKUs(BaseModel):
    skuKey: str
    demandFactor: int
    maxQuantity: int
    minQuantity: int


class SinkLocations(BaseModel):
    locationKey: str
    skus: SKUs

# class Recipe(BaseModel):
#     id: int
#     label: str
#     source: str
#     url: HttpUrl


# class RecipeSearchResults(BaseModel):
#     results: Sequence[Recipe]


# class RecipeCreate(BaseModel):
#     label: str
#     source: str
#     url: HttpUrl
#     submitter_id: int
