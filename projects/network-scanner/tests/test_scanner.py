import unittest
from unittest.mock import patch
from projects.network_scanner.scanner import scan_network

class TestNetworkScanner(unittest.TestCase):

    @patch('projects.network_scanner.scanner.srp')
    def test_scan_network(self, mock_srp):
        mock_srp.return_value = [([], [])]  # Mock empty response
        devices = scan_network("192.168.1.1/32")
        self.assertIsInstance(devices, list)
        self.assertGreaterEqual(len(devices), 0)

if __name__ == '__main__':
    unittest.main()

