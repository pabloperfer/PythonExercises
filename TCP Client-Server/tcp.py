import argparse, socket

"""
recvall function takes as arguments the socket number, and the length of message in number of bytes, to ensure
the total number of bytes of the segment was sent, it starts storing the received bytes in var more until
the length expected so data (the string of bytes) is returned
"""

def recvall(sock, length):
    data = b''   #empty bytes string
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:     # if bytes string is empty after receiving EOFError raised
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more     # Increasing length with the received message size
    return data

"""
The server will have a socket listening (sock and )
"""
def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # SO_REUSEADDR  Permits multiple AF_INET or AF_INET6 sockets to be bound to an identical socket address
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        print('Waiting for a new connection')    # new socket created for each message
        sc, sockname = sock.accept()  # creates a new connected socket, and returns a new file descriptor referring to that socket
        print('Connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        message = recvall(sc, 16)
        print('  message from client:', repr(message))
        sc.sendall(b'Goodbye, client!')   #sendall ensure all data is sent
        sc.close()       # file descriptor deleted
        print('  Closing socket')

def client(port):
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned the socket: ', sock.getsockname())
    sock.sendall(b'Greetings, server')
    reply = recvall(sock, 16)
    print('Server: ', repr(reply))
    sock.close()

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)