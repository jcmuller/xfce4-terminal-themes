from unittest import TestCase

from xfce4_terminal_themes.configurator import Configurator

class TestConfigurator(TestCase):
    def setUp(self):
        self.c = Configurator()

    def testVersion(self):
        self.assertEqual(self.c.version(), '%(prog)s 0.1')
