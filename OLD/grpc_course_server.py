from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки gRPC

import course_service_pb2  # Сгенерированные классы для работы с gRPC-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом


# Реализация gRPC-сервиса
class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса UserService"""

    def GetCourse(self, request, context):
        """Метод GetUser обрабатывает входящий запрос"""
        title = "Автотесты API"
        description = "Будем изучать написание API автотестов"
        print(f'Получен запрос к методу GetUser от пользователя: {request.course_id}')

        # Формируем и возвращаем ответное сообщение
        return course_service_pb2.GetCourseResponse(message=f'course_id: "{request.course_id}"\ntitle: "{title}"\ndescription: "{description}!"')


# Функция для запуска gRPC-сервера
def serve():
    """Функция создает и запускает gRPC-сервер"""

    # Создаем сервер с использованием пула потоков (до 5 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))

    # Регистрируем сервис CourseService на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()