from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


# Добавили описание структуры пользователя
class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания юзера.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
    API-клиент для публичных методов пользователей, которые не требуют авторизации.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создаёт нового пользователя через публичный API-эндпоинт.

        :param request: Тело запроса с email и password пользователя.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/users", json=request)

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())