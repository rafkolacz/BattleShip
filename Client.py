import socket
import sys


# klasa klient umozliwiajaca stworzenie 2 graczy
class Client:
    def __init__(self):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print(sys.stderr, 'connecting to %s port %s' % server_address)
        self.sock.connect(server_address)

    # funkcja sluzaca do wyslania wiadomosci (np pole w ktore statek strzela)
    def sendmsg(self, text):
        try:

            # Send data
            message = text.encode()
            print(sys.stderr, 'sending "%s"' % message)
            self.sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            # czeka na odpowiedz (bez tego nie pojdzie dalej)
            # mozna zakomentowac
            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print(sys.stderr, 'received "%s"' % data)
        except:
            pass

    # funkcja do zamykania polaczenia po skonczonej grze
    def kill(self):
            print(sys.stderr, 'closing socket')
            self.sock.close()

