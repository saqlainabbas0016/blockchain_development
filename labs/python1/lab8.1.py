import os
print("Current working directory:", os.getcwd())

with open('example.txt', 'w') as file:
    file.write("This is a test file.")

def process_file_in_blocks(filename, block_size=1024):
    with open(filename, 'rb') as file:
        while True:
            # Read the file in chunks of `block_size`
            block = file.read(block_size)
            
            # If no more data is read, exit the loop
            if not block:
                break
            
            # Process the block (for demonstration, we'll just print its length)
            print(f"Processed block of size: {len(block)} bytes")

# Example usage:
# filename = 'example.txt'

filename = 'c:\\Users\\Saqlain_abbas_313\\OneDrive\\Desktop\\BlockchainDevelopment\\labs\\python1\\example.txt'

# filename = '/Users/Saqlain_abbas_313/OneDrive/Desktop/python1/example.txt'

process_file_in_blocks(filename)


# filename = 'c:\\Users\\Saqlain_abbas_313\\OneDrive\\Desktop\\New folder\\labs\\python1\\example.txt'
