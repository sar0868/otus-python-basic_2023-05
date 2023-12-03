from pydantic import BaseModel


class SPartPot(BaseModel):
    whisk: int = 0
    wall: int = 0
    bottom: int = 0

    class Config:
        json_schema_extra = {
            "example": {
                "whisk": 4,
                "wall": 3,
                "bottom": 3,
            }
        }


class SPartPotOut(SPartPot):
    pass
