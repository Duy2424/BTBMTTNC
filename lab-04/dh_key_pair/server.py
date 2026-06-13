import os
import time
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Tao tham so Diffie-Hellman
parameters = dh.generate_parameters(generator=2, key_size=2048)

# Luu tham so DH ra file de client su dung
with open("dh_parameters.pem", "wb") as f:
    f.write(parameters.parameter_bytes(
        serialization.Encoding.PEM,
        serialization.ParameterFormat.PKCS3))

# Tao cap khoa cua server
server_private_key = parameters.generate_private_key()
server_public_key = server_private_key.public_key()

# Luu public key cua server ra file
with open("server_public_key.pem", "wb") as f:
    f.write(server_public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo))

print("Da tao server_public_key.pem")
print("Dang cho client_public_key.pem ...")

# Cho client tao public key
while not os.path.exists("client_public_key.pem"):
    time.sleep(1)

# Doc public key cua client
with open("client_public_key.pem", "rb") as f:
    client_public_key = serialization.load_pem_public_key(f.read())

# Tinh khoa bi mat duoc chia se
shared_key = server_private_key.exchange(client_public_key)
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)

print(f"Thong diep bi mat duoc chia se (server): {derived_key.hex()}")
