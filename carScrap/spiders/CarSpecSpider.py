import scrapy
import os
import pprint
from service import createCleanCarSpec
from mongo import saveToMongo
from carScrap.extractor import CarSpecExtractor


class CarSpecSpider(scrapy.Spider):
    name = 'CarSpecSpider'

    start_urls = ['file:///home/volanty/Documentos/carrosnaweb/fichadetalhe/fichadetalhe.{}.html'.format(c) for c in range(1,5)]
    

    def parse(self, response):
        
        # web_urls = ['https://www.carrosnaweb.com.br/fichadetalhe.asp?codigo={}'.format(c) for c in range(1,10)]

        urls = response.request.url

        splitedUrls = urls.split('.')

        carId = splitedUrls[1]

        print(carId)
        
        keyRaw=[]
        valueRaw=[]

        carName = response.xpath("//tr/td/font[@size='4']/text()").extract_first()
        
        for items in response.xpath("//tr"):
            keyRaw.append(items.xpath("./td[@align='right']/font[@size='2']/descendant::text()").getall())
            valueRaw.append(items.xpath("./td[@bgcolor='#efefef']/descendant::text()").getall())

        keys = [x for x in keyRaw if x != []]
        values = [x for x in valueRaw if x != []]
        
        
        extractor = CarSpecExtractor.CarSpecExtractor()

        keysFilter = extractor.replaceRepeatedKeys(keys)

        valuesFilter = extractor.filterRawDataFromValues(values)

        
        keysFilter[-2] = ['Consumo urbano','Consumo rodoviario']
        keysFilter[-1] = ['Consumo urbano2','Consumo rodoviario2']

        keysFilter.append(['Autonomia urbana','Autonomia rodoviaria'])
        keysFilter.append(['Autonomia urbana2','Autonomia rodoviaria2'])

        # pprint.pprint(keysFilter)
        # pprint.pprint(valuesFilter)
        # print(carName)

        carSpecRaw = {k:v for l1,l2 in zip(keysFilter,valuesFilter) for k,v in zip(l1,l2)}

        carSpecRaw = {k.strip(): v for (k, v) in carSpecRaw.items()}

        if 'Autonomia urbana' not in carSpecRaw:
            carSpecRaw['Autonomia urbana'] = carSpecRaw.pop('Consumo urbano2')
            carSpecRaw['Autonomia rodoviaria'] = carSpecRaw.pop('Consumo rodoviario2')

        # pprint.pprint(values)
        # print('------------------------------------------------------------------')
        # pprint.pprint(valuesFilter)
        # pprint.pprint(keysFilter)
        
        
        # pprint.pprint(carSpecRaw)

        carSpec = createCleanCarSpec(carSpecRaw,carName,carId)

        pprint.pprint(carSpec)

        # saveToMongo(carSpec)






        