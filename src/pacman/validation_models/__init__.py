from pydantic import BaseModel, RootModel

class PlayerScoreModel(BaseModel):
    name: str
    avatar_img_path: str
    points: int

class PlayerScoreRootModel(RootModel[list[PlayerScoreModel]]):
    ...

