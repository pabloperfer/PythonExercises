import socket

MAX_SIZE_BYTES = 65535 # Maximum size of a UDP datagram

# we create the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# we get the text to send and get capitalized in the udp server
message = input('Input lowercase sentence:' )
# we encode ascii to bytes
data = message.encode('ascii')

#sending to the udp server port
s.sendto(data, ('127.0.0.1', 3000))

print('The OS assigned the address {} to me'.format(s.getsockname()))
data, address = s.recvfrom(MAX_SIZE_BYTES)

text = data.decode('ascii')
print('The server {} replied with {!r}'.format(address, text))
