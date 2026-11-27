# Cybersecurity Portfolio

Author: Orlando Del Valle Sanchez
Focus: offensive security and red team work
Location: Puerto Rico

This portfolio holds small security tools I built to learn by doing. Each tool
is written in Python. Each one shows a core concept I use in labs, CTFs, and
authorized testing: host discovery, port scanning, password analysis, and
password recovery.

The goal is simple. Show that I can read a problem, write clean code to solve
it, and explain how it works and when to use it.

## Skills shown here

- Network reconnaissance: ARP host discovery and TCP port scanning.
- Python for security: sockets, scapy, threading, regex, argparse.
- Secure coding habits: input handling, timeouts, clear error paths.
- Documentation: each tool has its own README, usage, and sample output.
- Safe lab practice: every tool carries an authorized use notice.

## Projects

| Project | What it does | Key tech |
|---|---|---|
| [Network Scanner](projects/network-scanner) | Finds live hosts on a local network with ARP. | scapy, argparse |
| [Port Scanner](projects/port-scanner) | Checks which TCP ports are open on a host. | sockets, threading |
| [Password Strength Checker](projects/password-checker) | Rates a password and gives feedback. | regex |
| [ZIP Password Recovery](projects/zip-cracker) | Recovers a lost ZIP password by brute force or wordlist. | zipfile, itertools |

## Quick start

Each project is self contained. Go into its folder and read the README.

```sh
git clone https://github.com/goro1408/CyberSecurity-Portfolio.git
cd CyberSecurity-Portfolio/projects/port-scanner
pip install -r requirements.txt
python3 port_scanner.py --help
```

Python 3.8 or newer is recommended.

## Authorized use only

These tools are for learning, CTFs, and systems you own or have written
permission to test. Scanning or attacking hosts, networks, or files without
consent is illegal in most places. Use them only in an authorized lab or
engagement.

## About me

I am Orlando. I work in IT and cybersecurity and I am building toward offensive
security and red team work. I learn best by building tools, breaking lab
targets, and writing down what I find. I speak English and Spanish.

## Contact

- [LinkedIn](https://www.linkedin.com/in/orlando-del-valle-sanchez-499434314/)
- [Twitter / X](https://x.com/G0R026)
- [Email](mailto:goro.1408@gmail.com)

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
