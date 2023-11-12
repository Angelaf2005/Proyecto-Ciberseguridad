Buildwith y Whois
=================

Dentro de esta herramienta utilizamos estos dos modulos para la extracción de información sobre el dominio.

Buildwith
---------

Con Buildwith utilizamos el siguiente código para extraer información.

.. code-block:: python
    
    def info_built(a):
    try: 
        info = builtwith.parse(a)
        archivo = open("./archivos/Builwith.txt","w")
        for x,y in info.items():
            archivo.write(x)
            for i in y:
                archivo.write(i)
            archivo.write("\n")    
        archivo.close()
        with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/Builwith.txt")
    except:
        pass

De esta manera guardamos los archivos tanto en un txt como dentro de un archivo zip.

Whois
-----

Utilizamos en esta herramineta el modulo de whois para extraer información sobre el dominio utilizado.

.. code-block:: python

    def domain_whois(a,b):
    try:
        web = whois.whois(a)
        archivo = open("./archivos/domain_info.txt","w")
        archivo.write(web.text)
        archivo.close()
        with zipfile.ZipFile("./pass/archivos.zip","w") as archivo:
            archivo.write("./archivos/domain_info.txt")
    except Exception as e:
        logging.error(e)
        try:
            web = whois.whois(b)
            archivo = open("./archivos/domain_info.txt","w")
            archivo.write(web.text)
            archivo.close()
            with zipfile.ZipFile("./pass/archivos.zip","w") as archivo:
                archivo.write("./archivos/domain_info.txt")
        except Exception as e:
            logging.error(e)
            pass

De esta manera guardamos la información recibida en archivo de texto y dentro de un archivo zip que es el que se mandará por correo.



