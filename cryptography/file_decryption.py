from cryptography.fernet import Fernet
import os


def load_key(filename):
    filename, _ = os.path.splitext(filename)
    new_filename = filename + ".key"
    with open(new_filename, "rb") as file:
        return file.read()


def decrypt_file(filename, key):
    f = Fernet(key)

    encrypted_data = b''
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

    print("[+] Successfully Decrypted the file!")


if __name__ == "__main__":

    filename = input("[+] Enter the filename: ")
    key = load_key(filename)

    decrypt_file(filename, key)
