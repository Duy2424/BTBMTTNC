import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

server_key = RSA.generate(2048)
aes_key = get_random_bytes(16)
clients = []


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    pad_len = AES.block_size - len(message) % AES.block_size
    padded_message = message + pad_len * chr(pad_len)
    encrypted_message = cipher.iv + cipher.encrypt(padded_message.encode())
    return encrypted_message


def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(encrypted_message[AES.block_size:])
    unpadded_message = decrypted_message[:-decrypted_message[-1]]
    return unpadded_message.decode()


def handle_client(client_socket, client_address):
    print(f"Ket noi tu {client_address}")
    client_socket.send(server_key.publickey().export_key(format='PEM'))
    client_public_key = RSA.import_key(client_socket.recv(2048))
    cipher_rsa = PKCS1_OAEP.new(client_public_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    client_socket.send(encrypted_aes_key)

    clients.append(client_socket)

    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            message = decrypt_message(aes_key, encrypted_message)
            print(f"Tin nhan tu {client_address}: {message}")
            if message == "exit":
                break
            for client in clients:
                if client != client_socket:
                    client.send(encrypt_message(aes_key, message))
        except Exception:
            break

    clients.remove(client_socket)
    client_socket.close()
    print(f"Ngat ket noi voi {client_address}")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print("Server dang lang nghe tai cong 12345 ...")

while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client,
                                     args=(client_socket, client_address))
    client_thread.start()
