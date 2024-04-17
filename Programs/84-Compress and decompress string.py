import zlib

string = "hello world!hello world!hello world!hello world!"

# Compress the string
compressed_string = zlib.compress(string.encode())

# Decompress the string
decompressed_string = zlib.decompress(compressed_string).decode()

print("Original string: ", string)
print("Compressed string: ", compressed_string)
print("Decompressed string", decompressed_string)