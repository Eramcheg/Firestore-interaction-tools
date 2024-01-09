import hashlib

def hash_text(text, hash_algorithm='sha1'):
    # Create a hash object using the specified algorithm
    if hash_algorithm == 'md5':
        hash_object = hashlib.md5()
    elif hash_algorithm == 'sha1':
        hash_object = hashlib.sha1()
    elif hash_algorithm == 'sha256':
        hash_object = hashlib.sha256()
    else:
        raise ValueError("Unsupported hash algorithm")

    # Update the hash object with the bytes of the text
    hash_object.update(text.encode('utf-8'))

    # Get the hash value as a hexadecimal string
    hash_string = hash_object.hexdigest()

    return hash_string

text = "Hello, world!"
hash_value = hash_text(text)
print("MD5 Hash:", hash_value)
