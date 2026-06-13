import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')


class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key)
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key)

    def load_keys(self):
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = RSA.import_key(p.read())
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = RSA.import_key(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode())
        return encrypted_message

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(ciphertext)
        return decrypted_message.decode()

    def sign(self, message, key):
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(key).sign(h)
        return signature

    def verify(self, message, signature, key):
        h = SHA256.new(message.encode())
        try:
            pkcs1_15.new(key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
