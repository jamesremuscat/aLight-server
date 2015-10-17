def parseCommand(cmd):
    if len(cmd) != 3:
        raise InvalidCommandException(cmd)
    head = ord(cmd[0])
    param = ord(cmd[1])
    suffix = ord(cmd[2])  # always = 0x55
    if suffix != 0x55:
        raise InvalidCommandException(cmd)

    knownCommand = __commands.get(head)
    if knownCommand:
        if param > 0:
            return knownCommand(param)
        else:
            return knownCommand()
    else:
        return Command(head, param)


class Command(object):
    def __init__(self, head, param, group=0):
        self.head = head
        self.param = param
        self.group = group

    def __repr__(self):
        return "{0:=#04x} {1:=#04x} {2:=#04x} ({3})".format(self.head, self.param, 0x55, self.__class__.__name__)


class AllOffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x41, 0x0)


class AllOnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x42, 0x0)


class Group1OnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x45, 0x0, 1)


class Group1OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x46, 0x0, 1)


class Group2OnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x45, 0x0, 2)


class Group2OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x46, 0x0, 2)


class Group3OnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x45, 0x0, 3)


class Group3OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x46, 0x0, 3)


class Group4OnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x45, 0x0, 4)


class Group4OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x46, 0x0, 4)


class BrightnessCommand(Command):
    def __init__(self, brightnessHex):
        Command.__init__(self, 0x4E, brightnessHex, None)


class HueCommand(Command):
    def __init__(self, hueHex):
        Command.__init__(self, 0x40, hueHex, None)


class InvalidCommandException(Exception):
    pass

__commands = {
    0x40: HueCommand,
    0x41: AllOffCommand,
    0x42: AllOnCommand,
    0x45: Group1OnCommand,
    0x46: Group1OffCommand,
    0x47: Group2OnCommand,
    0x48: Group2OffCommand,
    0x49: Group3OnCommand,
    0x4A: Group3OffCommand,
    0x4B: Group4OnCommand,
    0x4C: Group4OffCommand,
    0x4E: BrightnessCommand
}
