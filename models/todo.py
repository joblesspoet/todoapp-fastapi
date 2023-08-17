from pydantic import BaseModel


class TodoItem(BaseModel):
    id: int | None = None
    description: str
