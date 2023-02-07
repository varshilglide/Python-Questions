import socket

# Create a TCP/IP socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# here I made a socket instance and passed it two parameters.
# AF_INET refers to the address family ipv4.
# Sock_Stream means connection-oriented TCP Protocol.


# Bind the socket to the port
# sock.bind('localhost', 10000)
#bind method which binds to a specific IP and port so that it can listen to incoming request on that IP and Port.

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')

    connection, client_address = sock.accept()

    try:

        print('connection from', client_address)
        while True:

            # Receive the data from the client

            data = connection.recv(1024).decode()

            if data.lower() == "bye":
                break
            if data:

                print('received from client:', data)

                # Send the message to the client

                message = input("Enter message to send to the client: ")

                connection.sendall(message.encode())

            else:

                print('no data from', client_address)

                break



    finally:

        # Clean up the connection
        connection.close()





