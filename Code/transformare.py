from cv2 import cv2

#! ATENTIE acest modul nu o sa functioneze daca este apelat singur in consola in folderul in care se afla
#! Fie rulati fisierul in cadrul proiectului, fie rulati fisierul din folderul repositoriului

def transformaImagineInMatrice(image_path): # transforma imaginea data intro matrice cu valori de la 0 pt alb la 1 pt negru
    img = cv2.imread(image_path, 0) # citeste imaginea in grayscale
    img_reverted= cv2.bitwise_not(img) # inversam valorile pentru ca albul sa fie 0, iar negrul 255
    new_img = img_reverted / 255.0
    return new_img

def obtineInaltimeaMinimaSiInaltimeaMaxima(lista): # obtinem primul si ultimul rand la care apare un pixel negru
    global maxim
    global minim
    maxim=0
    minim=1024000
    for i in lista:
        for j in range(0,len(i)):
            if 1. in i[j]:
                maxim=max(maxim,j)
                minim=min(minim,j)
    return(minim,maxim)

def obtineLatimeaMaximaSiLatimeaMinima(lista): # obtinem prima si ultima coloana la care apare un pixel negru
    global maxim
    global minim
    maxim=0
    minim=1024000
    for i in lista:
        for j in i:
            for k in range(0,len(j)):
                if j[k] != 0:
                    maxim=max(maxim,k)
                    minim=min(minim,k)
    return(minim,maxim)

def eliminaExcesul(lista): # copiem dreptunghiul format de cele 4 coordonate intr-o noua lista

    def Optimizeaza(inputLista,minI,maxI,minJ,maxJ):
        nouaLista=list() # lista noua va contine lista de matrici
        for i in inputLista:
            aux=[] # aux va contine o matrice
            for j in range(minI,maxI+1):
                buff=[] # buff va contine doar o linie
                for k in range(minJ,maxJ+1):
                    buff.append(i[j][k])
                aux.append(buff)
            nouaLista.append(aux)
        return nouaLista
    
    (listaTrain,listaTest) = lista # creem doua liste

    #aflam minim/maximul pentru fiecare lista
    (minITemp,maxITemp)=obtineInaltimeaMinimaSiInaltimeaMaxima(listaTrain) 
    (minJTemp,maxJTemp)=obtineLatimeaMaximaSiLatimeaMinima(listaTrain)

    (minITemp2,maxITemp2)=obtineInaltimeaMinimaSiInaltimeaMaxima(listaTest)
    (minJTemp2,maxJTemp2)=obtineLatimeaMaximaSiLatimeaMinima(listaTest)

    #luam extremele
    minI=min(minITemp,minITemp2)
    maxI=max(maxITemp,maxITemp2)
    minJ=min(minJTemp,minJTemp2)
    maxJ=max(maxJTemp,maxJTemp2)
    
    #oprimizam fiecare lista in mod individual
    listaTrainFinala=Optimizeaza(listaTrain,minI,maxI,minJ,maxJ)
    listaTestFinala=Optimizeaza(listaTest,minI,maxI,minJ,maxJ)

    return (listaTrainFinala,listaTestFinala) #retrunam tuplul; prima lista de antrebare, a doua lista de testare

if __name__ == "__main__":
    
    x=transformaImagineInMatrice("char_trainable_split/test/a/ca372230-3a15-4359-b84b-da02fe913d65.png")
    y=transformaImagineInMatrice("char_trainable_split/test/a/cbfe969b-fda4-4ee4-8966-3e1c65bb3beb.png")
    z=transformaImagineInMatrice("char_trainable_split/test/a/f971ad91-93dc-4e64-ba76-c8693bf8d0d0.png")
    lista=[]
    lista.append(x)
    lista.append(y)
    lista.append(z)

    a=transformaImagineInMatrice("char_trainable_split/train/a/0b7a718b-8cbd-427b-b5f4-5041155c4a48.png")
    b=transformaImagineInMatrice("char_trainable_split/train/a/1b41dca0-b24b-4304-bf60-0255844db435.png")
    c=transformaImagineInMatrice("char_trainable_split/train/a/2def46ee-4686-496f-abc4-96142caf76df.png")
    lista2=[]
    lista2.append(a)
    lista2.append(b)
    lista2.append(c)

    aux=eliminaExcesul((lista2,lista))
    for i in aux[0]:
        for j in i:
            print(j)
        print()
    for i in aux[1]:
        for j in i:
            print(j)
        print()