from pydantic import BaseModel


class FilterRequest(BaseModel):
    content: str
