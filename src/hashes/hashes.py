import hashlib

# bits string
key = b"str"
# another way for bit
my_string = 'This is a normal string'.encode()

# for i in range(10):
#     hashed = hashlib.sha256(key).hexdigest()
#     print(hashed)

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)