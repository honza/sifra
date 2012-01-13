from base64 import b64encode, b64decode
from Crypto import Random
from Crypto.PublicKey import RSA


class Sifra(object):

    def __init__(self, public_key_path=None, private_key_path=None,
            public_key_string=None, private_key_string=None, b64=True):

        if not public_key_string and not public_key_path:
            raise Exception('No public key')
            return

        if not private_key_string and not private_key_path:
            raise Exception('No private key')
            return

        if public_key_path:
            self.public_key = RSA.importKey(self.read_file(public_key_path))

        if public_key_string:
            self.public_key = RSA.importKey(public_key_string)

        if private_key_path:
            self.private_key = RSA.importKey(self.read_file(private_key_path))

        if private_key_string:
            self.private_key = RSA.importKey(private_key_string)

        self.b64 = b64

    def read_file(self, filename):
        f = open(filename)
        data = f.read()
        f.close()
        return data

    def write_file(self, data, filename):
        f = open(filename, 'w')
        f.write(data)
        f.close()

    def decrypt(self, data):
        if self.b64:
            data = b64decode(data)
        return self.private_key.decrypt(data)

    def encrypt(self, data):
        data = self.public_key.encrypt(data, Random.new().read)[0]
        if self.b64:
            data = b64encode(data)
        return data

    def encrypt_file(self, path):
        data = self.read_file(path)
        data = self.encrypt(data)
        self.write_file(data, path)

    def decrypt_file(self, path):
        data = self.read_file(path)
        data = self.decrypt(data)
        self.write_file(data, path)
