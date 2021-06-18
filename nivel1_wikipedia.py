import requests
from lxml import html

encabezado = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

url = "https://www.wikipedia.org/"
 
respuesta = requests.get(url, headers=encabezado)

parser = html.fromstring(respuesta.text)

ingles = parser.get_element_by_id("js-link-box-en")

print(ingles.text_content())

# print(respuesta.text)

