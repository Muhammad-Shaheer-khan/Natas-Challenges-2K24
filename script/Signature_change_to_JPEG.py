import binascii

# Change any file signature into JPEG signature

# Path to the PHP file you want to modify
file_path = r""

# JPEG file signature
jpeg_signature = binascii.unhexlify('FFD8FFDB')

# Read the original file content
with open(file_path, 'rb') as file:
    file_content = file.read()

# Open the file for writing
with open(file_path, 'wb') as file:
    # Write the JPEG signature at the beginning of the file
    file.write(jpeg_signature)
    # Append the rest of the original file content
    file.write(file_content)

print("File signature changed to JPEG.")
