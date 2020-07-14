import scrapy
import os
import pprint
from service import stringSeparate,createCleanCarSpec
# import pymongo

class Car2Spider(scrapy.Spider):
    name = 'Car2Spider'
    
    start_urls = ['file:///home/volanty/Documentos/carrosnaweb/fichadetalhe/fichadetalhe.1441.html']
    # .format(c) for c in range(15000,15010)]

    def parse(self, response):
        
        keyRaw=[]
        valueRaw=[]

        carName = response.xpath("//tr/td/font[@size='4']/text()").extract_first()
        
        for items in response.xpath("//tr"):
            keyRaw.append(items.xpath("./td[@align='right']/font[@size='2']/descendant::text()").getall())
            valueRaw.append(items.xpath("./td[@bgcolor='#efefef']/descendant::text()").getall())

        keys = [x for x in keyRaw if x != []]
        values = [x for x in valueRaw if x != []]
        
        keysFilter = []
        valuesFilter = []

        for c in keys:
            if c[0] == 'Dianteiros' and c[1] == 'Traseiros':
                c = ['Dianteiros-freios','Traseiros-freios']
                for a in c:
                    a.strip()
                    
            keysFilter.append(c)

        for c in values:
            c = [a for a in c if "\n" not in a]

            if len(c)>2:
                c = [a for a in c if a!="1"]
                c = [a for a in c if a!="2"]
                c = [a for a in c if a!="3"]

                for a in c:
                    if a==' kg/cv' or a==' kg/kgfm':
                        c[0]=c[0]+c[1]
                        c.pop(1)


                if len(c)>2:
                    c[-1]= c[-2]+" "+c[-1]
                    c.pop(-2)
                
            valuesFilter.append(c)


        # keysFilter[-2] = ['Urbano1','Rodoviario1']
        # keysFilter[-1] = ['Urbano2','Rodoviario2']

        # keysFilter.append(['Urbana1','Rodoviaria1'])
        # keysFilter.append(['Urbana2','Rodoviaria2'])

        keysFilter[-2] = ['Urbano-consumo','Rodoviario-consumo']
        keysFilter[-1] = ['Urbano-consumo2','Rodoviario-consumo2']

        keysFilter.append(['Urbana-autonomia','Rodoviaria-autonomia'])
        keysFilter.append(['Urbana-autonomia2','Rodoviaria-autonomia2'])

        # pprint.pprint(keysFilter)
        # pprint.pprint(valuesFilter)
        # print(carName)

        carSpecRaw = {k:v for l1,l2 in zip(keysFilter,valuesFilter) for k,v in zip(l1,l2)}

        carSpecRaw = {k.strip(): v for (k, v) in carSpecRaw.items()}

        if 'Urbana-autonomia' not in carSpecRaw:
            carSpecRaw['Urbana-autonomia'] = carSpecRaw.pop('Urbano-consumo2')
            carSpecRaw['Rodoviaria-autonomia'] = carSpecRaw.pop('Rodoviario-consumo2')

        # pprint.pprint(carSpecRaw)

        carSpec = createCleanCarSpec(carSpecRaw,carName)

        pprint.pprint(carSpec)


        