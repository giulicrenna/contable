print ('#################################################################')
print ('#                                                               #')
print ('#                                                               #')
print ('#          ALGORITMO BÁSICO DE SELECCIÓN DE CANDIDATOS          #')
print ('#             (SELECCIÓN POR VALORIZACIÓN NUMÉRICA)             #')
print ('#                                                               #')
print ('#                                                               #')
print ('#                   Aprieta enter para empezar                  #')
print ('#                                                               #')
print ('#                                                               #')
print ('#  By Giuliano Crenna Nic.                                      #')
print ('#################################################################')
opcion = input() 
candi1 = 1
candi2 = 1
candi3 = 1                                                   #IMPORTANTE
candi4 = 1                                                   #acordarme de comprobar sistema de ingreso de dato nulo o incorrecto
candi5 = 1
si = 111
no = 000
if opcion == '':
    print ('escriba cantidad de candidatos del 2 al 5')
    opcion2 = int(input())
else:
    print ('usted no escribió empezar') 
####################################################################
####################################################################   
if opcion2 == 2: #de a dos candidatos
    print ('Cree a sus candidatos')
    candidato1_1 = input('nombre al candidato 1: ') 
    if candidato1_1: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato1_1, 'es: ') #PARAMETRO EDAD
        edadcandidato1_1 = input()
        if edadcandidato1_1 > str(75):
            candi1 -= 4
        if edadcandidato1_1 < str(75):
            candi1 += 2
        if edadcandidato1_1 < str(20):
            candi1 -= 100000

        print ('¿tiene', candidato1_1, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi1 += 2
        if secundario == 000:
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

        print ('¿ha estado', candidato1_1, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi1 -= 10
            if cant < str(2):
                candi1 += 10
        if poder == 'no':
            candi1 += 10

        print ('¿ha', candidato1_1, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi1 -= 40
        if asesinado == 'no':   
            candi1 += 5

        print ('¿ha', candidato1_1, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi1 -= 2000
        if masas == 'no':   
            candi1 += 5       
    candidato1_2 = input('nombre al candidato 2: ') 
    if candidato1_2: #ALGORITMO DEL SEGUNDO CANDIDATO
        print ('la edad de', candidato1_2, 'es: ') #PARAMETRO EDAD
        edadcandidato1_2 = input()
        if edadcandidato1_2 > str(75):
            candi2 -= 4
        if edadcandidato1_2 < str(75):
            candi2 += 2
        if edadcandidato1_2 < str(20):
            candi2 -= 100000

        print ('¿tiene', candidato1_2, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi2 += 2
        if secundario == 000:
            candi2 -= 2

        print ('¿tiene', candidato1_2,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi2 += 2
        if grado == 'no':
            candi2 -= 2

        print ('¿tiene', candidato1_2,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi2 += 1
        if doc == 'no':
            candi2 -= 1

        print ('¿tiene', candidato1_2, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi2 -= 4
            if cant < str(2):
                candi2 -= 2

        print ('¿ha estado', candidato1_2, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi2 -= 10
            if cant < str(2):
                candi2 += 10
        if poder == 'no':
            candi2 += 10

        print ('¿ha', candidato1_2, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi2 -= 40
        if asesinado == 'no':   
            candi2 += 5

        print ('¿ha', candidato1_2, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi2 -= 2000
        if masas == 'no':   
            candi2 += 5
    candi1 = candidato1_1
    candi2 = candidato1_2
    list1 = [candidato1_1, candidato1_2]   
    print('Su candidato más apto es;', max(list1))
    print('Su candidato menos apto es;', min(list1))
    print(candi1, candi2)
####################################################################
####################################################################       
if opcion2 == 3: # DE A TRES CANDIDATOS
    print ('Cree a sus candidatos')
    candidato2_1 = input('nombre al candidato 1: ') 
    if candidato2_1: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato2_1, 'es: ') #PARAMETRO EDAD
        edadcandidato2_1 = input()
        if edadcandidato2_1 > str(75):
            candi1 -= 4
        if edadcandidato2_1 < str(75):
            candi1 += 2
        if edadcandidato2_1 < str(20):
            candi1 -= 100000

        print ('¿tiene', candidato2_1, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi1 += 2
        if secundario == 000:
            candi1 -= 2

        print ('¿tiene', candidato2_1,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi1 += 2
        if grado == 'no':
            candi1 -= 2

        print ('¿tiene', candidato2_1,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi1 += str(1)
        if doc == 'no':
            candi1 -= 1

        print ('¿tiene', candidato2_1, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi1 -= 4
            if cant < str(2):
                candi1 -= 2

        print ('¿ha estado', candidato2_1, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi1 -= 10
            if cant < str(2):
                candi1 += 10
        if poder == 'no':
            candi1 += 10

        print ('¿ha', candidato2_1, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi1 -= 40
        if asesinado == 'no':   
            candi1 += 5

        print ('¿ha', candidato2_1, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi1 -= 2000
        if masas == 'no':   
            candi1 += 5
    candidato2_2 = input('nombre al candidato 2: ') 
    if candidato2_2: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato2_2, 'es: ') #PARAMETRO EDAD
        edadcandidato2_2 = input()
        if edadcandidato2_2 > str(75):
            candi2 -= 4
        if edadcandidato2_2 < str(75):
            candi2 += 2
        if edadcandidato2_2 < str(20):
            candi2 -= 100000

        print ('¿tiene', candidato2_2, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi2 += 2
        if secundario == 000:
            candi2 -= 2

        print ('¿tiene', candidato2_2,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi2 += 2
        if grado == 'no':
            candi2 -= 2

        print ('¿tiene', candidato2_2,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi2 += str(1)
        if doc == 'no':
            candi2 -= 1

        print ('¿tiene', candidato2_2, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi2 -= 4
            if cant < str(2):
                candi2 -= 2

        print ('¿ha estado', candidato2_2, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi2 -= 10
            if cant < str(2):
                candi2 += 10
        if poder == 'no':
            candi2 += 10

        print ('¿ha', candidato2_2, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi2 -= 40
        if asesinado == 'no':   
            candi2 += 5

        print ('¿ha', candidato2_2, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi2 -= 2000
        if masas == 'no':   
            candi2 += 5        
    candidato2_3 = input('nombre al candidato 3: ') 
    if candidato2_3: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato2_3, 'es: ') #PARAMETRO EDAD
        edadcandidato2_3 = input()
        if edadcandidato2_3 > str(75):
            candi3 -= 4
        if edadcandidato2_3 < str(75):
            candi3 += 2
        if edadcandidato2_3 < str(20):
            candi3 -= 100000

        print ('¿tiene', candidato2_3, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi3 += 2
        if secundario == 000:
            candi3 -= 2

        print ('¿tiene', candidato2_3,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi3 += 2
        if grado == 'no':
            candi3 -= 2

        print ('¿tiene', candidato2_3,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi3 += str(1)
        if doc == 'no':
            candi3 -= 1

        print ('¿tiene', candidato2_3, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi3 -= 4
            if cant < str(2):
                candi3 -= 2

        print ('¿ha estado', candidato2_3, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi3 -= 10
            if cant < str(2):
                candi3 += 10
        if poder == 'no':
            candi3 += 10

        print ('¿ha', candidato2_3, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi3 -= 40
        if asesinado == 'no':   
            candi3 += 5

        print ('¿ha', candidato2_3, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi3 -= 2000
        if masas == 'no':   
            candi3 += 5                    
    list2 = [candidato2_1, candidato2_2, candidato2_3]   
    candi1 = str(candidato2_1)
    candi2 = str(candidato2_2)
    candi3 = str(candidato2_3)
    print('Su candidato más apto es;', max(list2))
    print('Su candidato menos apto es;', min(list2))
####################################################################
####################################################################    
if opcion2 == 4:
    print ('Cree a sus candidatos')
    candidato3_1 = input('nombre al candidato 1: ') 
    if candidato3_1: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato3_1, 'es: ') #PARAMETRO EDAD
        edadcandidato3_1 = input()
        if edadcandidato3_1 > str(75):
            candi1 -= 4
        if edadcandidato3_1 < str(75):
            candi1 += 2
        if edadcandidato3_1 < str(20):
            candi1 -= 100000

        print ('¿tiene', candidato3_1, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi1 += 2
        if secundario == 000:
            candi1 -= 2

        print ('¿tiene', candidato3_1,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi1 += 2
        if grado == 'no':
            candi1 -= 2

        print ('¿tiene', candidato3_1,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi1 += str(1)
        if doc == 'no':
            candi1 -= 1

        print ('¿tiene', candidato3_1, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi1 -= 4
            if cant < str(2):
                candi1 -= 2

        print ('¿ha estado', candidato3_1, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi1 -= 10
            if cant < str(2):
                candi1 += 10
        if poder == 'no':
            candi1 += 10

        print ('¿ha', candidato3_1, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi1 -= 40
        if asesinado == 'no':   
            candi1 += 5

        print ('¿ha', candidato3_1, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi1 -= 2000
        if masas == 'no':   
            candi1 += 5
    candidato3_2 = input('nombre al candidato 2: ') 
    if candidato3_2: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato3_2, 'es: ') #PARAMETRO EDAD
        edadcandidato3_2 = input()
        if edadcandidato3_2 > str(75):
            candi2 -= 4
        if edadcandidato3_2 < str(75):
            candi2 += 2
        if edadcandidato3_2 < str(20):
            candi2 -= 100000

        print ('¿tiene', candidato3_2, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi2 += 2
        if secundario == 000:
            candi2 -= 2

        print ('¿tiene', candidato3_2,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi2 += 2
        if grado == 'no':
            candi2 -= 2

        print ('¿tiene', candidato3_2,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi2 += str(1)
        if doc == 'no':
            candi2 -= 1

        print ('¿tiene', candidato3_2, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi2 -= 4
            if cant < str(2):
                candi2 -= 2

        print ('¿ha estado', candidato3_2, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi2 -= 10
            if cant < str(2):
                candi2 += 10
        if poder == 'no':
            candi2 += 10

        print ('¿ha', candidato3_2, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi2 -= 40
        if asesinado == 'no':   
            candi2 += 5

        print ('¿ha', candidato3_2, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi2 -= 2000
        if masas == 'no':   
            candi2 += 5        
    candidato3_3 = input('nombre al candidato 3: ') 
    if candidato3_3: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato3_3, 'es: ') #PARAMETRO EDAD
        edadcandidato3_3 = input()
        if edadcandidato3_3 > str(75):
            candi3 -= 4
        if edadcandidato3_3 < str(75):
            candi3 += 2
        if edadcandidato3_3 < str(20):
            candi3 -= 100000

        print ('¿tiene', candidato3_3, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi3 += 2
        if secundario == 000:
            candi3 -= 2

        print ('¿tiene', candidato3_3,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi3 += 2
        if grado == 'no':
            candi3 -= 2

        print ('¿tiene', candidato3_3,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi3 += 1
        if doc == 'no':
            candi3 -= 1

        print ('¿tiene', candidato3_3, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi3 -= 4
            if cant < str(2):
                candi3 -= 2

        print ('¿ha estado', candidato3_3, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi3 -= 10
            if cant < str(2):
                candi3 += 10
        if poder == 'no':
            candi3 += 10

        print ('¿ha', candidato3_3, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi3 -= 40
        if asesinado == 'no':   
            candi3 += 5

        print ('¿ha', candidato3_3, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi3 -= 2000
        if masas == 'no':   
            candi3 += 5       
    candidato3_4 = input('nombre al candidato 4: ') 
    if candidato3_4: #ALGORITMO DEL SEGUNDO CANDIDATO
        print ('la edad de', candidato3_4, 'es: ') #PARAMETRO EDAD
        edadcandidato3_4 = input()
        if edadcandidato3_4 > str(75):
            candi4 -= 4
        if edadcandidato3_4 < str(75):
            candi4 += 2
        if edadcandidato3_4 < str(20):
            candi4 -= 100000

        print ('¿tiene', candidato3_4, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi4 += 2
        if secundario == 000:
            candi4 -= 2

        print ('¿tiene', candidato3_4,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi4 += 2
        if grado == 'no':
            candi4 -= 2

        print ('¿tiene', candidato3_4,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi4 += 1
        if doc == 'no':
            candi4 -= 1

        print ('¿tiene', candidato3_4, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi4 -= 4
            if cant < str(2):
                candi4 -= 2

        print ('¿ha estado', candidato3_4, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi4 -= 10
            if cant < str(2):
                candi4 += 10
        if poder == 'no':
            candi4 += 10

        print ('¿ha', candidato3_4, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi4 -= 40
        if asesinado == 'no':   
            candi4 += 5

        print ('¿ha', candidato3_4, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi4 -= 2000
        if masas == 'no':   
            candi4 += 5
    list3 = [candidato3_1, candidato3_2, candidato3_3, candidato3_4]
    candi1 = str(candidato3_1)
    candi2 = str(candidato3_2)
    candi3 = str(candidato3_3)
    candi4 = str(candidato3_4)
    print('Su candidato más apto es;', max(list3))
    print('Su candidato menos apto es;', min(list3))
####################################################################
#################################################################### 
if opcion2 == 5:
    print ('Cree a sus candidatos')
    candidato4_1 = input('nombre al candidato 1: ') 
    if candidato4_1: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato4_1, 'es: ') #PARAMETRO EDAD
        edadcandidato4_1 = input()
        if edadcandidato4_1 > str(75):
            candi1 -= 4
        if edadcandidato4_1 < str(75):
            candi1 += 2
        if edadcandidato4_1 < str(20):
            candi1 -= 100000

        print ('¿tiene', candidato4_1, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi1 += 2
        if secundario == 000:
            candi1 -= 2

        print ('¿tiene', candidato4_1,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi1 += 2
        if grado == 'no':
            candi1 -= 2

        print ('¿tiene', candidato4_1,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi1 += str(1)
        if doc == 'no':
            candi1 -= 1

        print ('¿tiene', candidato4_1, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi1 -= 4
            if cant < str(2):
                candi1 -= 2

        print ('¿ha estado', candidato4_1, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi1 -= 10
            if cant < str(2):
                candi1 += 10
        if poder == 'no':
            candi1 += 10

        print ('¿ha', candidato4_1, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi1 -= 40
        if asesinado == 'no':   
            candi1 += 5

        print ('¿ha', candidato4_1, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi1 -= 2000
        if masas == 'no':   
            candi1 += 5
    candidato4_2 = input('nombre al candidato 2: ') 
    if candidato4_2: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato4_2, 'es: ') #PARAMETRO EDAD
        edadcandidato4_2 = input()
        if edadcandidato4_2 > str(75):
            candi2 -= 4
        if edadcandidato4_2 < str(75):
            candi2 += 2
        if edadcandidato4_2 < str(20):
            candi2 -= 100000

        print ('¿tiene', candidato4_2, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi2 += 2
        if secundario == 000:
            candi2 -= 2

        print ('¿tiene', candidato4_2,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi2 += 2
        if grado == 'no':
            candi2 -= 2

        print ('¿tiene', candidato4_2,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi2 += 1
        if doc == 'no':
            candi2 -= 1

        print ('¿tiene', candidato4_2, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi2 -= 4
            if cant < str(2):
                candi2 -= 2

        print ('¿ha estado', candidato4_2, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi2 -= 10
            if cant < str(2):
                candi2 += 10
        if poder == 'no':
            candi2 += 10

        print ('¿ha', candidato4_2, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi2 -= 40
        if asesinado == 'no':   
            candi2 += 5

        print ('¿ha', candidato4_2, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi2 -= 2000
        if masas == 'no':   
            candi2 += 5        
    candidato4_3 = input('nombre al candidato 3: ') 
    if candidato4_3: #ALGORITMO DEL PRIMER CANDIDATO
        print ('la edad de', candidato4_3, 'es: ') #PARAMETRO EDAD
        edadcandidato4_3 = input()
        if edadcandidato4_3 > str(75):
            candi3 -= 4
        if edadcandidato4_3 < str(75):
            candi3 += 2
        if edadcandidato4_3 < str(20):
            candi3 -= 100000

        print ('¿tiene', candidato4_3, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi3 += 2
        if secundario == 000:
            candi3 -= 2

        print ('¿tiene', candidato4_3,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi3 += 2
        if grado == 'no':
            candi3 -= 2

        print ('¿tiene', candidato4_3,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi3 += str(1)
        if doc == 'no':
            candi3 -= 1

        print ('¿tiene', candidato4_3, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi3 -= 4
            if cant < str(2):
                candi3 -= 2

        print ('¿ha estado', candidato4_3, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi3 -= 10
            if cant < str(2):
                candi3 += 10
        if poder == 'no':
            candi3 += 10

        print ('¿ha', candidato4_3, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi3 -= 40
        if asesinado == 'no':   
            candi3 += 5

        print ('¿ha', candidato4_3, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi3 -= 2000
        if masas == 'no':   
            candi3 += 5       
    candidato4_4 = input('nombre al candidato 4: ') 
    if candidato4_4: #ALGORITMO DEL SEGUNDO CANDIDATO
        print ('la edad de', candidato4_4, 'es: ') #PARAMETRO EDAD
        edadcandidato4_4 = input()
        if edadcandidato4_4 > str(75):
            candi4 -= 4
        if edadcandidato4_4 < str(75):
            candi4 += 2
        if edadcandidato4_4 < str(20):
            candi4 -= 100000

        print ('¿tiene', candidato4_4, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi4 += 2
        if secundario == 000:
            candi4 -= 2

        print ('¿tiene', candidato4_4,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi4 += 2
        if grado == 'no':
            candi4 -= 2

        print ('¿tiene', candidato4_4,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi4 += 1
        if doc == 'no':
            candi4 -= 1

        print ('¿tiene', candidato4_4, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi4 -= 4
            if cant < str(2):
                candi4 -= 2

        print ('¿ha estado', candidato4_4, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi4 -= 10
            if cant < str(2):
                candi4 += 10
        if poder == 'no':
            candi4 += 10

        print ('¿ha', candidato4_4, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi4 -= 40
        if asesinado == 'no':   
            candi4 += 5

        print ('¿ha', candidato4_4, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi4 -= 2000
        if masas == 'no':   
            candi4 += 5
    candidato4_5 = input('nombre al candidato 5: ') 
    if candidato4_5: #ALGORITMO DEL SEGUNDO CANDIDATO
        print ('la edad de', candidato4_5, 'es: ') #PARAMETRO EDAD
        edadcandidato4_5 = input()
        if edadcandidato4_5 > str(75):
            candi4 -= 4
        if edadcandidato4_5 < str(75):
            candi4 += 2
        if edadcandidato4_5 < str(20):
            candi4 -= 100000

        print ('¿tiene', candidato4_5, 'estudios secundarios?') #PARAMETRO PREPARACION 1
        secundario = input()
        if secundario == 111: 
            candi4 += 2
        if secundario == 000:
            candi4 -= 2

        print ('¿tiene', candidato4_5,'estudios de grado?') #parámetro preparación 2
        grado = input()
        if grado == 'si':
            candi4 += 2
        if grado == 'no':
            candi4 -= 2

        print ('¿tiene', candidato4_5,'al menos ún doctorado o postítulo?') #parámetro preparacion 3
        doc = input()
        if doc == 'si':
            candi4 += 1
        if doc == 'no':
            candi4 -= 1

        print ('¿tiene', candidato4_5, 'alguna causa judicial en su contra?')
        causa = input()
        if causa == 'si':
            print ('¿cuantas?')
            cant = input()
            if cant >= str(2):
                candi4 -= 4
            if cant < str(2):
                candi4 -= 2

        print ('¿ha estado', candidato4_5, 'en el poder?')
        poder = input()
        if poder == 'si':
            print('¿cuantas?')
            cant = input()
            if cant >= str(2) :
                candi4 -= 10
            if cant < str(2):
                candi4 += 10
        if poder == 'no':
            candi4 += 10

        print ('¿ha', candidato4_5, 'asesinado a alguien?')
        asesinado = input()
        if asesinado == 'si':
            candi4 -= 40
        if asesinado == 'no':   
            candi4 += 5

        print ('¿ha', candidato4_5, 'asesinado a masas?')
        masas = input()
        if masas == 'si': 
            candi4 -= 2000
        if masas == 'no':   
            candi4 += 5
    list4 = [candidato4_1, candidato4_2, candidato4_3, candidato4_4, candidato4_5]
    candi1 = str(candidato4_1)
    candi2 = str(candidato4_2)
    candi3 = str(candidato4_3)
    candi4 = str(candidato4_4)
    candi5 = str(candidato4_5)
    print('Su candidato más apto es;', max(list4))
    print('Su candidato menos apto es;', min(list4))
####################################################################
#################################################################### FIN ALGORITMO
####################################################################
#################################################################### 
if opcion2 < 2: 
    print ('monto erroneo')
if opcion2 > 5:
    print ('monto erroneo')

        