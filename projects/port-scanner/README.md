# Port Scanner

A fast Python tool that finds open TCP ports on a target host.

## What it does

The scanner tries to open a TCP connection to each port you ask for. If the
connection succeeds, the port is open. It uses a thread pool to run many checks
at once, so a full 1-1024 sweep takes seconds. Known ports are labeled with
their common service name.

This is a TCP connect scan. It completes the full handshake, so it is simple and
accurate, but it is also easy for the target to log.

## What it shows

- TCP connect scanning with raw sockets.
- Concurrency with a thread pool for speed.
- Hostname resolution and flexible port input.
- Service name mapping for readable output.

## Features

- Scan a port range or a custom list.
- Resolve hostnames, not just IPs.
- Adjustable per-port timeout.
- Clean, aligned results with service names.

## Install

No external dependencies. Python 3.8 or newer.

## Usage

```sh
python3 port_scanner.py 192.168.1.10
python3 port_scanner.py scanme.nmap.org --ports 1-1024 --timeout 0.5
python3 port_scanner.py 10.0.0.5 --ports 22,80,443,8080
```

## Sample output

```
Scanning scanme.nmap.org (45.33.32.156) across 1024 port(s)...

PORT    STATE   SERVICE
----------------------------
22      open    ssh
80      open    http

2 open port(s).
```

## Notes and limits

- TCP only. It does not scan UDP.
- A connect scan is visible in target logs. Use only where you are authorized.

## Authorized use only

Scan only hosts you own or have written permission to test.
