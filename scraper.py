import requests
from bs4 import BeautifulSoup
import json

url = 'https://bolsascc.guanajuato.gob.mx/index.php?usfmztXir8ems9ya5tbk2dSKwdPs1dvY3KSB'

# pedir el sitio
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# buscar la tabla
table = soup.find('table')

# extraer filas de la tabla
rows = []
for row in table.find_all('tr')[1:]:  # Omitir la primera fila de encabezados
    data = {}
    data["folio"] = row.find_all('td')[0].text.strip()
    data["dependencia"] = row.find_all('td')[1].text.strip()
    data["fecha_publicacion"] = row.find_all('td')[2].text.strip()
    data["fecha_limite"] = row.find_all('td')[3].text.strip()
    data["puesto"] = row.find_all('td')[4].text.strip().split('Nivel:')[0]
    data["nivel"] = row.find_all('td')[4].text.strip().split('Nivel:')[1]
    data["num_plazas"] = row.find_all('td')[5].text.strip()
    data["escolaridad"] = row.find_all('td')[6].text.strip()
    data["ciudad"] = row.find_all('td')[7].text.strip()
    data['url'] = row.find('a').attrs["href"] 
    # TODO: de esta `url` scrapear el botón que dice "Descargar PDF" y agregar data['pdf']

    # filtrar sólo los de sistemas
    escolaridad = data["escolaridad"].lower()
    if "sistemas" in escolaridad or "informática" in escolaridad:
        rows.append(data)

# Mostrar los resultados (json)
print(json.dumps(rows, indent=1, ensure_ascii=False))
