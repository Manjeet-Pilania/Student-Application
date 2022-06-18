from pydantic import BaseModel

# Create students Schema (Pydantic Model)
class studentsCreate(BaseModel):
    task: str

# Complete students Schema (Pydantic Model)
class students(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True