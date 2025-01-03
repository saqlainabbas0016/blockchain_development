import hashlib
import bcrypt

# Define a string to hash
text = "Blockchain course-GB"

# Generate MD5 hash
md5_hash = hashlib.md5(text.encode()).hexdigest()
print("MD5 Hash:", md5_hash)

# Generate SHA-1 hash
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
print("SHA-1 Hash:", sha1_hash)

# Generate RIPEMD-160 hash
ripemd160_hash = hashlib.new('ripemd160', text.encode()).hexdigest()
print("RIPEMD-160 Hash:", ripemd160_hash)

# Generate bcrypt hash with a salt
salt = bcrypt.gensalt()
bcrypt_hash = bcrypt.hashpw(text.encode(), salt)
print("bcrypt Hash:", bcrypt_hash)

# Generate SHA-256 hash
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print("SHA-256 Hash:", sha256_hash)

# Generate SHA-512 hash
sha512_hash = hashlib.sha512(text.encode()).hexdigest()
print("SHA-512 Hash:", sha512_hash)

# Generate BLAKE2 hash
blake2_hash = hashlib.blake2b(text.encode()).hexdigest()
print("BLAKE2 Hash:", blake2_hash)

# Generate SHA-3 hash
sha3_hash = hashlib.sha3_256(text.encode()).hexdigest()
print("SHA-3 Hash:", sha3_hash)
