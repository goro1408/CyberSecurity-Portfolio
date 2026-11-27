# Network Scanner

A Python tool that finds live hosts on a local network using ARP requests.

## What it does

The scanner sends an ARP request to every address in a range. Hosts that are up
reply with their MAC address. The tool collects the replies and prints each
live host with its IP and MAC. It can also save the result to JSON.

ARP runs at layer 2. That means this scanner only sees hosts on the same local
segment as you. On a lab network you own, this is a fast and accurate way to map
what is online.

## What it shows

- Layer 2 host discovery with ARP.
- Use of scapy to craft and send raw packets.
- Clean CLI design with argparse and optional JSON export.

## Features

- Scan a full CIDR range, for example `192.168.1.0/24`.
- Adjustable reply timeout.
- Table output in the terminal.
- Optional JSON export for later use.

## Install

```sh
pip install -r requirements.txt
```

## Usage

ARP scanning needs raw socket access, so run it with sudo.

```sh
sudo python3 scanner.py 192.168.1.0/24
sudo python3 scanner.py 192.168.1.0/24 --timeout 2 --output results.json
```

## Sample output

```
IP Address        MAC Address
----------------------------------------
192.168.1.1       a4:2b:8c:11:22:33
192.168.1.10      de:ad:be:ef:00:11
192.168.1.24      00:1a:2b:3c:4d:5e

3 host(s) up.
```

## Notes and limits

- Works only on the local segment. It will not cross routers.
- Needs root or admin rights for raw packets.

## Authorized use only

Scan only networks you own or are allowed to test.
