# Client SSL: ket noi va gui du lieu len server qua SSL
import socket
import ssl

HOST = "localhost"
PORT = 8443


def main():
    # Tao SSL context cho client
    # Vi dung chung chi tu ky (self-signed) nen tat kiem tra chung chi
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    # Tao socket va boc SSL
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_socket = context.wrap_socket(client_socket, server_hostname=HOST)
    ssl_socket.connect((HOST, PORT))
    print(f"Da ket noi den server SSL {HOST}:{PORT}")

    # Nhap va gui tin nhan
    message = input("Nhap tin nhan gui den server: ")
    ssl_socket.send(message.encode("utf-8"))

    # Nhan phan hoi tu server
    response = ssl_socket.recv(1024).decode("utf-8")
    print("Phan hoi tu server:", response)

    ssl_socket.close()


if __name__ == "__main__":
    main()
