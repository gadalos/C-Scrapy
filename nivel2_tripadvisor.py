from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

# Abstracion de datos que se va a extraer de la pagina
class Hotel(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()
    amenities = Field()
# Clase Core - Spider generalmente se nombra de la pagina a la que se le va a ser el Scrapy
class TripAdvisor(CrawlSpider):
    name = "Hoteles"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    start_urls = ['https://www.tripadvisor.com/']
