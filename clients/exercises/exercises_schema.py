from pydantic import BaseModel, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """
    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True
    )

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    course_id: str = Field(alias="courseId")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения одного задания.
    """
    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: list[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int | None = Field(alias="orderIndex")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления задания.
    """
    exercise: ExerciseSchema