import lxml.html

# Abrir el archivo HTML
with open("/home/carlos/work/projects/python/pdf/templates/static/informe.html", "r") as f:
    html = f.read()

# Parsear el archivo HTML
doc = lxml.html.fromstring(html)

# Imprimir el archivo parseado
print(doc)

# Obtener la entrada al style dentro del header
style = doc.find("head")

# Obtener los valores de los atributos
color = style.attrib
print(doc.attrib)
# font_size = style.attrib["body"]

# Imprimir la entrada al style
print(f"color: {color}")
