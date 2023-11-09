import argparse
import socket
import sys
import threading
import pandas as pd
import zipfile
def ports(a,ip):
    def Scan_hilos(Ip,port,puertos,estado):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((Ip, port))
            if result == 0:
                puertos.append(port)
                estado.append("Abierto")
            sock.close()
        except socket.error as error:
            sys.exit()
        return puertos,estado
    def Scan_ports_with_socket(IP,Ports):
        puertos = []
        estado = []
        for port in Ports:
            hilo = threading.Thread(target=Scan_hilos,args=(IP,port,puertos,estado))
            hilo.start()
        data = {
            "Puertos":puertos,
            "Estado":estado
        }
        df = pd.DataFrame(data)
        df.to_csv("./archivos/ports.csv",index=False)
        with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/ports.csv")
        return hilo
    try:
        if isinstance(a.split("-"),list):
            Rangeports = []
        for i in range(int(a.split("-")[0]),int(a.split("-")[1])+1,1):
            Rangeports.append(i)
    except:
        pass
    try:
        hilo = Scan_ports_with_socket(ip,Rangeports)
        return hilo
    except:
        pass