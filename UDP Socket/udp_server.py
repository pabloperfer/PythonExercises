"""
The client will send a line of text to the server.
The server will receive the data and convert each character to uppercase.
The server will send the uppercase characters to the client.
The client will receive and display them on its screen.
"""

import socket

MAX_SIZE_BYTES = 65535 # Maximum size of a UDP datagram

# we create a socket object for IPV4 and UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 3000
hostname = '127.0.0.1'

#bind socket to address
s.bind((hostname, port))

#getsockname() method on an object of the socket class to find the current IP address and port
print('Listening at {}'.format(s.getsockname())) # Printing the IP address and port of socket

#listening to clients. recvfrom accepts 65535 ensuring entirety of packet
while True:
    #Receive data from the socket.
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) # Receive at most 65535 bytes at once

    #decoding from bytes to ascii
    message = data.decode('ascii')
    #capitalizing the message received
    upperCaseMessage = message.upper()

    print('The client at {} says {!r}'.format(clientAddress, message))

    #encode  capitalized message
    data = upperCaseMessage.encode('ascii')

    #send back the number of bytes capitalized to client
    s.sendto(data, clientAddress)