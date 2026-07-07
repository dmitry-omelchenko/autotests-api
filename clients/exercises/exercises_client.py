from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str


class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения одного задания.
    """
    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: list[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания.
    """
    exercise: Exercise


class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получает список заданий для определённого курса.

        :param query: Query-параметры запроса с идентификатором курса courseId.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает информацию о задании по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создаёт новое задание.

        :param request: Тело запроса с данными нового задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновляет данные задания по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :param request: Тело запроса с обновлёнными данными задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получает список заданий и возвращает JSON-ответ.

        :param query: Query-параметры запроса с идентификатором курса courseId.
        :return: JSON-ответ со списком заданий.
        """
        response = self.get_exercises_api(query)
        return response.json()

    def get_exercise(self, exercise_id: str) -> GetExercisesResponseDict:
        """
        Получает одно задание и возвращает JSON-ответ.

        :param exercise_id: Идентификатор задания.
        :return: JSON-ответ с данными задания.
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создаёт задание и возвращает JSON-ответ.

        :param request: Тело запроса с данными нового задания.
        :return: JSON-ответ с данными созданного задания.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestDict
    ) -> UpdateExerciseResponseDict:
        """
        Обновляет задание и возвращает JSON-ответ.

        :param exercise_id: Идентификатор задания.
        :param request: Тело запроса с обновлёнными данными задания.
        :return: JSON-ответ с данными обновлённого задания.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Данные пользователя для авторизации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))