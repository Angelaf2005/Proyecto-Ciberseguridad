from scapy.all import IP, ICMP, traceroute
def traceroute(ip):
    print(ip)
    icmp = ICMP()
    a, uns = traceroute(target=ip,14=icmp, verbose=0)
    a.show()