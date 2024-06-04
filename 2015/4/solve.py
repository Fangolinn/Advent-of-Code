from hashlib import md5

HASH_SECRET = "bgvyzdsv"

x = 1
while True:
    if md5((HASH_SECRET + str(x)).encode()).hexdigest().startswith("000000"):
        break
    x += 1

print(x)
