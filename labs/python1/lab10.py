from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def rsa_decrypt(private_key_pem, cipher_text):
    # Load the private key from PEM format
    private_key = serialization.load_pem_private_key(private_key_pem, password=None)

    # Decrypt the ciphertext
    decrypted_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_text.decode()

# Example usage
def main():
    # Generate RSA keys for demonstration
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Serialize keys to PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # Encrypt a sample plaintext message
    plain_text = "This is a secret message"
    cipher_text = rsa_encrypt(public_key_pem, plain_text)
    
    print("Ciphertext:")
    print(cipher_text)

    # Decrypt the ciphertext
    decrypted_text = rsa_decrypt(private_key_pem, cipher_text)
    
    print("Decrypted Text:")
    print(decrypted_text)

# Function to encrypt text, included for completeness
def rsa_encrypt(public_key_pem, plain_text):
    # Load the public key from PEM format
    public_key = serialization.load_pem_public_key(public_key_pem)

    # Encrypt the plaintext
    cipher_text = public_key.encrypt(
        plain_text.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher_text

if __name__ == "__main__":
    main()
