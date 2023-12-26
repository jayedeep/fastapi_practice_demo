from pydantic import BaseModel,validator


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str

    
    @validator("name")
    def validate_name(cls, value):
        if len(value) < 4:
            raise ValueError("name must be greater then 4 letter")
        return value

class UserObj(BaseModel):
    name: str
    email: str
    password: str

    class Meta:
        orm_mode = True