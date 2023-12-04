from pydantic import BaseModel, Field, ConfigDict


class SObjectStudy(BaseModel):
    place: str
    year: int
    description: str = Field(default="")
    number: int = Field(default=0)

    class Config:
        json_schema_extra = {
            "example": {"place": "city", "year": 2023, "description": "", "number": 0}
        }


class SObjectStudyOut(SObjectStudy):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., example=123)
