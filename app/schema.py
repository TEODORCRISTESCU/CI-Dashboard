from uuid import UUID
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class BuildCreate(BaseModel):
    repo : str
    branch : str
    commit_sha : str 

class BuildSummary(BaseModel):
    id : UUID
    repo: str
    branch: str
    commit_sha : str
    status : str
    created_at : datetime
    model_config  = ConfigDict(from_attributes=True)