import socket
import sys
import threading
from threading import Thread
import time

#class Server:
#    def __init__(self):
# Przechowuja wazne dane jak np adresy klientow
clients = []
threads = []
data = ""


# funkcja  do oblsugi wielu klientow (kazdy to osobny watek)
def on_new_client(clientsocket,addr):
    while True:
        data = connection.recv(16)
        print(sys.stderr, 'received "%s"' % data)
        clientsocket.sendto(data, addr)
        #clientsocket.send(msg)
        time.sleep(5)
        break
    clientsocket.close()


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(3)

for i in range(3):
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    clients.append(client_address)

    thread = threading.Thread(target=on_new_client(connection, client_address))
    threads.append(thread)
    thread.start()

#for t in threads:
 #   t.join()

print(clients)
print(data)

'''
    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'received "%s"' % data)
            if data:
                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()
    '''