from scapy.all import IP, ICMP, traceroute
def traceroute(ip):
    print(ip)
    icmp = ICMP()
    a, uns = traceroute(target=ip,l4=icmp, verbose=0)
    archivo = open("traceroute.txt","w")
    archivo.write(a.show())
    archivo.close()
    