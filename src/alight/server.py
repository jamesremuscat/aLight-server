import logging
import socket
from commands import parseCommand
from threading import Thread
from time import sleep


class Server(Thread):
    logger = logging.getLogger("Server")

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 8899))
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    def run(self):
        while True:
            data = self.socket.recv(64)  # buffer size is 64 bytes
            if data is not None:
                cmd = parseCommand(data)
                self.logger.debug("Received {1} => {0}".format(cmd, data))
                for listener in self.listeners:
                    listener.handleCommand(cmd)


def byteArrayToString(byteArray):
    return ''.join(chr(b) for b in byteArray)


class Relay(object):
    logger = logging.getLogger("Relay")

    def __init__(self, destinationIP, destinationPort=8899):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.destinationIP = destinationIP
        self.destinationPort = destinationPort

    def handleCommand(self, command):
        string = byteArrayToString(command.getBytes())
        self.logger.debug("Relaying message {2} to {0}:{1}".format(self.destinationIP, self.destinationPort, string))
        self.socket.sendto(string, (self.destinationIP, self.destinationPort))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    s = Server()
    r = Relay("192.168.2.99")
    s.addListener(r)
    s.start()
    while True:
        sleep(1)
