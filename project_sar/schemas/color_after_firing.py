from pydantic import BaseModel


class SColorAfterFiring(BaseModel):
    red: int = 0
    grey: int = 0
    white: int = 0

    class Config:
        json_schema_extra = {
            "example": {
                "red": 3,
                "grey": 0,
                "white": 7,
            }
        }


class SColorAfterFiringOut(SColorAfterFiring):
    pass
