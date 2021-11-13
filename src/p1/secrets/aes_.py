import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def format_key(key: str) -> bytes:
    key += '*' * 200
    return bytes(key, 'UTF-8')[:32]

gg = format_key('kadabra')


key = os.urandom(32)
iv = os.urandom(16)  # initialization vector

cipher = Cipher(algorithms.AES(format_key('kadabra')), modes.CBC(iv))

encryptor = cipher.encryptor()
ct = encryptor.update(b'a secret message') + encryptor.finalize()

decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ct) + decryptor.finalize()
print(decrypted_message)
