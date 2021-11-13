import base64

key = 'kadabra'
key_b = bytes(key, 'UTF-8')
print(key_b)
key_b64 = base64.b64encode(key_b)
print(key_b64)
key_b1 = base64.b64decode(key_b64)
print(key_b1)
key1 = key_b1.decode('UTF-8')
print(key1)


