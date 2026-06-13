import tornado.ioloop
import tornado.websocket

URL = "ws://localhost:8888/websocket"


async def main():
    client = await tornado.websocket.websocket_connect(URL)
    print("Da ket noi den server:", URL)

    while True:
        message = await client.read_message()
        if message is None:
            print("Ket noi da dong.")
            break
        print("Nhan duoc trai cay:", message)


if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(main)
