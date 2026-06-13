import socket
import threading
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

client_key = RSA.generate(2048)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

server_public_key = RSA.import_key(client_socket.recv(2048))
client_socket.send(client_key.publickey().export_key(format='PEM'))
encrypted_aes_key = client_socket.recv(1024)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)
print("Da nhan duoc khoa AES tu server")


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


def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            message = decrypt_message(aes_key, encrypted_message)
            print(f"Tin nhan nhan duoc: {message}")
        except Exception:
            break


receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    encrypted_message = encrypt_message(aes_key, message)
    client_socket.send(encrypted_message)
    if message == "exit":
        break

client_socket.close()
