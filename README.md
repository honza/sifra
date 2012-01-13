Sifra
=====

A wrapper around pycrypto RSA public key encryption. *Sifra* means *cipher* in
Czech.

```python

from sifra import Sifra

s = Sifra(public_key_path='id_rsa.pub', private_key_path='id_rsa', b64=True)

text = 'super secret text'

data = s.encrypt(text)
print s.decrypt(data)

s.encrypt_file('test')
s.decrypt_file('test')
```

For both the private and public keys, you can pass it in as a string or as a
path to the key. By default all encryption is base64 encoded.

License
-------

BSD, of course...
