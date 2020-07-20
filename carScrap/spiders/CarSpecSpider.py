import scrapy
import os
import pprint
from transformer import createCleanCarSpec
from mongo import saveToMongo
from carScrap.extractor import CarSpecExtractor


class CarSpecSpider(scrapy.Spider):
    name = 'CarSpecSpider'

    start_urls = ['file:///home/volanty/Documentos/carrosnaweb/fichadetalhe/fichadetalhe.{}.html'.format(c) for c in range(1,5)]
    

    def parse(self, response):
        
        urls = response.request.url

        splitedUrls = urls.split('.')

        carId = splitedUrls[1]

        keyRaw=[]
        valueRaw=[]

        carName = response.xpath("//tr/td/font[@size='4']/text()").extract_first()
        
        for items in response.xpath("//tr"):
            keyRaw.append(items.xpath("./td[@align='right']/font[@size='2']/descendant::text()").getall())
            valueRaw.append(items.xpath("./td[@bgcolor='#efefef']/descendant::text()").getall())

        
        extractor = CarSpecExtractor.CarSpecExtractor()

        keys = extractor.cleanEmptyLists(keyRaw)

        values = extractor.cleanEmptyLists(valueRaw)
        
        keysFilter = extractor.replaceRepeatedKeys(keys)

        valuesFilter = extractor.cleanRawValues(values)

        extractor.transformKeys(keysFilter)

        

        carSpecRaw = {k:v for l1,l2 in zip(keysFilter,valuesFilter) for k,v in zip(l1,l2)}

        carSpecRaw = {k.strip(): v for (k, v) in carSpecRaw.items()}

        extractor.checkDoubleFields(carSpecRaw)

       
         # pprint.pprint(carSpecRaw)

        carSpec = createCleanCarSpec(carSpecRaw,carName,carId)

        pprint.pprint(carSpec)

        # saveToMongo(carSpec)






        