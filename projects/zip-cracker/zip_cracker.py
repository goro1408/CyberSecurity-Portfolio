import zipfile
from itertools import product
import string

def crack_zip(zip_file, max_length):
    characters = string.ascii_letters + string.digits
    zip_ref = zipfile.ZipFile(zip_file, 'r')

    for length in range(1, max_length + 1):
        for password in product(characters, repeat=length):
            password = ''.join(password)
            try:
                zip_ref.extractall(pwd=password.encode())
                print(f"Password found: {password}")
                return password
            except:
                continue
    print("Password not found")
    return None

if __name__ == "__main__":
    zip_file = input("Enter the path to the ZIP file: ")
    max_length = int(input("Enter the maximum password length to try: "))
    crack_zip(zip_file, max_length)

