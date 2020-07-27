import re

def stringSeparatePrice(string):

    splited = string.split()
    splitedList = []
    
    for a in splited:

        if a[0].isdigit():
            a = int(a.replace(".", ""))
            splitedList.append(a)

        else:
            splitedList.append(a)
    
    splitedObj = {
        "unit": splitedList[0],
        "value": splitedList[1]
    }
    
    return splitedObj

def stringSeparateInt(string):

    splited = string.split()
    splitedList = []

    for a in splited:

        if a[0].isdigit():
            a = int(a.replace(".", ""))
            splitedList.append(a)

        else:
            splitedList.append(a)
    
    splitedObj = {
        "value": splitedList[0],
        "unit": splitedList[1]
    }
    
    return splitedObj


def stringSeparateFloat(string):

    splited = string.split()
    splitedList = []

    for a in splited:

        if a[0].isdigit():
            a = float(a.replace(",", "."))
            splitedList.append(a)

        else:
            splitedList.append(a)
    
    splitedObj = {
        "value": splitedList[0],
        "unit": splitedList[1]
    }
    
    return splitedObj

def separateMaxPowerAndTorque(string,option):

    splited = string.split()
    splitedList = []

    for a in splited:

        if a[0].isdigit():
            a = float(a.replace(",", "."))
            splitedList.append(a)

        else:
            splitedList.append(a)

    if len(splitedList)>7:
        splitedObj = [{
            "type": "alcool",
            "value": splitedList[0],
            "unit": "cv" if option=="power" else "kgfm"
            }, 
            {
            "type": "gasolina",
            "value": splitedList[3],
            "unit": "cv" if option=="power" else "kgfm"
            },
            {
            "rpm": splitedList[7],
            }]
    else:
        splitedObj = {
            "value": splitedList[0],
            "unit": "cv" if option=="power" else "kgfm",
            "rpm": splitedList[3]
        }

    return splitedObj
        

def separateVolumeAndArea(string,option):

    splited = string.split()
    splitedList = []

    splitedList.append(float(splited[0].replace(',','.')))

    if option=="volume":
        splitedList.append("cm3")

    elif option=="area":
        splitedList.append("cm2")

    
    splitedObj = {
        "value": splitedList[0],
        "unit": splitedList[1]
    }

    return splitedObj


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

        splitedObj = {
        "unit": splitedList[0],
        "value": splitedList[1]
        }

        return splitedObj

    else:
        return string


def separateCompressionRatio(string):

    splited = string.split(":")
    splitedList = []
    splitedList.extend((float(splited[0].replace(",", ".")), int(splited[1])))
    return splitedList[0]

def separateFuelUse(carSpecRaw,option):

    if option == 'urban':

        splited = stringSeparateFloat(carSpecRaw['Consumo urbano'])
        splitedList = []

        if 'Consumo urbano2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Consumo urbano2'])
            splited["type"] = 'alcool'
            splited_2["type"] = 'gasolina'

            splitedList.extend((splited,splited_2))

            return splitedList
        
        else:
            return splited
        
    elif option == 'road':

        splited = stringSeparateFloat(carSpecRaw['Consumo rodoviario'])
        splitedList = []

        if 'Consumo rodoviario2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Consumo rodoviario2'])
            splited["type"] = 'alcool'
            splited_2["type"] = 'gasolina'

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
            splited["type"] = 'alcool'
            splited_2["type"] = 'gasolina'

            splitedList.extend((splited,splited_2))

            return splitedList
        
        else:
            return splited
        
    elif option == 'road':

        splited = stringSeparateFloat(carSpecRaw['Autonomia rodoviaria'])
        splitedList = []

        if 'Autonomia rodoviaria2' in carSpecRaw:
            splited_2 = stringSeparateFloat(carSpecRaw['Autonomia rodoviaria2'])
            splited["type"] = 'alcool'
            splited_2["type"] = 'gasolina'

            splitedList.extend((splited,splited_2))

            return splitedList
        
        else:
            return splited

