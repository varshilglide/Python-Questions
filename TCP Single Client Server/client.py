import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

while True:

    # Send data to the server
    message = input('Enter message to send to the server: ')

    ## using sock.sendall method we can sends entire buffer.
    sock.sendall(message.encode())

    #Encode() method encodes the string, using the specified encoding If no encoding is specified, UTF-8 will be used.
    # Receive data from the server
    data = sock.recv(1024).decode()
    print('received from server:', data)

    if message.lower() == "bye":
        break

# Clean up the connection

sock.close()

