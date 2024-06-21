import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the path to the scanner module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scanner import scan_network

class TestNetworkScanner(unittest.TestCase):

    @patch('scanner.srp')
    @patch('scanner.ARP')
    @patch('scanner.Ether')
    def test_scan_network(self, mock_Ether, mock_ARP, mock_srp):
        # Mock ARP and Ether to return mocked objects
        mock_ARP.return_value = MagicMock()
        mock_Ether.return_value = MagicMock()

        # Create a mock response for srp
        mock_sent = MagicMock()
        mock_received = MagicMock()
        mock_received.psrc = "192.168.1.1"
        mock_received.hwsrc = "00:11:22:33:44:55"
        mock_srp.return_value = [(mock_sent, mock_received)]  # Ensure this returns a tuple of two elements

        devices = scan_network("192.168.1.1/32")

        self.assertIsInstance(devices, list)
        self.assertGreaterEqual(len(devices), 2)
        self.assertEqual(devices[0]['ip'], "192.168.1.1")
        self.assertEqual(devices[0]['mac'], "00:11:22:33:44:55")

if __name__ == '__main__':
    unittest.main()

