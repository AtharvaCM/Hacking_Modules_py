from cryptography.fernet import Fernet


if __name__ == "__main__":
    key = Fernet.generate_key()
    print(key)

    # encoding strings

    message = "This is my secret msg"

    msg_binary = message.encode()

    f = Fernet(key)

    encrypted_msg = f.encrypt(msg_binary)
    print(encrypted_msg)

    decrypted_msg = f.decrypt(encrypted_msg)
    print(decrypted_msg)
