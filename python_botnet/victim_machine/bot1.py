import socket


if __name__ == "__main__":
    print("[+] Connecting with server...")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.43.235", 8085))
    run_bot = True
    while run_bot:
        communicate_bot = True
        while communicate_bot:
            msg = s.recv(1024)
            msg = msg.decode()
            print("Command center said: ", msg)
            if msg == "exit":
                communicate_bot = False

        ans = "connected"
        if ans == "no":
            status = "disconnected"
            s.send(status.encode())
            run_bot = False
        else:
            status = "connected".encode()
            s.send(status)
    s.close()
