import hashlib

def hash_concatenate(input1, input2):
    # Concatenate the inputs
    combined = input1 + input2
    
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the combined data encoded as bytes
    sha256.update(combined.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return sha256.hexdigest()

# Example usage:
input1 = "Hello"
input2 = "World"
hash_value = hash_concatenate(input1, input2)
print(f"Hash value: {hash_value}")






# def process_file_in_blocks(filename, block_size=1024):
#     with open(filename, 'rb') as file:
#         while True:
#             # Read the file in chunks of `block_size`
#             block = file.read(block_size)
            
#             # If no more data is read, exit the loop
#             if not block:
#                 break
            
#             # Process the block (for demonstration, we'll just print its length)
#             print(f"Processed block of size: {len(block)} bytes")

# # Example usage:
# filename = 'example.txt'
# process_file_in_blocks(filename)
