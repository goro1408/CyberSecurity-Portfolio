#!/usr/bin/env python3
"""Network Scanner.

Discovers live hosts on a local network using ARP requests. It sends an ARP
request to every address in a range and lists the IP and MAC address of each
host that replies.

ARP works at layer 2, so this only sees hosts on the same local segment. It is
fast and reliable for a lab network you own.

Authorized use only. Run this against networks you own or are allowed to test.

Usage:
    sudo python3 scanner.py 192.168.1.0/24
    sudo python3 scanner.py 192.168.1.0/24 --timeout 2 --output results.json
"""

import argparse
import json
import sys

try:
    from scapy.all import ARP, Ether, srp
except ImportError:
    sys.exit("scapy is required. Install it with: pip install -r requirements.txt")


def scan_network(ip_range, timeout=3):
    """Send ARP requests across ip_range and return the hosts that reply.

    Args:
        ip_range: Target range in CIDR form, for example "192.168.1.0/24".
        timeout: Seconds to wait for replies.

    Returns:
        A list of dicts, each with keys "ip" and "mac".
    """
    arp_request = ARP(pdst=ip_range)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame / arp_request

    answered = srp(packet, timeout=timeout, verbose=0)[0]

    devices = []
    for _sent, received in answered:
        devices.append({"ip": received.psrc, "mac": received.hwsrc})
    return devices


def print_table(devices):
    """Print discovered hosts as a simple aligned table."""
    if not devices:
        print("No hosts replied.")
        return
    print(f"{'IP Address':<18}{'MAC Address'}")
    print("-" * 40)
    for device in devices:
        print(f"{device['ip']:<18}{device['mac']}")
    print(f"\n{len(devices)} host(s) up.")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Discover live hosts on a local network with ARP."
    )
    parser.add_argument(
        "target", help="Target range in CIDR form, e.g. 192.168.1.0/24"
    )
    parser.add_argument(
        "-t", "--timeout", type=int, default=3,
        help="Seconds to wait for replies (default: 3)",
    )
    parser.add_argument(
        "-o", "--output",
        help="Write results to a JSON file as well as printing them",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    devices = scan_network(args.target, timeout=args.timeout)
    print_table(devices)

    if args.output:
        with open(args.output, "w") as handle:
            json.dump(devices, handle, indent=2)
        print(f"Results written to {args.output}")


if __name__ == "__main__":
    main()
