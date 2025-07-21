import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Сервер запущен и ждет подключений...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            ip, port = client_address
            print(f"Подключен клиент: {ip}:{port}")

            try:
                while True:
                    data = client_socket.recv(1024).decode()
                    if not data:  # Клиент закрыл соединение
                        break
                    print(f"Получено: {data}")
                    response = f"Сервер получил: {data}"
                    client_socket.send(response.encode())
            except ConnectionResetError:
                print("Клиент отключился неожиданно!")
            finally:
                client_socket.close()  # Закрываем сокет клиента
                print(f"Клиент {ip}:{port} отключен")
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        server_socket.close()  # Закрываем серверный сокет

if __name__ == '__main__':
    server()