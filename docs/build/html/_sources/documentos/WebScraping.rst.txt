Uso de Web Scraping
===================

Dentro de este proyecto utilizamos el web scraping con distintos fines entre ellos:

* Obtener correos
* Obtener Telefonos
* Obtener links

Correos y Telefonos
-------------------
Para obtener los correos y Telefonos con web Scraping tenemos el siguiente código

.. code-block:: python

  response = requests.get(dom)
  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      texto = soup.get_text()
      # Expresión regular para encontrar correos electrónicos
      correos = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' , texto)
      # Expresión regular para encontrar números de teléfono (varios formatos)
      numeros = re.findall(r'[\(]?[\+]?(\d{2})[\)]?[\s]?((\d{6})|(\d{2}[\*\.\-\s]){4}|(\d{4}[\*\.\-\s]){2})|\d{8}', texto)
      with open("./archivos/Reporte.txt", "w") as archivo:
          archivo.write("Correos electrónicos:\n")
          for correo in correos:
              archivo.write(correo + "\n")
          archivo.write("\nNúmeros de teléfono:\n")
          for numero in numeros:
              # Formatea el número de teléfono antes de escribirlo en el archivo
              formatted_number = "-".join(numero)
              archivo.write(formatted_number + "\n")

Un código sencillo En el cuál utilizamos expresiones regulares junto con BeautifulSoup y requests
para extraer todos los correos en la página, esto es importante, ya que nos ayuda a saber qué tanta
información es expuesta dentro de la página.

links
-----
Para obtener todos los links dentro de la página web utilizamos el siguiente código de python

.. code-block:: python

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            regex = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            match = re.search(regex, href)
            if match:
                links.append(match.group())
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Enlaces'
    for i, link in enumerate(links, 1):
        sheet.cell(row=i, column=1, value=link)
    workbook.save('./archivos/links.xlsx')
    with zipfile.ZipFile("./pass/archivos.zip","a") as archivo:
            archivo.write("./archivos/links.xlsx")

Este código se encarga de extraer los links de toda la página web con request y bs4, además utilizamos openpyxl
para guardar toda la información en un archivo xlsx y a su vez se gaurda dentro de un archivo zip.
