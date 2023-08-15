from pydantic import BaseModel
from datetime import datetime

class Rate(BaseModel):
    name = str


