import socket
import ssl
import threading
import sys

server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("\nNhận:", data.decode('utf-8'))
            print("nhap tin nhan: ", end="", flush=True)
    except:
        pass
    finally:
        ssl_socket.close()
        print("\nket noi da dong.")

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.verify_mode = ssl.CERT_NONE 
    context.check_hostname = False
    
    ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    ssl_socket.connect(server_address)
    
    receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
    receive_thread.start()
    
    try:
        while True:
            message = input("nhap tin nhan: ")
            if message.strip() == "":
                continue
            ssl_socket.send(message.encode('utf-8'))
    except (KeyboardInterrupt, SystemExit):
        print("\ndang thoat")
    finally:
        ssl_socket.close()

if __name__ == "__main__":
    main()