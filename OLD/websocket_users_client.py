import asyncio
import websockets

async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")
        await websocket.send(message)

        try:
            while True:
                response = await websocket.recv()
                print(f"Ответ от сервера: {response}")
                if response[0] == '5':
                    break
        except websockets.exceptions.ConnectionClosedOK:
            print("Соединение закрыто сервером, завершение работы.")

asyncio.run(client())