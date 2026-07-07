from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    GetExerciseResponseSchema,
    GetExercisesResponseSchema,
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema
)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Получает список заданий для определённого курса.

        :param query: Query-параметры запроса с идентификатором курса courseId.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.get(url="/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает информацию о задании по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Создаёт новое задание.

        :param request: Тело запроса с данными нового задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.post(url="/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Обновляет данные задания по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :param request: Тело запроса с обновлёнными данными задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: HTTP-ответ сервера в виде объекта httpx.Response.
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получает список заданий и возвращает JSON-ответ.

        :param query: Query-параметры запроса с идентификатором курса courseId.
        :return: JSON-ответ со списком заданий.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Получает одно задание и возвращает JSON-ответ.

        :param exercise_id: Идентификатор задания.
        :return: JSON-ответ с данными задания.
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Создаёт задание и возвращает JSON-ответ.

        :param request: Тело запроса с данными нового задания.
        :return: JSON-ответ с данными созданного задания.
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(
            self,
            exercise_id: str,
            request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        """
        Обновляет задание и возвращает JSON-ответ.

        :param exercise_id: Идентификатор задания.
        :param request: Тело запроса с обновлёнными данными задания.
        :return: JSON-ответ с данными обновлённого задания.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :param user: Данные пользователя для авторизации.
    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
