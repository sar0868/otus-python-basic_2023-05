from pydantic import BaseModel


class SVesselTypes(BaseModel):
    pot: int
    lid: int
    jug: int
    bowl: int
    other: int

    class Config:
        json_schema_extra = {
            "example": {
                "pot": 4,
                "lid": 1,
                "jug": 0,
                "bowl": 3,
                "other": 2,
            }
        }


class SVesselTypesOut(SVesselTypes):
    pass
