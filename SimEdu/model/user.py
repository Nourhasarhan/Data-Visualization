# app/models/user.py
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    fullname: str
    # disabled: bool = False

class UserCreate(User):
    password: str

class UserInDB(User):
    hashed_password: str
