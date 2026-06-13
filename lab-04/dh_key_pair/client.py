from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

with open("dh_parameters.pem", "rb") as f:
    parameters = serialization.load_pem_parameters(f.read())

with open("server_public_key.pem", "rb") as f:
    server_public_key = serialization.load_pem_public_key(f.read())

client_private_key = parameters.generate_private_key()
client_public_key = client_private_key.public_key()

with open("client_public_key.pem", "wb") as f:
    f.write(client_public_key.public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo))

print("Da tao client_public_key.pem")

shared_key = client_private_key.exchange(server_public_key)
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(shared_key)

print(f"Thong diep bi mat duoc chia se (client): {derived_key.hex()}")
