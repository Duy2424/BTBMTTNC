# WebSocket server su dung Tornado
# Cu moi 3 giay, server gui ten mot loai trai cay den tat ca client
import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Danh sach client dang ket noi
clients = []

# Danh sach trai cay
fruits = ["Apple", "Banana", "Orange", "Mango", "Grape",
          "Pineapple", "Strawberry", "Watermelon", "Kiwi", "Peach"]


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        # Khi co client ket noi
        clients.append(self)
        print("Client da ket noi. Tong so client:", len(clients))

    def on_close(self):
        # Khi client ngat ket noi
        if self in clients:
            clients.remove(self)
        print("Client da ngat ket noi. Tong so client:", len(clients))

    def on_message(self, message):
        print("Nhan tu client:", message)


def send_fruit():
    # Gui ten mot loai trai cay ngau nhien den tat ca client
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

    # Cu moi 3000ms (3 giay) gui mot loai trai cay
    tornado.ioloop.PeriodicCallback(send_fruit, 3000).start()
    tornado.ioloop.IOLoop.current().start()
