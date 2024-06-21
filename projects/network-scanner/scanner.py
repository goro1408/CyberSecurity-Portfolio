import csv
import json
import socket
from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def save_results_to_csv(devices, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["IP", "MAC", "Open Ports"])
        writer.writeheader()
        for device in devices:
            writer.writerow({"IP": device['ip'], "MAC": device['mac'], "Open Ports": ', '.join(map(str, device['open_ports']))})

def save_results_to_json(devices, filename):
    with open(filename, 'w') as file:
        json.dump(devices, file, indent=4)

if __name__ == "__main__":
    ip_range = input("Enter the IP range (e.g., 192.168.1.1/24): ")
    ports_to_scan = list(map(int, input("Enter the ports to scan (comma-separated, e.g., 22,80,443): ").split(',')))
    export_format = input("Enter the export format (csv or json): ").strip().lower()
    export_filename = input("Enter the export filename: ")

    devices = scan_network(ip_range)

    for device in devices:
        device['open_ports'] = scan_ports(device['ip'], ports_to_scan)

    print("Available devices in the network:")
    print("IP" + " "*18+"MAC" + " "*18+"Open Ports")
    for device in devices:
        print(f"{device['ip']:16}    {device['mac']:18}    {', '.join(map(str, device['open_ports']))}")

    if export_format == 'csv':
        save_results_to_csv(devices, export_filename)
    elif export_format == 'json':
        save_results_to_json(devices, export_filename)
    else:
        print("Unsupported export format. Results not saved.")

