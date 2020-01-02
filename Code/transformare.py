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
    (minI,maxI)=obtineInaltimeaMinimaSiInaltimeaMaxima(lista)
    (minJ,maxJ)=obtineLatimeaMaximaSiLatimeaMinima(lista)
    
    nouaLista=list() # lista noua va contine lista de matrici
    for i in lista:
        aux=[] # aux va contine o matrice
        for j in range(minI,maxI+1):
            buff=[] # buff va contine doar o linie
            for k in range(minJ,maxJ+1):
               buff.append(i[j][k])
            aux.append(buff)
        nouaLista.append(aux)
    return nouaLista

if __name__ == "__main__":
    
    x=transformaImagineInMatrice("char_trainable_split/test/a/ca372230-3a15-4359-b84b-da02fe913d65.png")
    y=transformaImagineInMatrice("char_trainable_split/test/a/cbfe969b-fda4-4ee4-8966-3e1c65bb3beb.png")
    z=transformaImagineInMatrice("char_trainable_split/test/a/f971ad91-93dc-4e64-ba76-c8693bf8d0d0.png")
    lista=[]
    lista.append(x)
    lista.append(y)
    lista.append(z)

    aux=eliminaExcesul(lista)
    for i in aux:
        for j in i:
            print(j)
        print()
    print(len(aux),len(aux[0]),len)