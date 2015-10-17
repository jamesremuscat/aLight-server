def parseCommand(cmd):
    if len(cmd) != 3:
        raise InvalidCommandException(cmd)
    return Command(cmd)


class Command(object):
    def __init__(self, bytedata):
        self.bytedata = bytedata

    def __repr__(self):
        return "{0:=#04x} {1:=#04x} {2:=#04x}".format(ord(self.bytedata[0]), ord(self.bytedata[1]), ord(self.bytedata[2]))


class InvalidCommandException(Exception):
    pass