def getBrandOrModel(carName,option):

    brands = ["Acura","Alfa Romeo","Aston Martin","Audi","Bentley","BMW","Bugatti","Buick","Cadillac","Chevrolet",
    "Chrysler","Citroen","Dodge","Ferrari","Fiat","Ford","Geely","General Motors","GMC","Honda","Hyundai","Infiniti",
    "Jaguar","Jeep","Kia","Koenigsegg","Lamborghini","Land Rover","Lexus","Maserati","Mazda","McLaren","Mercedes-Benz",
    "Mini","Mitsubishi","Nissan","Pagani","Peugeot","Porsche","Ram","Renault","Rolls Royce","Saab","Subaru","Suzuki",
    "Tata Motors","Tesla","Toyota","Volkswagen","Volvo"]

    carBrand = list(re.match(f"({'|'.join(brands)})(.*)", carName).groups())

    if option=='brand':
        return carBrand[0]
    
    elif option=='model':
        return carBrand[1].strip()


def createCleanCarSpec(carSpecRaw,carName,carId):

    carSpec = {
        "id": int(carId),
        "name": carName,
        "brand": getBrandOrModel(carName,'brand'),
        "model": getBrandOrModel(carName,'model'),
        "year": int(carSpecRaw["Ano"]) if 'Ano' in carSpecRaw else None,
        "price": stringSeparatePrice(carSpecRaw["Preço"]) if 'Preço' in carSpecRaw else None,
        "fuel": carSpecRaw["Combustível"] if 'Combustível' in carSpecRaw else None,
        "IPVA": separateCheckUp(carSpecRaw["IPVA"]) if 'IPVA' in carSpecRaw else None,
        "insurance": stringSeparatePrice(carSpecRaw["Seguro"]) if 'Seguro' in carSpecRaw else None,
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
            
            "valves":{
                "control": carSpecRaw["Comando de válvulas"] if 'Comando de válvulas' in carSpecRaw else None,
                "perCylinder": int(carSpecRaw["Válvulas por cilindro"]) if 'Válvulas por cilindro' in carSpecRaw else None
            },
            "cylinder": {
                "capacity": separateVolumeAndArea(carSpecRaw['Cilindrada'],'volume') if 'Cilindrada' in carSpecRaw else None,
                "quantity": int(carSpecRaw["Cilindros"].split()[0]) if 'Cilindros' in carSpecRaw else None,
                "diameter": stringSeparateFloat(carSpecRaw["Diâmetro dos cilindros"]) if 'Diâmetro dos cilindros' in carSpecRaw else None,
                "pistonStroke": stringSeparateFloat(carSpecRaw["Curso dos pistões"]) if 'Curso dos pistões' in carSpecRaw else None,
                "compressionRatio": separateCompressionRatio(carSpecRaw["Razão de compressão"]) if 'Razão de compressão' in carSpecRaw else None,
            },
            "power": {
                "max": separateMaxPowerAndTorque(carSpecRaw['Potência máxima'],"power") if 'Potência máxima' in carSpecRaw else None,
                "specific": stringSeparateFloat(carSpecRaw['Potência específica']) if 'Potência específica' in carSpecRaw else None,
                "weight": stringSeparateFloat(carSpecRaw['Peso/potência']) if 'Peso/potência' in carSpecRaw else None,
            },
            "torque": {
                "max": separateMaxPowerAndTorque(carSpecRaw['Torque máximo'],"torque") if 'Torque máximo' in carSpecRaw else None,
                "specific": stringSeparateFloat(carSpecRaw['Torque específico']) if 'Torque específico' in carSpecRaw else None,
                "weight": stringSeparateFloat(carSpecRaw['Peso/torque']) if 'Peso/torque' in carSpecRaw else None,
            },
            
            "engineCode": carSpecRaw['Código do motor'] if 'Código do motor' in carSpecRaw else None,
            
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
            "frontArea": separateVolumeAndArea(carSpecRaw['Área frontal (A)'],'area') if 'Área frontal (A)' in carSpecRaw else None,
            "dragCoefficient": float(carSpecRaw['Coeficiente de arrasto (Cx)'].replace(',','.')) if 'Coeficiente de arrasto (Cx)' in carSpecRaw else None,
            "frontAreaCorrected": separateVolumeAndArea(carSpecRaw['Área frontal corrigida'],'area') if 'Área frontal corrigida' in carSpecRaw else None,
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
            "domain": 'www.carrosnaweb.com.br',
        }
    }
    return carSpec



   

 