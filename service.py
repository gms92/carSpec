import pprint

def stringSeparate(string):
    
    splited = string.split()

    if "R$" in splited:
        splitedList = []

        if len(splited)==3:
            splitedList.extend((splited[0],int(splited[1].replace('.','')),splited[2]))

        elif len(splited)==5:
            unitSplited = splited[2]+" "+splited[3]+" "+splited[4]
            splitedList.extend((splited[0],int(splited[1].replace('.','')),unitSplited))

        else:
            splitedList.extend((splited[0],int(splited[1].replace('.',''))))

        return splitedList

    else:
        return string

def createCleanCarSpec(carSpecRaw,carName):
    carSpec = {
            'name':carName,
            'year':int(carSpecRaw['Ano']),
            'price':stringSeparate(carSpecRaw['Preço']),
            'fuel':carSpecRaw['Combustível'],
            'IPVA':stringSeparate(carSpecRaw['IPVA']),
            'insurance':stringSeparate(carSpecRaw['Seguro']),
            'check-up-price':stringSeparate(carSpecRaw['Revisões']),
            'origin':carSpecRaw['Procedência'],
            'guarantee':carSpecRaw['Garantia'],
            'configuration':carSpecRaw['Configuração'],
            'body-size':carSpecRaw['Porte'],
            'capacity':int(carSpecRaw['Lugares']),
            'doors':int(carSpecRaw['Portas']),
            'generation':int(carSpecRaw['Geração']),
            'index-CNW':float(carSpecRaw['Índice CNW'].replace(',','.')),
            'ranking-CNW':int(carSpecRaw['Ranking CNW']),

            # 'motor':{
            #     'installation':
            #     'aspiration':
            #     'layout':
            #     'power-supply':
            #     'cylinder':
            #     'valve-control':
            #     'valves-per-cylinder':
            #     'cylinder-diameter':
            #     'compression-ratio':
            #     'piston-stroke':
            #     'cubic-capacity':
            #     'max-power':
            #     'motor-code':
            #     'max-torque':
            #     'weight-power':
            #     'specific-torque':
            #     'weight-torque':
            #     'specific-power':


            # }
            }
    return carSpec




    # print(obj['IPVA'])
    # if "R$" in obj['IPVA']:
    #     obj_IPVA = obj['IPVA'].split()
    #     obj_IPVA_separado = []
    #     obj_IPVA_separado.extend((obj_IPVA[0],float(obj_IPVA[1])))
    #     obj['IPVA'] = obj_IPVA_separado
    
    # if "R$" in obj['Seguro']:
    #     obj_seguro = obj['Seguro'].split()
    #     obj_seguro_separado = []
    #     obj_seguro_separado.extend((obj_seguro[0],float(obj_seguro[1])))
    #     obj['Seguro'] = obj_seguro_separado

    # obj_garantia = obj['Garantia'].split()
    # obj_garantia_separado = []
    # obj_garantia_separado.extend((int(obj_garantia[0].replace(',','.')),obj_garantia[1]))
    # obj['Garantia'] = obj_garantia_separado

    # obj_aceleração = obj['Aceleração 0-100 km/h'].split()
    # obj_aceleração_separado = []
    # obj_aceleração_separado.extend((float(obj_aceleração[0].replace(',','.')),obj_aceleração[1]))
    # obj['Aceleração 0-100 km/h'] = obj_aceleração_separado

    

    # x = [int(obj_aceleração[0]) + " " + obj_aceleração[1]]

    # print(obj_IPVA_separado)

    # obj['Aceleração 0-100 km/h'] = float(obj_aceleração[0]) + obj_aceleração[1]
