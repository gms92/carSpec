import pprint

def stringSeparateInt(string):

    splited = string.split()
    splitedList = []

    for a in splited:

        if a[0].isdigit():
            a = int(a.replace(".", ""))
            splitedList.append(a)

        # elif isinstance(a[0],str):
        #     return string

        else:
            splitedList.append(a)
    
    return splitedList



def stringSeparateFloat(string):

    splited = string.split()
    splitedList = []

    for a in splited:

        if a[0].isdigit():
            a = float(a.replace(",", "."))
            splitedList.append(a)

        else:
            splitedList.append(a)
    
    return splitedList

def separateVolume(string):

    splited = string.split()
    splitedList = []

    splitedList.append(int(splited[0]))
    splitedList.append("cm")
    splitedList.append(3)

    return splitedList

def separateArea(string):

    splited = string.split()
    splitedList = []

    splitedList.append(int(splited[0]))
    splitedList.append("cm")
    splitedList.append(2)

    return splitedList

def separateCompressionRatio(string):

    splited = string.split(":")
    splitedList = []
    splitedList.extend((float(splited[0].replace(",", ".")), int(splited[1])))
    return splitedList


def createCleanCarSpec(carSpecRaw, carName):
    carSpec = {
        "name": carName,
        "year": int(carSpecRaw["Ano"]) if 'Ano' in carSpecRaw else None,
        "price": stringSeparateInt(carSpecRaw["Preço"]) if 'Preço' in carSpecRaw else None,
        "fuel": carSpecRaw["Combustível"] if 'Combustível' in carSpecRaw else None,
        "IPVA": stringSeparateInt(carSpecRaw["IPVA"]) if 'IPVA' in carSpecRaw else None,
        "insurance": stringSeparateInt(carSpecRaw["Seguro"]) if 'Seguro' in carSpecRaw else None,
        "check-up-price": stringSeparateInt(carSpecRaw["Revisões"]) if 'Revisões' in carSpecRaw else None,
        "origin": carSpecRaw["Procedência"] if 'Procedência' in carSpecRaw else None,
        "guarantee": stringSeparateInt(carSpecRaw["Garantia"]) if 'Garantia' in carSpecRaw else None,
        "configuration": carSpecRaw["Configuração"] if 'Configuração' in carSpecRaw else None,
        "body-size": carSpecRaw["Porte"] if 'Porte' in carSpecRaw else None,
        "capacity": int(carSpecRaw["Lugares"]) if 'Lugares' in carSpecRaw else None,
        "doors": int(carSpecRaw["Portas"]) if 'Portas' in carSpecRaw else None,
        "generation": int(carSpecRaw["Geração"]) if 'Geração' in carSpecRaw else None,
        "index-CNW": float(carSpecRaw["Índice CNW"].replace(",", ".")) if 'Índice CNW' in carSpecRaw else None,
        "ranking-CNW": int(carSpecRaw["Ranking CNW"]) if 'Ranking CNW' in carSpecRaw else None,

        "motor": {
            "installation": carSpecRaw["Instalação"] if 'Instalação' in carSpecRaw else None,
            "aspiration": carSpecRaw["Aspiração"] if 'Aspiração' in carSpecRaw else None,
            "layout": carSpecRaw["Disposição"] if 'Disposição' in carSpecRaw else None,
            "power-supply": carSpecRaw["Alimentação"] if 'Alimentação' in carSpecRaw else None,
            "cylinders": stringSeparateInt(carSpecRaw["Cilindros"]) if 'Cilindros' in carSpecRaw else None,
            "valve-control": carSpecRaw["Comando de válvulas"] if 'Comando de válvulas' in carSpecRaw else None,
            "valves-per-cylinder": int(carSpecRaw["Válvulas por cilindro"]) if 'Válvulas por cilindro' in carSpecRaw else None,
            "cylinder-diameter": stringSeparateFloat(carSpecRaw["Diâmetro dos cilindros"]) if 'Diâmetro dos cilindros' in carSpecRaw else None,
            "compression-ratio": separateCompressionRatio(carSpecRaw["Razão de compressão"]) if 'Razão de compressão' in carSpecRaw else None,
            "piston-stroke": stringSeparateFloat(carSpecRaw["Curso dos pistões"]) if 'Curso dos pistões' in carSpecRaw else None,
            "cubic-capacity": separateVolume(carSpecRaw['Cilindrada']) if 'Cilindrada' in carSpecRaw else None,
            "max-power": stringSeparateFloat(carSpecRaw['Potência máxima']) if 'Potência máxima' in carSpecRaw else None,
            "motor-code": carSpecRaw['Código do motor'] if 'Código do motor' in carSpecRaw else None,
            "max-torque": stringSeparateFloat(carSpecRaw['Torque máximo']) if 'Torque máximo' in carSpecRaw else None,
            "weight-power": stringSeparateFloat(carSpecRaw['Peso/potência']) if 'Peso/potência' in carSpecRaw else None,
            "specific-torque": stringSeparateFloat(carSpecRaw['Torque específico']) if 'Torque específico' in carSpecRaw else None,
            "weight-torque": stringSeparateFloat(carSpecRaw['Peso/torque']) if 'Peso/torque' in carSpecRaw else None ,
            "specific-power": stringSeparateFloat(carSpecRaw['Potência específica']) if 'Potência específica' in carSpecRaw else None
        },

        "transmission": {
            "traction": carSpecRaw['Tração'] if 'Tração' in carSpecRaw else None,
            "gear": carSpecRaw['Câmbio'] if 'Câmbio' in carSpecRaw else None, 
            "gear-code": carSpecRaw['Código do câmbio'] if 'Código do câmbio' in carSpecRaw else None,
            "coupling": carSpecRaw['Acoplamento'] if 'Acoplamento' in carSpecRaw else None,
        },

        "Suspension": {
            "front": carSpecRaw['Suspensão dianteira'] if 'Suspensão dianteira' in carSpecRaw else None,
            "front-elastic-element": carSpecRaw['Elemento elástico dianteiro'] if 'Elemento elástico dianteiro' in carSpecRaw else None,
            "back": carSpecRaw['Suspensão traseira'] if 'Suspensão traseira' in carSpecRaw else None,
            "back-elastic-element": carSpecRaw['Elemento elástico traseiro'] if 'Elemento elástico traseiro' in carSpecRaw else None,
        },

        "brakes": {
            "front": carSpecRaw['Freios dianteiros'] if 'Freios dianteiros' in carSpecRaw else None,
            "back": carSpecRaw['Freios traseiros'] if 'Freios traseiros' in carSpecRaw else None,
        },

        "direction": {
            "assistance": carSpecRaw['Assistência'] if 'Assistência' in carSpecRaw else None,
            "min-rotate-diameter": carSpecRaw['Diâmetro mínimo de giro'] if 'Diâmetro mínimo de giro' in carSpecRaw else None,
        },

        "tires": {
            "front": carSpecRaw['Pneus dianteiros'] if 'Pneus dianteiros' in carSpecRaw else None,
            "front-sidewall-height": stringSeparateFloat(carSpecRaw['Altura do flanco dianteiro']) if 'Altura do flanco dianteiro' in carSpecRaw else None,
            "back": carSpecRaw['Pneus traseiros'] if 'Pneus traseiros' in carSpecRaw else None,
            "back-sidewall-height": stringSeparateFloat(carSpecRaw['Altura do flanco traseiro']) if 'Altura do flanco traseiro' in carSpecRaw else None,
        },

        "dimensions": {
            "lenght": stringSeparateFloat(carSpecRaw['Comprimento']) if 'Comprimento' in carSpecRaw else None,
            "width": stringSeparateFloat(carSpecRaw['Largura']) if 'Largura' in carSpecRaw else None,
            "axes-distance": stringSeparateFloat(carSpecRaw['Distância entre-eixos']) if 'Distância entre-eixos' in carSpecRaw else None,
            "height": stringSeparateFloat(carSpecRaw['Altura']) if 'Altura' in carSpecRaw else None,
            "front-gauge": stringSeparateFloat(carSpecRaw['Bitola Dianteira']) if 'Bitola Dianteira' in carSpecRaw else None,
            "back-gauge": stringSeparateFloat(carSpecRaw['Bitola Traseira']) if 'Bitola Traseira' in carSpecRaw else None,
            "trunk-volume": stringSeparateFloat(carSpecRaw['Porta-malas']) if 'Porta-malas' in carSpecRaw else None,
            "fuel-tank": stringSeparateFloat(carSpecRaw['Tanque de combustível']) if 'Tanque de combustível' in carSpecRaw else None,
            "weight": stringSeparateFloat(carSpecRaw['Peso']) if 'Peso' in carSpecRaw else None,
            "payload": stringSeparateFloat(carSpecRaw['Carga útil']) if 'Carga útil' in carSpecRaw else None,
            "free-span-ground": stringSeparateFloat(carSpecRaw['Vão livre do solo']) if 'Vão livre do solo' in carSpecRaw else None,

        }
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

    # if "R$" in splited:

    #     if len(splited) == 3:
    #         splitedList.extend(
    #             (splited[0], int(splited[1].replace(".", "")), splited[2])
    #         )

    #     elif len(splited) == 5:
    #         unitSplited = splited[2] + " " + splited[3] + " " + splited[4]
    #         splitedList.extend(
    #             (splited[0], int(splited[1].replace(".", "")), unitSplited)
    #         )

    #     else:
    #         splitedList.extend((splited[0], int(splited[1].replace(".", ""))))

    #     return splitedList

    # elif int(splited[0]) > 0 or float(splited[0].replace(",", ".")) > 0:

    #     if len(splited) == 2:
    #         splitedList.extend((float(splited[0].replace(",", ".")), splited[1]))

    #     if len(splited)>4:
    #         for a in splited:
    #             # if float(a.replace(",", ".")) > 0:
    #             #     a = 'aff'
    #             #     # a = float(a.replace(",", "."))
    #             #     splitedList.append(a)
    #             # else:
    #                 splitedList.append(a)