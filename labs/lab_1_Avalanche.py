import binascii # to convert binary to ASCII bytes
from hashlib import sha1

print(sha1(binascii.b2a_uu(b"11111111")).hexdigest())


# let's flip a single bit and see what happens

print(sha1(binascii.b2a_uu(b"11111011")).hexdigest())
