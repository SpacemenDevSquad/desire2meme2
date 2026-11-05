from cryptography.fernet import Fernet
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

class Hasher:
    def __init__(self, pepper_key: bytes):
        self.pepper = Fernet(pepper_key)
        self.pwd_hash = PasswordHash((Argon2Hasher(),))

    def hash(self, password: str) -> bytes:
        hash: str = self.pwd_hash.hash(password)

        hash_bytes: bytes = hash.encode('utf-8')
        peppered_hash: bytes = self.pepper.encrypt(hash_bytes)
        return peppered_hash

    def check(self, password: str, peppered_hash: bytes) -> bool:
        hash_bytes: bytes = self.pepper.decrypt(peppered_hash)
        hash: str = hash_bytes.decode('utf-8')
        return self.pwd_hash.verify(password, hash)

    @staticmethod
    def random_pepper() -> bytes:
        return Fernet.generate_key()