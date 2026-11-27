#!/usr/bin/env python3
"""Port Scanner.

Checks which TCP ports are open on a target host. It opens a TCP connection to
each port with a short timeout. If the connection succeeds, the port is open.

A thread pool runs many checks at once, so a full 1-1024 sweep finishes in
seconds instead of minutes.

Authorized use only. Scan only hosts you own or are allowed to test.

Usage:
    python3 port_scanner.py 192.168.1.10
    python3 port_scanner.py scanme.nmap.org --ports 1-1024 --timeout 0.5
    python3 port_scanner.py 10.0.0.5 --ports 22,80,443,8080
"""

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor

# Common ports mapped to a friendly service name for nicer output.
COMMON_SERVICES = {
    21: "ftp", 22: "ssh", 23: "telnet", 25: "smtp", 53: "dns",
    80: "http", 110: "pop3", 139: "netbios", 143: "imap", 443: "https",
    445: "smb", 3306: "mysql", 3389: "rdp", 5432: "postgres", 8080: "http-alt",
}


def scan_port(ip, port, timeout=1.0):
    """Return the port number if it is open, else None."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        if sock.connect_ex((ip, port)) == 0:
            return port
    return None


def scan_ports(ip, ports, timeout=1.0, workers=100):
    """Scan many ports concurrently and return the sorted list of open ones."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(lambda p: scan_port(ip, p, timeout), ports)
        for port in results:
            if port is not None:
                open_ports.append(port)
    return sorted(open_ports)


def parse_ports(spec):
    """Turn a port spec into a list of ints.

    Accepts a range like "1-1024" or a comma list like "22,80,443".
    """
    if "-" in spec:
        start, end = spec.split("-", 1)
        return list(range(int(start), int(end) + 1))
    return [int(p) for p in spec.split(",") if p.strip()]


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scan a host for open TCP ports."
    )
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument(
        "-p", "--ports", default="1-1024",
        help='Ports to scan. Range "1-1024" or list "22,80,443" (default: 1-1024)',
    )
    parser.add_argument(
        "-t", "--timeout", type=float, default=1.0,
        help="Per-port timeout in seconds (default: 1.0)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        raise SystemExit(f"Could not resolve host: {args.target}")

    ports = parse_ports(args.ports)
    print(f"Scanning {args.target} ({ip}) across {len(ports)} port(s)...\n")

    open_ports = scan_ports(ip, ports, timeout=args.timeout)

    if not open_ports:
        print("No open ports found.")
        return

    print(f"{'PORT':<8}{'STATE':<8}{'SERVICE'}")
    print("-" * 28)
    for port in open_ports:
        service = COMMON_SERVICES.get(port, "unknown")
        print(f"{port:<8}{'open':<8}{service}")
    print(f"\n{len(open_ports)} open port(s).")


if __name__ == "__main__":
    main()
