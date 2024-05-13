import hashlib
mystring = 'Python is fun!'
print('Your string is:', mystring)
myhash = hashlib.sha256(mystring.encode())
print('Your SHA256 hash is:', myhash.hexdigest())


