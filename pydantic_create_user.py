from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class UserBaseSchema(BaseModel):
    """Base schema with common user fields."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )

    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class UserSchema(UserBaseSchema):
    """Schema for user data returned by the API."""

    id: str


class CreateUserRequestSchema(UserBaseSchema):
    """Schema for user creation request."""

    password: str


class CreateUserResponseSchema(BaseModel):
    """Schema for user creation response."""

    user: UserSchema
