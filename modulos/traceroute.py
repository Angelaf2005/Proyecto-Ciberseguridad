from scapy.all import ICMP,traceroute, IP, TCP, UDP
import io,sys
import zipfile
def traceICMP(ip):
    try:
        icmp = ICMP()
        a, uns = traceroute(ip, l4=icmp, verbose=0)
        sys.stdout  = io.StringIO()
        a.show()
        archivo = open("./archivos/tracerouteICMP.txt","w")
        archivo.write(sys.stdout.getvalue())
        archivo.close()
        sys.stdout.close()
        a.graph(target="./archivos/tracerouteICMP.svg")
        with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/tracerouteICMP.txt")
            archivo.write("./archivos/tracerouteICMP.svg")
    except:
        pass
def traceTCP(ip):
    try:
        tcp = TCP()
        a,uns = traceroute(ip, l4=tcp,verbose = 0)
        sys.stdout = io.StringIO()
        a.show()
        archivo = open("./archivos/tracerouteTCP.txt","w")
        archivo.write(sys.stdout.getvalue())
        archivo.close()
        sys.stdout.close()
        a.graph(target="./archivos/tracerouteTCP.svg")
        with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/tracerouteTCP.txt")
            archivo.write("./archivos/tracerouteTCP.svg")
    except:
        pass

def traceUDP(ip):
    try:
        udp = UDP()
        a,uns = traceroute(ip, l4=udp,verbose = 0)
        sys.stdout = io.StringIO()
        a.show()
        archivo = open("./archivos/tracerouteUDP.txt","w")
        archivo.write(sys.stdout.getvalue())
        archivo.close()
        sys.stdout.close()
        a.graph(target="./archivos/tracerouteUDP.svg")
        with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/tracerouteUDP.txt")
            archivo.write("./archivos/tracerouteUDP.svg")
    except:
        pass