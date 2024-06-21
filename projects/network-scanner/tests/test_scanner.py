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
        # Mock ARP and Ether
        mock_ARP.return_value = MagicMock()
        mock_Ether.return_value = MagicMock()
        
        # Mock srp to return a controlled output
        mock_srp.return_value = [(
            MagicMock(), 
            MagicMock(psrc="192.168.1.1", hwsrc="00:11:22:33:44:55")
        )]
        
        devices = scan_network("192.168.1.1/32")
        
        self.assertIsInstance(devices, list)
        self.assertGreaterEqual(len(devices), 1)
        self.assertEqual(devices[0]['ip'], "192.168.1.1")
        self.assertEqual(devices[0]['mac'], "00:11:22:33:44:55")

if __name__ == '__main__':
    unittest.main()

