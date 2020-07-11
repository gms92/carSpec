import scrapy
import os
import pprint

class Car2Spider(scrapy.Spider):
    name = 'Car2Spider'
    
    start_urls = ['file:///home/volanty/Documentos/carrosnaweb/fichadetalhe/fichadetalhe.1441.html']

    def parse(self, response):
        
        keyRaw=[]
        valueRaw=[]
        
        for items in response.xpath("//tr"):
            keyRaw.append(items.xpath("./td[@align='right']/font[@size='2']/descendant::text()").getall())
            valueRaw.append(items.xpath("./td[@bgcolor='#efefef']/descendant::text()").getall())

        key = [x for x in keyRaw if x != []]
        value = [x for x in valueRaw if x != []]

        valueFilter = []

        for c in value:
            c = [a for a in c if "\n" not in a]
            valueFilter.append(c)

        key[-2] = ['Urbano1','Rodoviario1']
        key[-1] = ['Urbano2','Rodoviario2']

        key.append(['Urbana1','Rodoviaria1'])
        key.append(['Urbana2','Rodoviaria2'])


        # pprint.pprint(valueFilter)
        

        lists1 = [ ['a','b'], ['c','d'], ['e','f'] ]
        lists2 = [ [1,2,9], [3,4], [5,6] ]

        dictionary = {k:v for l1,l2 in zip(lists1,lists2) for k,v in zip(l1,l2)}
        pprint.pprint(dictionary)  