Parametros
==========
Vamos a explicar un poco sobre los parametros que utiliza nuestra herramienta.

* **-Ts --typescan** Esta función decide el tipo de escaneo que realizará donde **1** es nmap y **2** es por socket 
* **-w** Argumento requerido. Página web con la que actuará el programa Ejemplo: -w https://www.google.com/ Nota: Debe incluir el prefijo https o http.
* **-Rp** Rango de puertos que serán escaneados debe estar en el formato Ejemplo: "0-100" Nota: por defecto se escanearán los primeros 500 puertos.
* **-As** Uso de API de Shodan, es necesario tener una cuenta y una APIKEY válida introduzca -AS 2 si desea utilizar Shodan, no se usará Shodan por defecto.
* **-MM** Correo al que se enviarán los resultados. 