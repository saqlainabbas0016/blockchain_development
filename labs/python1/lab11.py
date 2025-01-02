from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def print_rsa_key_details(key):
    # Extract details from RSA key
    if isinstance(key, rsa.RSAPublicKey):
        print("Public Key Details:")
        print(f"  Key Size: {key.key_size} bits")
        numbers = key.public_numbers()
        print(f"  Public Exponent: {numbers.e}")
        print(f"  Modulus: {numbers.n}")
    elif isinstance(key, rsa.RSAPrivateKey):
        print("Private Key Details:")
        print(f"  Key Size: {key.key_size} bits")
        numbers = key.private_numbers()
        print(f"  Public Exponent: {numbers.public_exponent}")
        print(f"  Modulus: {numbers.public_numbers.n}")
        print(f"  Private Exponent: {numbers.d}")
        print(f"  Prime 1: {numbers.p}")
        print(f"  Prime 2: {numbers.q}")
        print(f"  Exponent 1: {numbers.dmp1}")
        print(f"  Exponent 2: {numbers.dmq1}")
        print(f"  Coefficient: {numbers.iqmp}")
    else:
        print("Unsupported key type")

def main():
    # Generate RSA keys for demonstration
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # Print RSA key details
    print_rsa_key_details(public_key)
    print()
    print_rsa_key_details(private_key)

    # Serialize keys to PEM format (optional, for viewing the actual key)
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    print("\nSerialized RSA Private Key (PEM):")
    print(private_key_pem.decode())
    print("\nSerialized RSA Public Key (PEM):")
    print(public_key_pem.decode())

if __name__ == "__main__":
    main()
