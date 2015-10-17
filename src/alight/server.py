import logging
import socket
from commands import parseCommand
from threading import Thread
from time import sleep


logger = logging.getLogger("Server")


class Server(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 8899))

    def run(self):
        while True:
            data = self.socket.recv(64)  # buffer size is 64 bytes
            if data is not None:
                cmd = parseCommand(data)
                logger.debug("Received {0}".format(cmd))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    Server().start()
    while True:
        sleep(1)
