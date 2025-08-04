from pydantic import BaseModel, EmailStr, Field, constr


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: constr(min_length=3, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=3, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=3, max_length=50) = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: constr
    last_name: constr(min_length=3, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=3, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=3, max_length=50) = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


