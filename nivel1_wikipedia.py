import requests
from lxml import html

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

url = "https://www.wikipedia.org/"
 
respuesta = requests.get(url, headers=encabezado)

parser = html.fromstring(respuesta.text)

# Extraccion de datos por python para todos los idiomas
# idiomas = parser.find_class('central-featured-lang')
# for idioma in idiomas:
#     print(idioma.text_content())

# Extraccion de datos mediante Xpath para todos los idiomas
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
for idiomas in idiomas:
    print(idiomas)

# Extraccion de datos mediante Xpath para solo el idioma ingles
# ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
# print(ingles)

# Extraccion de datos mediante python para solo el idioma ingles
# ingles = parser.get_element_by_id("js-link-box-en")
# print(ingles.text_content())

# Test de la primera versión
# print(respuesta.text)

