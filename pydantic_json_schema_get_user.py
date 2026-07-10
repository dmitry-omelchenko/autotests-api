from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake


# Initialize PublicUsersClient
public_users_client = get_public_users_client()

# Initialize request for creating a user
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

# Create user
create_user_response = public_users_client.create_user(create_user_request)

# Initialize authentication data
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

# Initialize PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Get created user by ID
get_user_response = private_users_client.get_user_api(create_user_response.user.id)

# Generate JSON schema from Pydantic model
get_user_response_schema = GetUserResponseSchema.model_json_schema()

# Validate API response against JSON schema
validate_json_schema(
    instance=get_user_response.json(),
    schema=get_user_response_schema,
)
