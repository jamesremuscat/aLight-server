from enum import Enum


class Mode(Enum):
    WHITE = 1
    RGB = 2


class Zone(object):

    def __init__(self, zoneID):
        self.id = zoneID
        self.on = False
        self.whiteBrightness = 0
        self.colourBrightness = 0
        self.hue = 0
        self.mode = Mode.WHITE


class Zones(object):
    def __init__(self):
        self.zones = {1: Zone(1), 2: Zone(2), 3: Zone(3), 4: Zone(4)}
        self.activeZone = None

    def handleCommand(self, cmd):
        if cmd.group == ZoneConstants.ALL:
            pass
        elif cmd.group == ZoneConstants.ACTIVE:
            if self.activeZone is not None:
                cmd.applyTo(self.zones[self.activeZone])
        else:
            cmd.applyTo(self.zones[cmd.group])
            self.activeZone = cmd.group


class ZoneConstants(Enum):
    ALL = 0
    ACTIVE = -1
