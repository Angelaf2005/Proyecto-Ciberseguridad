TraceRoute
==========
Dentro de este programa utilizamos un rastreo de ruta a través de 3 distintos métodos:

* ICMP
* TCP
* UDP

TraceRoute por ICMP
-------------------

A través del módulo de *scapy* pudimos realizar un traceroute con python que utilizara ICMP.

.. code-block:: python

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

Este código realiza un traceroute a través de ICMP y gráfica los resultados otorgandonos resultados faciles de comprender

.. figure:: ./Traceroute_ICMP.png

Este es un ejemplo de la capacidad que tiene la herramienta para realizar gráficos

TraceRoute por TCP
------------------

Este traceroute utiliza paquetes TCP para realizar el rastreo de la ruta.

.. code-block:: python

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

Este código nos realiza el rastreo por TCP y también permite el uso de gráficos. Este tipo de traceroute pueden ser útiles
en casos donde los paquetes ICMP y UDP sean bloqueados por firewalls.

TraceRoute por UDP
------------------

TraceRoute con envío de paquetes UDP para el rastreo de la red.

.. code-block:: python
    
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

Herramienta de diagnostico para la ruta de paquetes desde el host de origen al host destino.




