# from cryptography.hazmat.primitives.asymmetric import rsa, dsa
# from cryptography.hazmat.primitives import serialization, hashes
# from cryptography.hazmat.primitives.asymmetric import padding
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives import serialization

# # Function to generate RSA keys and encrypt/decrypt message
# def rsa_operations(message):
#     # Generate RSA keys
#     private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
#     public_key = private_key.public_key()

#     # Serialize keys
#     private_pem = private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.TraditionalOpenSSL,
#         encryption_algorithm=serialization.NoEncryption()
#     )
#     public_pem = public_key.public_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PublicFormat.SubjectPublicKeyInfo
#     )

#     print("RSA Private Key:")
#     print(private_pem.decode())
#     print("RSA Public Key:")
#     print(public_pem.decode())

#     # Encrypt message
#     encrypted_message = public_key.encrypt(
#         message.encode(),
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )

#     # Decrypt message
#     decrypted_message = private_key.decrypt(
#         encrypted_message,
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )

#     print("Encrypted Message:")
#     print(encrypted_message)
#     print("Decrypted Message:")
#     print(decrypted_message.decode())

# # Function to generate DSA keys, sign and verify message
# def dsa_operations(message):
#     # Generate DSA keys
#     private_key = dsa.generate_private_key(key_size=2048)
#     public_key = private_key.public_key()

#     # Serialize keys
#     private_pem = private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.TraditionalOpenSSL,
#         encryption_algorithm=serialization.NoEncryption()
#     )
#     public_pem = public_key.public_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PublicFormat.SubjectPublicKeyInfo
#     )

#     print("DSA Private Key:")
#     print(private_pem.decode())
#     print("DSA Public Key:")
#     print(public_pem.decode())

#     # Sign message
#     signature = private_key.sign(
#         message.encode(),
#         hashes.SHA256()
#     )

#     # Verify signature
#     try:
#         public_key.verify(
#             signature,
#             message.encode(),
#             hashes.SHA256()
#         )
#         print("Signature is valid.")
#     except Exception as e:
#         print("Signature is invalid:", str(e))

#     print("Signature:")
#     print(signature)

# # Main function to run RSA and DSA operations
# def main():
#     message = "This is a secret message"
    
#     print("RSA Operations:")
#     rsa_operations(message)
    
#     print("\nDSA Operations:")
#     dsa_operations(message)

# if __name__ == "__main__":
#     main()



# _________________________________________|   
                #  Answer3 
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

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

# Example usage
def main():
    # Generate RSA keys for demonstration
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Serialize the public key to PEM format
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # Plaintext message to be encrypted
    plain_text = "This is a secret message"

    # Encrypt the plaintext
    cipher_text = rsa_encrypt(public_key_pem, plain_text)
    
    print("Encrypted Ciphertext:")
    print(cipher_text)

if __name__ == "__main__":
    main()               
