import hashlib
from hashlib import md5

HASH_SECRET = "bgvyzdsv"
md5 = hashlib.md5()

x = 1
while True:
    hash = md5.update(str(x).encode("ASCII"))
    if hash:
        pass

print(hash)
