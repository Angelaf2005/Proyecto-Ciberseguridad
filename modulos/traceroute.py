from scapy.all import IP, ICMP, traceroute
import sys
import io

def trace(ip):
    icmp = ICMP()
    a, uns = traceroute(ip, l4=icmp, verbose=0)
    sys.stdout  = io.StringIO()
    a.show()
    archivo = open("./archivos/traceroute.txt","w")
    archivo.write(sys.stdout.getvalue())
    archivo.close()
    sys.stdout.close()
    a.graph(target=".7archivos/traceroute.svg")