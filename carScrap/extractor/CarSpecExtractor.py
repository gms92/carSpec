class CarSpecExtractor:

    
    def cleanEmptyLists(self,lists):

        cleanLists = [l for l in lists if l != []]

        return cleanLists
    
    
    def replaceRepeatedKeys(self,keys):

        keysFilter = []

        for key in keys:
            if key[0] == 'Dianteiros' and key[1] == 'Traseiros':
                key = ['Freios dianteiros','Freios traseiros']

            if key[0] == 'Dianteira' and key[1] == 'Elemento elástico':
                key = ['Suspensão dianteira','Elemento elástico dianteiro']

            if key[0] == 'Traseira' and key[1] == 'Elemento elástico':
                key = ['Suspensão traseira','Elemento elástico traseiro']

            if key[0] == 'Dianteiros' and key[1] == 'Altura do flanco':
                key = ['Pneus dianteiros','Altura do flanco dianteiro']

            if key[0] == 'Traseiros' and key[1] == 'Altura do flanco':
                key = ['Pneus traseiros','Altura do flanco traseiro']

            keysFilter.append(key)
            

        return keysFilter

    def cleanRawValues(self,values):

        valuesFilter = []

        for value in values:

            if len(value)>2:
                value = [v for v in value if v!="1"]
                value = [v for v in value if v!="2"]
                value = [v for v in value if v!="3"]

            value = [v for v in value if "\n" not in v]
            
            for v in value:
                if v==' kg/cv' or v==' kg/kgfm':
                    value[0]=value[0]+value[1]
                    value.pop(1)

                if 'rpm' in v and 'kgfm' in v:
                    value[-1]=value[-2]+value[-1]
                    value.pop(-2)
                
            if len(value)>2:
                value[-1]= value[-2]+" "+value[-1]
                value.pop(-2)

                
            valuesFilter.append(value)

        return valuesFilter
    

    
    def transformKeys(self,keys):

        keys[-2] = ['Consumo urbano','Consumo rodoviario']
        keys[-1] = ['Consumo urbano2','Consumo rodoviario2']

        keys.append(['Autonomia urbana','Autonomia rodoviaria'])
        keys.append(['Autonomia urbana2','Autonomia rodoviaria2'])

    def checkDoubleFields(self,carSpecRaw):

        if 'Autonomia urbana' not in carSpecRaw:
            carSpecRaw['Autonomia urbana'] = carSpecRaw.pop('Consumo urbano2')
            carSpecRaw['Autonomia rodoviaria'] = carSpecRaw.pop('Consumo rodoviario2')

