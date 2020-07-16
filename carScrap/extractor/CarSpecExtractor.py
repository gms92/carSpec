class CarSpecExtractor:

    def replaceRepeatedKeys(self,keys):

        keysFilter = []

        for c in keys:
            if c[0] == 'Dianteiros' and c[1] == 'Traseiros':
                c = ['Freios dianteiros','Freios traseiros']

            if c[0] == 'Dianteira' and c[1] == 'Elemento elástico':
                c = ['Suspensão dianteira','Elemento elástico dianteiro']

            if c[0] == 'Traseira' and c[1] == 'Elemento elástico':
                c = ['Suspensão traseira','Elemento elástico traseiro']

            if c[0] == 'Dianteiros' and c[1] == 'Altura do flanco':
                c = ['Pneus dianteiros','Altura do flanco dianteiro']

            if c[0] == 'Traseiros' and c[1] == 'Altura do flanco':
                c = ['Pneus traseiros','Altura do flanco traseiro']

            keysFilter.append(c)
            

        return keysFilter

    
    
    def filterRawDataFromValues(self,values):

        valuesFilter = []

        for c in values:

            if len(c)>2:
                c = [a for a in c if a!="1"]
                c = [a for a in c if a!="2"]
                c = [a for a in c if a!="3"]

            c = [a for a in c if "\n" not in a]
            
            for a in c:
                if a==' kg/cv' or a==' kg/kgfm':
                    c[0]=c[0]+c[1]
                    c.pop(1)

                if 'rpm' in a and 'kgfm' in a:
                    c[-1]=c[-2]+c[-1]
                    c.pop(-2)
                
            if len(c)>2:
                c[-1]= c[-2]+" "+c[-1]
                c.pop(-2)

                
            valuesFilter.append(c)

        return valuesFilter

