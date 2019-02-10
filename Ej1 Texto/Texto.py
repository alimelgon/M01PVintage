#Retorna número de palabras del fichero
def Palabras(archivo):
    return len(archivo.split())
    
   
#Retorna número de Vocales, numero de Consonantes o cantidad de números cuando se solicite    
def Voc_Cons_num(archivo,cadena,opcion):
    cont=0
    if opcion==1:
        vocmay=cadena.upper()
        vocales=vocmay+cadena
        for palabra in archivo:
            for caracter in palabra:
                if (caracter in vocales):
                    cont+=1
    elif opcion==2:
        consmay=cadena.upper()
        consonantes=consmay+cadena
        for palabra in archivo:
            for caracter in palabra:
                if (caracter in consonantes):
                    cont+=1
    
    elif opcion==3:
        for palabra in archivo:
            for caracter in palabra:
                if (caracter in cadena):
                    cont+=1
    
    return cont


#Retorna número de caracteres distintos a los anteriores
def OtrosCar (archivo, vocales,consonantes,numeros):
    otroscaracteres={}
    vocalesmay=vocales.upper()
    totalvocales=vocalesmay+vocales
    consonmay=consonantes.upper()
    totalcons=consonmay+consonantes
    cont=0
    palabras=archivo.split()
    for palabra in palabras:
        for caracter in palabra:
            if not (caracter in totalvocales) and not (caracter in totalcons) and not (caracter in numeros):
                cont+=1
                if otroscaracteres.get(caracter)==None:
                    otroscaracteres[caracter]=1
                else:
                    otroscaracteres[caracter]+=1
    #Si quiero buscar cuantas veces aparece cada caracter, hago una busqueda en el diccionario otroscaracteres
    #for car in otroscaracteres.keys():
        #print(otroscaracteres[car],":",car)
    return cont

#Retorna el número de parrafos que tienen contenido   
def Parrafos(file):
    file.seek(0) #leer lineas desde principio 
    cont=0
    linea=file.readlines()
    for linea in linea:
        if len(linea)!=1:  #solo cuenta las líneas no vacías
            cont+=1
            linea=file.readline()
                    
    return cont

#Retorna cantidad de mayúsculas y minúsculas segun se solicite
def may_min(archivo, vocales,consonantes,may=True):
    vocalesmay=vocales.upper()
    consonmay=consonantes.upper()
    totalmay=consonmay+vocalesmay
    totalmin=vocales+consonantes
    cont=0
    palabras=archivo.split()
    if may==True:
        for palabra in palabras:
            for caracter in palabra:
                if caracter in totalmay:
                    cont+=1
    if may==False:
        for palabra in palabras:
            for caracter in palabra:
                if caracter in totalmin:
                    cont+=1
        
    return cont
    

#Corrección texto
def correction(mitexto):
    
    mitextomaysalto=[]
    mitextomaypuntoseg=[]
    mitextomaypuntoap=[]

    #Hago las primeras sustituciones para ordenar los espacios
    mitextoA=mitexto.replace(":",": ")
    mitextoB=mitextoA.replace(" :",":")
    mitextoC=mitextoB.replace(";","; ")
    mitextoD=mitextoC.replace(" ;",";")
    mitextoE=mitextoD.replace(" .",".")
    mitextoF=mitextoE.replace(".",". ")
    mitextoG=mitextoF.replace(",",", ")
    mitextoH=mitextoG.replace(" ,",",")
    mitextoI=mitextoH.replace("       ","\t")
    mitextoJ=mitextoI.replace("      ","\t")
    mitextoK=mitextoJ.replace("     ","\t")
    mitextoL=mitextoK.replace("    ","\t")
    mitextoM=mitextoL.replace("   "," ")
    mitextoN=mitextoM.replace("  "," ")
    mitextoO=mitextoN.replace(" \n","\n")
    mitextoP=mitextoO.replace("\n ","\n")

    
    #Gestiono los puntos y seguido y los puntos y aparte
    #Despues de punto y seguido va mayuscula
    mitextodos=mitextoP.split(". ")
    for i in mitextodos:
        maypuntoseg=i.capitalize()
        
        mitextomaypuntoseg.append(maypuntoseg)
    #paso a cadena por donde habia roto    
    mitextotres='. '.join(mitextomaypuntoseg)

    #Hago una variable para almacenar los puntos y seguido
    mitextoalt=mitextotres.replace('. ','*\n')
    
    #Despues de punto y aparte va mayúscula
    mitextocuatro=mitextoalt.split('\n')
    for i in mitextocuatro:
        maypuntoap=i.capitalize()
        mitextomaypuntoap.append(maypuntoap)
        
    #paso a cadena por donde habia roto     
    mitextocinco='\n'.join(mitextomaypuntoap)

    #deshago el cambio hecho en mitextoalt
    mitextoseis=mitextocinco.replace('*\n','. ')
    mitextosiete=mitextoseis.replace('.','.')

    return mitextosiete



    
#main
namefile=input("Introduzca el nombre del fichero a leer (Ejemplo: mitexto.txt): ")
f=open(namefile,'r')
file=f.read()

vocales_min='aeiouáéíóúäëïöüàèìòù'
cons_min='bcdfghjklmnñpqrstvwxyz'
numeros='0123456789'

print('El texto tiene {:3d} palabras'.format(Palabras(file)))
print('El texto tiene {:3d} vocales'.format(Voc_Cons_num(file,vocales_min,1)))
print('El texto tiene {:3d} consonantes'.format(Voc_Cons_num(file,cons_min,2)))
print('El texto tiene {:3d} numeros'.format(Voc_Cons_num(file,numeros,3)))
print('El texto tiene {:3d} caracteres distintos'.format(OtrosCar(file,vocales_min,cons_min,numeros)))
print('El texto tiene {:3d} lineas'.format(Parrafos(f)))
print('El texto tiene {:3d} mayúsculas'.format(may_min(file,vocales_min,cons_min)))
print('El texto tiene {:3d} minúsculas'.format(may_min(file,vocales_min,cons_min,False)))  

#Escritura de resultados en el fichero stats.txt (si no existe, lo crea)
ff=open('stats.txt','w+')
ff.write('El texto:\n\n')
ff.write(file)
ff.write('\n\nTiene:\n')
ff.write('{:3d} palabras\n'.format(Palabras(file)))
ff.write('{:3d} vocales\n'.format(Voc_Cons_num(file,vocales_min,1)))
ff.write('{:3d} consonantes\n'.format(Voc_Cons_num(file,cons_min,2)))
ff.write('{:3d} numeros\n'.format(Voc_Cons_num(file,numeros,3)))
ff.write('{:3d} caracteres distintos\n'.format(OtrosCar(file,vocales_min,cons_min,numeros)))
ff.write('{:3d} párrafos\n'.format(Parrafos(f)))
ff.write('{:3d} mayúsculas\n'.format(may_min(file,vocales_min,cons_min)))
ff.write('{:3d} minúsculas\n\n\n'.format(may_min(file,vocales_min,cons_min,False)))  


#Corrijo el texto y lo escribo corregido en correccion.txt (si no existe el fichero, lo crea)
fff=open('correccion.txt','w+')

correction(file)

fff.write('El texto antiguo:\n\n')
fff.write(file)
fff.write('\n\nEl texto corregido:\n\n')
fff.write(correction(file))

#Cierro los ficheros
f.close()
ff.close()
fff.close()

