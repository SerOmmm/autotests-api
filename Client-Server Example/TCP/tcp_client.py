import socket
import time

# Создаем TCP-сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 12345)
try:
    client_socket.connect(server_address)
    messages = ["Привет!", "Как дела?", "Пойдем гулять?"]

    for msg in messages:
        client_socket.send(msg.encode())
        print(f"Отправлено: {msg}")
        response = client_socket.recv(1024).decode()
        print(f"Ответ сервера: {response}")
        time.sleep(2)

except ConnectionRefusedError:
    print("Сервер недоступен!")
except ConnectionResetError:
    print("Сервер разорвал соединение!")
finally:
    client_socket.close()  # Закрываем сокет
    print("Клиент завершил работу.")
