import requests
from bs4 import BeautifulSoup
import re

def obtener_correos_y_numeros(dom):
    response = requests.get(dom)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        texto = soup.get_text()

        # Expresión regular para encontrar correos electrónicos
        correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' , texto)

        # Expresión regular para encontrar números de teléfono (varios formatos)
        numeros = re.findall(r'[\(]?[\+]?(\d{2})[\)]?[\s]?((\d{6})|(\d{2}[\*\.\-\s]){4}|(\d{4}[\*\.\-\s]){2})|\d{8}', texto)

        return correos, numeros

    else:
        print("Error al obtener la página:", response.status_code)
        return [], []
 
dom = "https://www.fime.uanl.mx/contacto/"

correos, numeros = obtener_correos_y_numeros(dom)

with open("Reporte.txt", "w") as archivo:
    archivo.write("Correos electrónicos:\n")
    for correo in correos:
        archivo.write(correo + "\n")
    
    archivo.write("\nNúmeros de teléfono:\n")
    for numero in numeros:
        # Formatea el número de teléfono antes de escribirlo en el archivo
        formatted_number = "-".join(numero)
        archivo.write(formatted_number + "\n")

print("La información se guarda en Reporte.txt")