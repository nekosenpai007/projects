import sys
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def ping_sweep(network, netmask):
    live_hosts = []
    total_hosts = 0
    scanned_hosts = 0

    ip_network = IPNetwork(network + '/' + netmask)
    total_hosts = ip_network.size - 2  # exclude network & broadcast

    print(f"{Fore.CYAN}[*] Starting Ping Sweep on {network}/{netmask}")
    for host in ip_network.iter_hosts():
        scanned_hosts += 1
        print(f"{Fore.YELLOW}Scanning: {scanned_hosts}/{total_hosts} {host}", end="\r")
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is not None:
            live_hosts.append(str(host))
            print(f"{Fore.GREEN}Host {host} is online.                ")
    
    return live_hosts

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <network> <netmask>")
        print(f"Example: python {sys.argv[0]} 192.168.1.0 24")
        sys.exit(1)

    network = sys.argv[1]
    netmask = sys.argv[2]

    live_hosts = ping_sweep(network, netmask)
    
    print("\n" + Fore.CYAN + "[*] Scan Completed")
    if live_hosts:
        print(Fore.GREEN + "Live hosts:")
        for host in live_hosts:
            print(Fore.GREEN + f"- {host}")
    else:
        print(Fore.RED + "No live hosts found.")
