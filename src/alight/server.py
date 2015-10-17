import socket
from threading import Thread


class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 8899))

    def run(self):
        while True:
            data, addr = self.socket.recvfrom(64)  # buffer size is 64 bytes
            if data is not None:
                print data, addr


if __name__ == "__main__":
    Server().start()
