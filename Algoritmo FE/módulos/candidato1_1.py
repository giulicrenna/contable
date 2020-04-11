    if candidato1_1: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato1_1, 'es: ') #PARAMETRO EDAD
        edadcandidato1_1 = input()
        if edadcandidato1_1 > str(75):
            candi1 -= 4
        if edadcandidato1_1 < str(75):
            candi1 += 2
        if edadcandidato1_1 < 20
            candi1 -= 10
        print ('¿tiene', candidato1_1, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 'si': 
            candi1 += 2
        if secundario == 'no':
            candi1 -= 2
        print ('¿tiene', candidato1_1,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi1 += 2
        if grado == 'no':
            candi1 -= 2
        print ('¿tiene', candidato1_1,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi1 += 1
        if doc == 'no':
            candi1 -= 1
        print ('¿tiene', candidato1_1, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi1 -= 4
            if cant < str(2):
                candi1 -= 2