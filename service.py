import pprint

def stringSeparateInt(string):

    splited = string.split()
    splitedList = []

    for a in splited:

        if a[0].isdigit():
            a = int(a.replace(".", ""))
            splitedList.append(a)

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

    splitedList.append(float(splited[0].replace(',','.')))
    splitedList.append(splited[1])
    splitedList.append(3)

    return splitedList


def separateCheckUp(string):

    splited = string.split()
    splitedList = []

    if splited[0]=="R$":
        for a in splited:
            if a[0].isdigit():
                a = int(a.replace(".", ""))
                splitedList.append(a)
            else:
                splitedList.append(a)

        return splitedList

    else:
        return string


def separateArea(string):

    splited = string.split()
    splitedList = []

    splitedList.append(float(splited[0].replace(',','.')))
    splitedList.append(splited[1])
    splitedList.append(2)

    return splitedList

def separateCompressionRatio(string):

    splited = string.split(":")
    splitedList = []
    splitedList.extend((float(splited[0].replace(",", ".")), int(splited[1])))
    return splitedList

def separateFuelUse(carSpecRaw,option):

    if option == 'urban':

        splited = stringSeparateFloat(carSpecRaw['Consumo urbano'])
        splitedList = []

        if 'Consumo urbano2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Consumo urbano2'])
            splitedList.extend((splited,splited_2))
            return splitedList
        
        else:
            return splited
        
    elif option == 'road':

        splited = stringSeparateFloat(carSpecRaw['Consumo rodoviario'])
        splitedList = []

        if 'Consumo rodoviario2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Consumo rodoviario2'])
            splitedList.extend((splited,splited_2))
            return splitedList
        
        else:
            return splited


def separateDrivingRange(carSpecRaw,option):

    if option == 'urban':

        splited = stringSeparateFloat(carSpecRaw['Autonomia urbana'])
        splitedList = []

        if 'Autonomia urbana2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Autonomia urbana2'])
            splitedList.extend((splited,splited_2))
            return splitedList
        
        else:
            return splited
        
    elif option == 'road':

        splited = stringSeparateFloat(carSpecRaw['Autonomia rodoviaria'])
        splitedList = []

        if 'Autonomia rodoviaria2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Autonomia rodoviaria2'])
            splitedList.extend((splited,splited_2))
            return splitedList
        
        else:
            return splited
        
        
