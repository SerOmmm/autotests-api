import grpc

import user_service_pb2
import user_service_pb2_grpc

# Устанавливаем соединение с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = user_service_pb2_grpc.UserServiceStub(channel)

# Отправляем запрос
for c in ("Alice", 'Bob', 'Marvel', 'Optimus', 'Salage', 'Marines', 'Indigo'):
    response = stub.GetUser(user_service_pb2.GetUserRequest(username=c))
    print(response.message)  # Выведет: Привет, Alice!