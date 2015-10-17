def parseCommand(cmd):
    if len(cmd) != 3:
        raise InvalidCommandException(cmd)
    head = ord(cmd[0])
    param = ord(cmd[1])
    suffix = ord(cmd[2])  # always = 0x55
    if suffix != 0x55:
        raise InvalidCommandException(cmd)
    return Command(head, param, suffix)


class Command(object):
    def __init__(self, head, param, suffix):
        self.head = head
        self.param = param
        self.suffix = suffix

    def __repr__(self):
        return "{0:=#04x} {1:=#04x} {2:=#04x}".format(self.head, self.param, self.suffix)


class InvalidCommandException(Exception):
    pass
