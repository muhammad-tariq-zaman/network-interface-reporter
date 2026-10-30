import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import parse

SAMPLE = """Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo: 1000000    100    0    0    0     0          0         0  1000000    100    0    0    0     0       0          0
  eth0: 5000000    500    2    0    0     0          0         0  2000000    200    1    0    0     0       0          0
"""


class TestInterfaceReporter(unittest.TestCase):
    def test_parses_two_interfaces(self):
        self.assertEqual(len(parse(SAMPLE)), 2)

    def test_busiest_first(self):
        self.assertEqual(parse(SAMPLE)[0]["name"], "eth0")

    def test_errors_recorded(self):
        eth0 = parse(SAMPLE)[0]
        self.assertEqual((eth0["rx_errors"], eth0["tx_errors"]), (2, 1))
