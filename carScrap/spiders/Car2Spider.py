import scrapy
import os
import pprint

class Car2Spider(scrapy.Spider):
    name = 'Car2Spider'
    
    start_urls = ['file:///home/volanty/Documentos/carrosnaweb/fichadetalhe/fichadetalhe.12300.html']

    def parse(self, response):
        
        keyRaw=[]
        valueRaw=[]
        
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
            keysFilter.append(c)

        for c in values:
            c = [a for a in c if "\n" not in a]

            if len(c)>2:
                c = [a for a in c if a!="1"]
                c = [a for a in c if a!="2"]
                c = [a for a in c if a!="3"]

                if len(c)>2:
                    c[-1]= c[-2]+" "+c[-1]
                    c.pop(-2)
                
            valuesFilter.append(c)


        # keysFilter[-2] = ['Urbano1','Rodoviario1']
        # keysFilter[-1] = ['Urbano2','Rodoviario2']

        # keysFilter.append(['Urbana1','Rodoviaria1'])
        # keysFilter.append(['Urbana2','Rodoviaria2'])

        keys[-2] = ['Urbano1','Rodoviario1']
        keys[-1] = ['Urbano2','Rodoviario2']

        keys.append(['Urbana1','Rodoviaria1'])
        keys.append(['Urbana2','Rodoviaria2'])

        # pprint.pprint(keysFilter)
        # pprint.pprint(valuesFilter)

        dictionary = {k:v for l1,l2 in zip(keysFilter,valuesFilter) for k,v in zip(l1,l2)}

        pprint.pprint(dictionary)

        # lists1 = [ ['a','b'], ['c','d'], ['e','f'],['h'],['x'] ]
        # lists2 = [ [1,2,9], [3,4], [5,6] ,[3],[10] ]

        # dictionary = {k:v for l1,l2 in zip(lists1,lists2) for k,v in zip(l1,l2)}
        # pprint(dictionary)  