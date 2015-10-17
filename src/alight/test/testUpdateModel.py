import unittest
from alight.state import Zones
from alight.commands import Group1OnCommand, Group2OnCommand, Group3OnCommand, Group4OnCommand


class TestUpdateModel(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.model = Zones()

    def testTurnZoneOn(self):
        cmd = Group1OnCommand()
        self.model.handleCommand(cmd)

        self.assertTrue(self.model.zones[1].on)
        self.assertEqual(1, self.model.activeZone)

        cmd = Group2OnCommand()
        self.model.handleCommand(cmd)

        self.assertTrue(self.model.zones[2].on)
        self.assertEqual(2, self.model.activeZone)

        cmd = Group3OnCommand()
        self.model.handleCommand(cmd)

        self.assertTrue(self.model.zones[3].on)
        self.assertEqual(3, self.model.activeZone)

        cmd = Group4OnCommand()
        self.model.handleCommand(cmd)

        self.assertTrue(self.model.zones[4].on)
        self.assertEqual(4, self.model.activeZone)
