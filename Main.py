import argparse
import re
import socket
from urllib.parse import urlparse
import whois
import builtwith
import nmap
import pandas as pd
#Funcion que busca que la url coincida con la expresión regular
def errorfromurl(a):
    #Esta expresión regular fue sacada de internet, dejo referencias al final
    regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    urls = re.findall(regex, a)
    if (len(urls) == 0):
        print("El formato no es el adecuado\nRevise la documentación con \"--help\"")
    return(urls[0])
#Encuentra la ip de una página web solamente con el hostname
def ipbyhostname(a):
    try:
        url = urlparse(a)
        ip = socket.gethostbyname(url.hostname)
    except:
        print("El hostname ingresado no es válido\nRevise la documentación con \"--help\"")
        exit()
    return ip

def domain_whois(a,b):
    try:
        web = whois.whois(a)
        archivo = open("domain_info.txt","w")
        archivo.write(web.text)
        archivo.close()
    except:
        try:
            web = whois.whois(b)
            archivo = open("domain_info.txt","w")
            archivo.write(web.text)
            archivo.close()
        except:
            pass
def info_built(a):
    try: 
        info = builtwith.parse(a)
        archivo = open("Builwith.txt","w")
        for x,y in info.items():
            archivo.write(x)
            for i in y:
                archivo.write(i)
            archivo.write("\n")    
        archivo.close()
    except:
        pass
def scan_port(a,ip):
    scanner = nmap.PortScanner()
    horas = list()
    hostname = list()
    estado1 = list()
    estado2 = list()
    nombre = list()
    puertos = list()
    try:
        b = a.split("-")
        for i in range(int(b[0]),int(b[1])+1,1):
            
            try:
                res = scanner.scan(ip,str(i),arguments="--host-timeout 30s")
                hora = res["nmap"]["scanstats"]["timestr"]
                puertos.append(i)
                if hora is None:
                    horas.append(" ")
                else:
                    horas.append(hora)
                host = res['scan'][ip]['hostnames'][0]['name']
                if host is None:
                    hostname.append(" ")
                else:
                    hostname.append(host)
                estados1 = res["scan"][ip]["status"]["state"]
                if estados1 is None:
                    estado1.append(" ")
                else:
                    estado1.append(estados1)
                estados2 = res["scan"][ip]["tcp"][i]["state"]
                if estados2 is None:
                    estado2.append(" ")
                else:
                    estado2.append(estados2)
                nombres = res['scan'][ip]['tcp'][i]['name']
                if nombres is None:
                    nombre.append(" ")
                else:
                    nombre.append(nombres)
                #horas = horas.append(res["nmap"]["scanstats"]["timestr"])
                #hostname = hostname.append(res["scan"][ip]["hostnames"][0]["name"])
                #estado1 = estado1.append(res["scan"][ip]["status"]["state"])
                #estado2 = estado2.append(res["scan"][ip]["tcp"][i]["state"])
                #nombre = nombre.append(res['scan'][ip]['tcp'][i]['name'])
            except Exception as e:
                print(e)
                continue
        data = {
            "Puertos":puertos,
            "Hora":horas,
            "Hostname":hostname,
            "Estatus":estado1,
            "Estado":estado2,
            "Nombre":nombre
            }
        df = pd.DataFrame(data)
        df.to_csv("ports.csv",index=False)
    except:
        pass
    return
if (__name__ == '__main__'):
    #Definición de argumentos de ArgsParse(En proceso)
    parser = argparse.ArgumentParser(prog="Programa con enfoque en la ciberseguridad",description="Programa con enfoque en ciberseguridad:\n-Webscraping\n-Escaneo\n-Buildwith",epilog="Fines educativos")
    parser.add_argument("-w","--webpage",type=str,required=True,help="Utiliza dominios e páginas webs\nEjemplo: -w https://www.google.com/ \n Nota: Debe incluir el prefijo https o http")
    parser.add_argument("-Rp","--Rangeports",type=str,required=False,help="Escanea un rango de puertos de la Ip en especifico\nSe utiliza de la siguiente forma -Rp 0-55",default="0-500")
    args = parser.parse_args()
    url = errorfromurl(args.webpage)
    ip = ipbyhostname(url)
    domain_whois(ip,url)
    info_built(url)
    scan_port(args.Rangeports,ip)
    





"""Referencias
https://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url
"""
#Realizado en Github por: Angelaf2005
"""Notas sobre Nmap:
Muy probablemente no funcione desde tu computador
para que lo haga tienes que realizar 2 cosas:
1) Descargar nmap desde su página web
2) Agregar la dirección de donde se instaló nmap a la variable de entorno Path desde cmd"""