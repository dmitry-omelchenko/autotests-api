from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания юзера.
    """
    email: str
    password: str


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
        return self.client.post(url="/api/v1/users", json=request)