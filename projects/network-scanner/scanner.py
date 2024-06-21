from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Create ARP request packet
    arp_request = ARP(pdst=ip_range)
    # Create Ethernet frame
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and the ARP request packet
    packet = ether_frame / arp_request

    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Process the response and extract the IP and MAC addresses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

