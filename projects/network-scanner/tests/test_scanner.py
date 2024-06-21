import unittest
import sys
import os

# Add the path to the scanner module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scanner import scan_network

class TestNetworkScanner(unittest.TestCase):

    def test_scan_network(self):
        devices = scan_network("192.168.1.1/32")
        self.assertIsInstance(devices, list)
        self.assertGreaterEqual(len(devices), 0)

if __name__ == '__main__':
    unittest.main()

