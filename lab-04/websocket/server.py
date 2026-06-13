import random
import tornado.ioloop
import tornado.web
import tornado.websocket

clients = []

fruits = ["Apple", "Banana", "Orange", "Mango", "Grape",
          "Pineapple", "Strawberry", "Watermelon", "Kiwi", "Peach"]


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        clients.append(self)
        print("Client da ket noi. Tong so client:", len(clients))

    def on_close(self):
        if self in clients:
            clients.remove(self)
        print("Client da ngat ket noi. Tong so client:", len(clients))

    def on_message(self, message):
        print("Nhan tu client:", message)


def send_fruit():
    fruit = random.choice(fruits)
    print("Gui:", fruit)
    for client in clients:
        client.write_message(fruit)


def make_app():
    return tornado.web.Application([
        (r"/websocket", WebSocketHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server dang chay tai ws://localhost:8888/websocket")

    tornado.ioloop.PeriodicCallback(send_fruit, 3000).start()
    tornado.ioloop.IOLoop.current().start()
