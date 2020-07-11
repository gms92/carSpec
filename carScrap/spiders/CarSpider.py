import scrapy
import os
import keys


class CarSpider(scrapy.Spider):
    name = 'CarSpider'
    
    start_urls = ['file:///home/volanty/Documentos/carrosnaweb/fichadetalhe/fichadetalhe.1441.html']

    # .format(c) for c in range(1,5)

    def parse(self, response):
        
        carTitle = response.xpath("//tr/td/font[@size='4']/text()").extract_first()
        carRawLink = response.xpath("//tr/td[@bgcolor='#efefef']/a/font[@size='2']/text()")[0:2].extract()
        carRawLink2 = response.xpath("//tr/td[@bgcolor='#efefef']/font[@size='2']/a/font/text()")[:3].extract()
        carRawLink3 = response.xpath("//tr/td[@bgcolor='#efefef']/font[@size='2']/a/text()")[0:2].extract()
        carRaw = response.xpath("//tr/td[@bgcolor='#efefef']/font[@size='2']/text()")[:11].extract()

        carHeaderRawValues = []
        carHeaderRawValues.append(carTitle)

        for c in carRawLink:
            carHeaderRawValues.append(c)
        
        for c in carRawLink3:
            carHeaderRawValues.append(c)

        for c in carRaw:
            carHeaderRawValues.append(c)
        
        for c in carRawLink2:
            carHeaderRawValues.append(c)

        # carFilter = carRaw[0,4]
        # car_year_and_price = carRawLink[0:2]
        # car_fuel = carRawLink3[0]
        # car_ipva_origin = carRaw[1:4]
        # car_config = carRawLink2[0]
        # car_body_size_capacity_and_doors = carRaw[4:7]
        # car_CNW = carRaw[7:9]

        yield{'values':carHeaderRawValues}
        # carKeys = response.xpath("//tr/td[@align='right']/font[@size='2']/text()").extract()
        # carValues = response.xpath("//tr/td[@bgcolor='#efefef']/font[@size='2']/text()").extract()
        # carRaw = response.xpath("//tbody/tr/td/table/tbody/tr/td").extract()
        
        # carHeader = []
        # carHeader.append(carTitle)

        # for c in car_year_and_price:
        #     carHeader.append(c)

        # carHeader.append(car_fuel)

        # for c in car_ipva_origin:
        #     carHeader.append(c)

        # carHeader.append(car_config)

        # for c in car_body_size_capacity_and_doors:
        #     carHeader.append(c)

        # for c in car_CNW:
        #     carHeader.append(c)


        # 1 - car title
