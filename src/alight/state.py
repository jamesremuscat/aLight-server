from enum import Enum


class Mode(Enum):
    WHITE = 1
    RGB = 2


class Zone(object):

    def __init__(self, zoneID):
        self.zoneID = zoneID
        self.on = False
        self.whiteBrightness = 0
        self.colourBrightness = 0
        self.hue = 0
        self.mode = Mode.WHITE


class Zones(object):

    def __init__(self):
        self.zones = {1: Zone(1), 2: Zone(2), 3: Zone(3), 4: Zone(4)}
        self.activeZone = 0
