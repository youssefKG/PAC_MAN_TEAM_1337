from uuid import uuid4
from pydantic import BaseModel, RootModel, Field

class PlayerScoreModel(BaseModel):
    id: str = Field(default=str(uuid4()))
    name: str
    avatar_img_path: str
    points: int

class PlayerScoreRootModel(RootModel[list[PlayerScoreModel]]):
    ...

