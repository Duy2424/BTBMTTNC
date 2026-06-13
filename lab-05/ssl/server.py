import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

# Danh sách các client đã kết nối
clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    
    print("da ket noi voi:", client_socket.getpeername())
    
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("nhan:", data.decode('utf-8'))
            
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
    except:
        if client_socket in clients:
            clients.remove(client_socket)
    finally:
        try:
            print("da ngat ket noi:", client_socket.getpeername())
        except:
            print("mot ket noi da ngta.")
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)
    
    print("sever dang cho ket noi")
    
    while True:
        client_socket, client_address = server_socket.accept()
        
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile="./certificates/server-cert.crt", keyfile="./certificates/server-key.key")
        
        try:
            ssl_socket = context.wrap_socket(client_socket, server_side=True)
            
            client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
            client_thread.start()
        except Exception as e:
            print(f"loi: {e}")
            client_socket.close()

if __name__ == "__main__":
    main()