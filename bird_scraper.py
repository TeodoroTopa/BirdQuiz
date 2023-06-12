import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
import pandas as pd
import numpy as np

class BirdSpider(scrapy.Spider):
    
    name = 'BirdSpider'

    custom_settings = {
        'USER_AGENT' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",

        'ITEM_PIPELINES' : {'scrapy.pipelines.images.ImagesPipeline': 1},
        'IMAGES_STORE' : 'bird_pics'
    }
    
    def start_requests(  self  ):
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            
            
    def parse(  self, response  ):
        bird_items = response.xpath("//div[@id='guide-taxa']//div[@class='col-xs-3']")
        img_url_list = []
        for birdblock in bird_items:
            species = birdblock.xpath("./h5/a/text()").extract()[0]
            img_url = birdblock.xpath("./a/img/@src").extract()[0]
            birddata.append((species, img_url))
            img_url_list.append(img_url)
    
        yield {
            'image_urls' : img_url_list
        }        


baseurl = "https://www.inaturalist.org/guides/1098?page="

urls=[]
for i in range(1, 6):
    urls.append(baseurl + str(i))

birddata=[]

process = CrawlerProcess()
process.crawl(BirdSpider)
process.start()

df = pd.DataFrame(birddata, columns= ['species', 'image_url'])
df.to_csv('bird_data.csv', index= False)
