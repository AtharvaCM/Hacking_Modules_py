from cryptography.fernet import Fernet
import os


def write_key(filename, key):
    filename, _ = os.path.splitext(filename)
    new_filename = filename + ".key"
    with open(new_filename, "wb") as file:
        file.write(key)


def load_key(filename, key):
    filename, _ = os.path.splitext(filename)
    new_filename = filename + ".key"
    with open(new_filename, "rb") as file:
        return file.read()


def encrypt_file(filename, key):
    f = Fernet(key)
    enceypted = b''  # empty var
    with open(filename, "rb") as file:
        data = file.read()  # loads file contents into this var
        encrypted = f.encrypt(data)

    with open(filename, "wb") as file:
        file.write(encrypted)
        print("[+] Successfully Encrypted the file!")


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
    key = Fernet.generate_key()

    filename = input("[+] Enter the filename: ")
    # write key onto disk
    write_key(filename, key)
    encrypt_file(filename, key)
