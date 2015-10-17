import logging
import socket
from threading import Thread


logger = logging.getLogger("Server")


class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 8899))

    def run(self):
        while True:
            data = self.socket.recv(64)  # buffer size is 64 bytes
            if data is not None:
                logger.debug("Received {0}".format(data))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    Server().start()
