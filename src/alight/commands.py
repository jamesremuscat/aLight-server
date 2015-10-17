from state import ZoneConstants


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
    def __init__(self, head, param, group=ZoneConstants.ALL):
        self.head = head
        self.param = param
        self.group = group

    def getBytes(self):
        return [self.head, self.param, 0x55]

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
        Command.__init__(self, 0x47, 0x0, 2)


class Group2OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x48, 0x0, 2)


class Group3OnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x49, 0x0, 3)


class Group3OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x4A, 0x0, 3)


class Group4OnCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x4B, 0x0, 4)


class Group4OffCommand(Command):
    def __init__(self):
        Command.__init__(self, 0x4C, 0x0, 4)


class BrightnessCommand(Command):
    def __init__(self, brightnessHex):
        Command.__init__(self, 0x4E, brightnessHex, ZoneConstants.ACTIVE)


class HueCommand(Command):
    def __init__(self, hueHex):
        Command.__init__(self, 0x40, hueHex, ZoneConstants.ACTIVE)

    @staticmethod
    def fromHueValue(hue):
        miHue = int(round(((250 - hue) % 360) * 256 / 360))
        return HueCommand(miHue)


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
