from scapy.all import ICMP,traceroute, IP, TCP, UDP
import io,sys

def traceICMP(ip):
    icmp = ICMP()
    a, uns = traceroute(ip, l4=icmp, verbose=0)
    sys.stdout  = io.StringIO()
    a.show()
    archivo = open("./archivos/tracerouteICMP.txt","w")
    archivo.write(sys.stdout.getvalue())
    archivo.close()
    sys.stdout.close()
    a.graph(target="./archivos/tracerouteICMP.svg")
def traceTCP(ip):
    tcp = TCP()
    a,uns = traceroute(ip, l4=tcp,verbose = 0)
    sys.stdout = io.StringIO()
    a.show()
    archivo = open("./archivos/tracerouteTCP.txt","w")
    archivo.write(sys.stdout.getvalue())
    archivo.close()
    sys.stdout.close()
    a.graph(target="./archivos/tracerouteTCP.svg")

def traceUDP(ip):
    udp = UDP()
    a,uns = traceroute(ip, l4=udp,verbose = 0)
    sys.stdout = io.StringIO()
    a.show()
    archivo = open("./archivos/tracerouteUDP.txt","w")
    archivo.write(sys.stdout.getvalue())
    archivo.close()
    sys.stdout.close()
    a.graph(target="./archivos/tracerouteUDP.svg")