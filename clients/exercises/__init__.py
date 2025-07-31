import httpx

from clients.api_client import APIClient


class ExercisesClient(APIClient):


    # get_exercises_api – GET / api / v1 / exercises.Получение
    # списка     заданий     для     определенного     курса.
    # get_exercise_api – GET / api / v1 / exercises / {exercise_id}.Получение
    # информации      о     задании     по     exercise_id.
    # create_exercise_api – POST / api / v1 / exercises.Создание     задания.
    # update_exercise_api – PATCH / api / v1 / exercises / {exercise_id}.Обновления
    # данных     задания.
    # delete_exercise_api – DELETE / api / v1 / exercises / {exercise_id}.Удаление
    # задания.