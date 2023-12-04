from pydantic import BaseModel, ConfigDict, Field


class SAnalogy(BaseModel):
    source: str
    link: str
    description: str

    class Config:
        json_schema_extra = {
            "example": {
                "source": "source1",
                "link": "link1",
                "description": "some text",
            }
        }


class SAnalogyOut(SAnalogy):
    model_config = ConfigDict(from_attributes=True)
    id: int = Field(..., example=123)
