import socket

def start_server():
    s = socket.socket()
    print("Socket successfully created")

    port = 8080
    s.bind(('127.0.0.1', port))
    print(f"Socket binded to {port}")

    s.listen(5)
    print("Socket is listening")

    while True:
        c, address = s.accept()
        print("Got connection from:", address)

        c.send('Thank you for connecting'.encode())

        try:
            while True:
                # Receive a message from the client
                data = c.recv(1024).decode()
                if not data:
                    break  # Exit if the client has closed the connection
                
                print("Received message from client:", data)
                
                # Send a response back to the client
                send_message = input("Enter Message to send to client: ")
                c.send(send_message.encode())
                
        except KeyboardInterrupt:
            print("Server shutting down...")
            c.send("Connection ended!!!".encode())
            c.close()
            break

if __name__ == "__main__":
    start_server()
