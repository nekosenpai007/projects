import sys
from scapy.all import ICMP, IP, sr1
from netaddr import IPNetwork

def ping_sweep(network, netmask):
    live_host = []
    total_host = 0
    scanned_host = 0

    ip_network = IPNetwork(network + '/' + netmask)
    for host in ip_network.iter_hosts():
        total_host += 1

    for host in ip_network.iter_hosts():
        scanned_host += 1
        print(f"Scanning: {scanned_host}/{total_host}", end="\r")
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is not None:
            live_host.append(str(host))
            print(f"Host {host} is online.")
        
        return live_hosts
    
if __name__ == "__main__":
    network = sys.argv[1]
    netmask = sys.argv[2]

    live_hosts = ping_sweep(network, netmask)
    print("Completed\n")
    print(f"Live hosts: {live_hosts}")



