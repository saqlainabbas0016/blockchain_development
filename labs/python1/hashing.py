import bcryptt


# Hash a password
def hash_password(password: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Verify a password  
def verify_password(stored_hash: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))

# Example usage
if __name__ == "__main__":
    password = input("Enter a password : ")
    hashed_password = hash_password(password)
    print("Hashed password:", hashed_password)

    # Verification
    check_password = input("Enter the password to verify: ")
    if verify_password(hashed_password, check_password):
        print("Password matches!")
    else:
        print("Password does not match.")

#    SHA-256
import hashlib

def generate_sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

if __name__ == "__main__":
    data = "Hello, World!"
    hash_value = generate_sha256_hash(data)
    print(f"SHA-256 Hash: {hash_value}")


text_file_name = "my_text_file.txt"
with open( text_file_name, "w") as f:
    f.write("this is sample text file")

original_hash = calculate_sha256(text_file_text)
print(" original sha-256 hash:" , original_hash)