def createCleanCarSpec(carSpecRaw, carName,carId):
    carSpec = {
        "name": carName,
        "brand": 
        "year": int(carSpecRaw["Ano"]) if 'Ano' in carSpecRaw else None,
        "price": stringSeparateInt(carSpecRaw["Preço"]) if 'Preço' in carSpecRaw else None,
        "fuel": carSpecRaw["Combustível"] if 'Combustível' in carSpecRaw else None,
        "IPVA": stringSeparateInt(carSpecRaw["IPVA"]) if 'IPVA' in carSpecRaw else None,
        "insurance": stringSeparateInt(carSpecRaw["Seguro"]) if 'Seguro' in carSpecRaw else None,
        "checkUpPrice": separateCheckUp(carSpecRaw["Revisões"]) if 'Revisões' in carSpecRaw else None,
        "origin": carSpecRaw["Procedência"] if 'Procedência' in carSpecRaw else None,
        "guarantee": stringSeparateInt(carSpecRaw["Garantia"]) if 'Garantia' in carSpecRaw else None,
        "configuration": carSpecRaw["Configuração"] if 'Configuração' in carSpecRaw else None,
        "bodySize": carSpecRaw["Porte"] if 'Porte' in carSpecRaw else None,
        "capacity": int(carSpecRaw["Lugares"]) if 'Lugares' in carSpecRaw else None,
        "doors": int(carSpecRaw["Portas"]) if 'Portas' in carSpecRaw else None,
        "generation": int(carSpecRaw["Geração"]) if 'Geração' in carSpecRaw else None,
        "platform": carSpecRaw["Plataforma"] if 'Plataforma' in carSpecRaw else None,
        "indexCNW": float(carSpecRaw["Índice CNW"].replace(",", ".")) if 'Índice CNW' in carSpecRaw else None,
        "rankingCNW": int(carSpecRaw["Ranking CNW"]) if 'Ranking CNW' in carSpecRaw else None,

        "engine": {
            "installation": carSpecRaw["Instalação"] if 'Instalação' in carSpecRaw else None,
            "aspiration": carSpecRaw["Aspiração"] if 'Aspiração' in carSpecRaw else None,
            "layout": carSpecRaw["Disposição"] if 'Disposição' in carSpecRaw else None,
            "powerSupply": carSpecRaw["Alimentação"] if 'Alimentação' in carSpecRaw else None,
            "cylinders": stringSeparateInt(carSpecRaw["Cilindros"]) if 'Cilindros' in carSpecRaw else None,
            "valveControl": carSpecRaw["Comando de válvulas"] if 'Comando de válvulas' in carSpecRaw else None,
            "valvesPerCylinder": int(carSpecRaw["Válvulas por cilindro"]) if 'Válvulas por cilindro' in carSpecRaw else None,
            "cylinderDiameter": stringSeparateFloat(carSpecRaw["Diâmetro dos cilindros"]) if 'Diâmetro dos cilindros' in carSpecRaw else None,
            "compressionRatio": separateCompressionRatio(carSpecRaw["Razão de compressão"]) if 'Razão de compressão' in carSpecRaw else None,
            "pistonStroke": stringSeparateFloat(carSpecRaw["Curso dos pistões"]) if 'Curso dos pistões' in carSpecRaw else None,
            "cubicCapacity": separateVolume(carSpecRaw['Cilindrada']) if 'Cilindrada' in carSpecRaw else None,
            "maxPower": stringSeparateFloat(carSpecRaw['Potência máxima']) if 'Potência máxima' in carSpecRaw else None,
            "motorCode": carSpecRaw['Código do motor'] if 'Código do motor' in carSpecRaw else None,
            "maxTorque": stringSeparateFloat(carSpecRaw['Torque máximo']) if 'Torque máximo' in carSpecRaw else None,
            "weightPower": stringSeparateFloat(carSpecRaw['Peso/potência']) if 'Peso/potência' in carSpecRaw else None,
            "specificTorque": stringSeparateFloat(carSpecRaw['Torque específico']) if 'Torque específico' in carSpecRaw else None,
            "weightTorque": stringSeparateFloat(carSpecRaw['Peso/torque']) if 'Peso/torque' in carSpecRaw else None ,
            "specificPower": stringSeparateFloat(carSpecRaw['Potência específica']) if 'Potência específica' in carSpecRaw else None
        },

        "transmission": {
            "traction": carSpecRaw['Tração'] if 'Tração' in carSpecRaw else None,
            "gear": carSpecRaw['Câmbio'] if 'Câmbio' in carSpecRaw else None, 
            "gearCode": carSpecRaw['Código do câmbio'] if 'Código do câmbio' in carSpecRaw else None,
            "coupling": carSpecRaw['Acoplamento'] if 'Acoplamento' in carSpecRaw else None,
        },

        "suspension": {
            "front": carSpecRaw['Suspensão dianteira'] if 'Suspensão dianteira' in carSpecRaw else None,
            "frontElasticElement": carSpecRaw['Elemento elástico dianteiro'] if 'Elemento elástico dianteiro' in carSpecRaw else None,
            "back": carSpecRaw['Suspensão traseira'] if 'Suspensão traseira' in carSpecRaw else None,
            "backElasticElement": carSpecRaw['Elemento elástico traseiro'] if 'Elemento elástico traseiro' in carSpecRaw else None,
        },

        "brakes": {
            "front": carSpecRaw['Freios dianteiros'] if 'Freios dianteiros' in carSpecRaw else None,
            "back": carSpecRaw['Freios traseiros'] if 'Freios traseiros' in carSpecRaw else None,
        },

        "steering": {
            "assistance": carSpecRaw['Assistência'] if 'Assistência' in carSpecRaw else None,
            "minRotateDiameter": carSpecRaw['Diâmetro mínimo de giro'] if 'Diâmetro mínimo de giro' in carSpecRaw else None,
        },

        "tires": {
            "front": carSpecRaw['Pneus dianteiros'] if 'Pneus dianteiros' in carSpecRaw else None,
            "frontSidewallHeight": stringSeparateFloat(carSpecRaw['Altura do flanco dianteiro']) if 'Altura do flanco dianteiro' in carSpecRaw else None,
            "back": carSpecRaw['Pneus traseiros'] if 'Pneus traseiros' in carSpecRaw else None,
            "backSidewallHeight": stringSeparateFloat(carSpecRaw['Altura do flanco traseiro']) if 'Altura do flanco traseiro' in carSpecRaw else None,
        },

        "dimensions": {
            "lenght": stringSeparateFloat(carSpecRaw['Comprimento']) if 'Comprimento' in carSpecRaw else None,
            "width": stringSeparateFloat(carSpecRaw['Largura']) if 'Largura' in carSpecRaw else None,
            "axesDistance": stringSeparateFloat(carSpecRaw['Distância entre-eixos']) if 'Distância entre-eixos' in carSpecRaw else None,
            "height": stringSeparateFloat(carSpecRaw['Altura']) if 'Altura' in carSpecRaw else None,
            "frontGauge": stringSeparateFloat(carSpecRaw['Bitola Dianteira']) if 'Bitola Dianteira' in carSpecRaw else None,
            "backGauge": stringSeparateFloat(carSpecRaw['Bitola Traseira']) if 'Bitola Traseira' in carSpecRaw else None,
            "trunkVolume": stringSeparateFloat(carSpecRaw['Porta-malas']) if 'Porta-malas' in carSpecRaw else None,
            "fuelTank": stringSeparateFloat(carSpecRaw['Tanque de combustível']) if 'Tanque de combustível' in carSpecRaw else None,
            "weight": stringSeparateFloat(carSpecRaw['Peso']) if 'Peso' in carSpecRaw else None,
            "payload": stringSeparateFloat(carSpecRaw['Carga útil']) if 'Carga útil' in carSpecRaw else None,
            "freeSpanGround": stringSeparateFloat(carSpecRaw['Vão livre do solo']) if 'Vão livre do solo' in carSpecRaw else None,

        },

        "aerodynamics": {
            "frontArea": separateArea(carSpecRaw['Área frontal (A)']) if 'Área frontal (A)' in carSpecRaw else None,
            "dragCoefficient": stringSeparateFloat(carSpecRaw['Coeficiente de arrasto (Cx)']) if 'Coeficiente de arrasto (Cx)' in carSpecRaw else None,
            "frontAreaCorrected": separateArea(carSpecRaw['Área frontal corrigida']) if 'Área frontal corrigida' in carSpecRaw else None,
        },

        "performance": {
            "maxSpeed": stringSeparateFloat(carSpecRaw['Velocidade máxima']) if 'Velocidade máxima' in carSpecRaw else None,
            "acceleration-0-100-km/h": stringSeparateFloat(carSpecRaw['Aceleração 0-100 km/h']) if 'Aceleração 0-100 km/h' in carSpecRaw else None,
        },

        "fuelUse": {
            "urban": separateFuelUse(carSpecRaw,'urban') if 'Consumo urbano' in carSpecRaw else None,
            "road": separateFuelUse(carSpecRaw,'road') if 'Consumo rodoviario' in carSpecRaw else None,
        },

        "drivingRange": {
            "urban": separateDrivingRange(carSpecRaw,'urban') if 'Autonomia urbana' in carSpecRaw else None,
            "road": separateDrivingRange(carSpecRaw,'road') if 'Autonomia rodoviaria' in carSpecRaw else None,
        },

        "source": {
            "url": 'https://www.carrosnaweb.com.br/fichadetalhe.asp?codigo={}'.format(carId),
            "carId": carId,
            "domain": 'www.carrosnaweb.com.br',
        }
    }
    return carSpec

   

 