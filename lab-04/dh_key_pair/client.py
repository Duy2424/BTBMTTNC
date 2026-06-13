from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Doc tham so DH tu file do server tao
with open("dh_parameters.pem", "rb") as f:
    parameters = serialization.load_pem_parameters(f.read())

# Doc public key cua server
with open("server_public_key.pem", "rb") as f:
    server_public_key = serialization.load_pem_public_key(f.read())

# Tao cap khoa cua client
client_private_key = parameters.generate_private_key()
client_public_key = client_private_key.public_key()

# Luu public key cua client ra file de server su dung
with open("client_public_key.pem", "wb") as f:
    f.write(client_public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo))

print("Da tao client_public_key.pem")

# Tinh khoa bi mat duoc chia se
shared_key = client_private_key.exchange(server_public_key)
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)

print(f"Thong diep bi mat duoc chia se (client): {derived_key.hex()}")
