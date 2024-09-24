import socket

def start_client():
    s = socket.socket()
    port = 8080

    s.connect(('127.0.0.1', port))
    print(s.recv(1024).decode())  # Receive welcome message from server

    while True:
        try:
            send_message = input("Enter Message to send to server: ")
            s.send(send_message.encode())

            # Wait for a response from the server
            response = s.recv(1024).decode()
            print("Received from server:", response)
        except KeyboardInterrupt:
            s.send("Connection ended!!!".encode())
            s.close()
            break

if __name__ == "__main__":
    start_client()
