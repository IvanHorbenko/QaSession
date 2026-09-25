from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str | None = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserProfile(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str | None = None

    class Config:
        from_attributes = True


class UserProfileUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None


class ChangePassword(BaseModel):
    current_password: str
    new_password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
