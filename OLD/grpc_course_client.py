import grpc
from grpc import StatusCode
import course_service_pb2
import course_service_pb2_grpc

try:
    # Устанавливаем соединение с сервером
    channel = grpc.insecure_channel('localhost:50051')

    # Проверяем подключение (необязательно, но рекомендуется)
    try:
        grpc.channel_ready_future(channel).result(timeout=5)
    except grpc.FutureTimeoutError:
        raise ConnectionError('Не удалось подключиться к серверу')

    stub = course_service_pb2_grpc.CourseServiceStub(channel)

    # Отправляем запрос с обработкой ошибок
    try:
        response = stub.GetCourse(
            course_service_pb2.GetCourseRequest(course_id="api-course"),
            timeout=10  # Таймаут для вызова метода
        )
        print(response.message)

    except grpc.RpcError as rpc_error:
        if rpc_error.code() == StatusCode.UNAVAILABLE:
            raise ConnectionError('Сервер недоступен') from rpc_error
        elif rpc_error.code() == StatusCode.DEADLINE_EXCEEDED:
            raise TimeoutError('Превышено время ожидания ответа') from rpc_error
        else:
            raise RuntimeError(
                f'Ошибка при вызове метода: {rpc_error.code()}. Детали: {rpc_error.details()}'
            ) from rpc_error

except ConnectionError as conn_err:
    print(f'Ошибка подключения: {conn_err}')
except Exception as e:
    print(f'Непредвиденная ошибка: {e}')
finally:
    # Закрываем соединение при необходимости
    channel.close()
