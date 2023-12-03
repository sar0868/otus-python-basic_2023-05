from pydantic import BaseModel, Field, NonNegativeInt, ConfigDict

from .analogy import SAnalogy
from .color_after_firing import SColorAfterFiringOut
from .part_of_the_pot import SPartPotOut
from .vessel_type import SVesselTypesOut


class SPackage(BaseModel):
    number: NonNegativeInt
    passport: str
    layer_number: NonNegativeInt
    mainland_hole: str = Field(max_length=20)
    object_study_id: int

    class Config:
        json_schema_extra = {
            "example": {
                "object_study_id": 1,
                "number": 1,
                "passport": "кв.А-1 гл -120 сл.т-к.суп",
                "layer_number": 1,
                "mainland_hole": "м.я. 1",
            }
        }


class SPackageOut(SPackage):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., example=123)


class SPackageOutFull(SPackage):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., example=123)
    vessel_types: SVesselTypesOut
    part_of_the_pots: SPartPotOut
    color_after_firing: SColorAfterFiringOut


class SPackageAnalogies(BaseModel):
    layer_number: int
    analogies: list[SAnalogy]
