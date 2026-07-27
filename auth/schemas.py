from pydantic import BaseModel, EmailStr

#new user create
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password:str
    role:str
#user login
class UserLogin(BaseModel):
    username:str
    password: str