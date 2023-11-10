Escaneo de puertos
==================

Dentro de esta herramienta utilizamos 2 tipos de Escaneos:

* Nmap
* Socket

En breve explicaremos un poco sobre cada uno de ellos.

Nmap
----

El escaneo con Nmap se realiza de la siguiente manera:

.. code-block:: python

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
            except Exception as e:
                logging.eror(e)
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
        with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/ports.csv")
    except:
        pass

Este escaneo utiliza nmpa para obtener toda la información de una IP en especifico y a su vez,
utiliza el modulo de pandas para la creación de un archivo csv que sirve como reporte sobre los puertos.

Para usar el código anterior se utiliza el parametro *-Ts 1*

Socket
------

Esta herramienta también realiza un escaneo de puertos con ayuda del módulo socket. Este tipo
de escaneo resulta mucho más rápido que Nmap, pero tiene limitación en la información que podemos recibir.

.. code-block:: python

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

Este escaneo es muy útil para escaneos rápidos de información. PAra utilizarlo en la herramineta se coloca el parametro *-Ts 2*

    
