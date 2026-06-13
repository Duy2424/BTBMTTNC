# Server SSL: nhan ket noi tu client va giai ma du lieu qua SSL
import socket
import ssl

HOST = "localhost"
PORT = 8443

# Duong dan den chung chi va khoa rieng
CERT_FILE = "certificates/server-cert.crt"
KEY_FILE = "certificates/server-key.key"


def main():
    # Tao SSL context cho server
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    # Tao socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server SSL dang lang nghe tai {HOST}:{PORT}")

    # Boc socket bang SSL
    with context.wrap_socket(server_socket, server_side=True) as ssl_socket:
        while True:
            client_socket, addr = ssl_socket.accept()
            print("Ket noi tu:", addr)
            data = client_socket.recv(1024).decode("utf-8")
            print("Nhan duoc tu client:", data)
            client_socket.send("Server da nhan tin nhan".encode("utf-8"))
            client_socket.close()


if __name__ == "__main__":
    main()
