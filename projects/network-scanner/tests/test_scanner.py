import unittest
from scanner import scan_network

class TestNetworkScanner(unittest.TestCase):

    def test_scan_network(self):
        devices = scan_network("192.168.1.1/32")
        self.assertIsInstance(devices, list)
        self.assertGreaterEqual(len(devices), 0)

if __name__ == '__main__':
    unittest.main()

