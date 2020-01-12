import transformare
import os
import random

#! ATENTIE acest modul nu o sa functioneze daca este apelat singur in consola in folderul in care se afla
#! Fie rulati fisierul in cadrul proiectului, fie rulati fisierul din folderul repositoriului

def obtineLista():
    absolute_path = os.path.dirname(os.path.realpath("char_trainable_split")) # Cautam dinamic fisierul char_trainable_split
    dir_path_train=os.path.join(absolute_path,"char_trainable_split","train") # Obtinem path-ul pentru folderul de antrenare
    dir_path_test=os.path.join(absolute_path,"char_trainable_split","test") # Obtinem path-ul pentru folderul de test
    lista_litere=os.listdir(dir_path_test) # Obtinem lista de litere a alfabetului
    listaPozeTrain=[] # creem listele in care sa stocam datele de antrenare si test
    listaPozeTest=[]
    for i in lista_litere:
        director=os.path.join(dir_path_train,i)
        aux=os.listdir(director)
        for j in aux: # pentru fiecare poza de antrenare creem o matrice
            temp=transformare.transformaImagineInMatrice(os.path.join(director,j))
            listaPozeTrain.append((temp,i))

        director=os.path.join(dir_path_test,i)
        aux=os.listdir(director)
        for j in aux: # pentru fiecare poza de testare creem o matrice
            temp=transformare.transformaImagineInMatrice(os.path.join(director,j))
            listaPozeTest.append((temp,i))
    
    auxTrain=[i[0] for i in listaPozeTrain]
    auxTest=[i[0] for i in listaPozeTest]    
    (auxTrain,auxTest)=transformare.eliminaExcesul((auxTrain,auxTest))
    ListaFinalaTrain=[]
    ListaFinalaTest=[]
    for i in range(0,len(listaPozeTrain)):
        ListaFinalaTrain.append((auxTrain[i],listaPozeTrain[i][1]))
    for i in range(0,len(listaPozeTest)):
        ListaFinalaTest.append((auxTest[i],listaPozeTest[i][1]))
    #dictionarFinal[i]=(listaPozeTrain,listaPozeTest) # adaugam in dictionar o tupla; prima data lista de antrenament, dupa lista de test
    return (ListaFinalaTrain,ListaFinalaTest) # retrunam finalul

if __name__ == "__main__":
    #procesarea ia in jur de 24-26 secunde
    (y,z)=obtineLista()
    random.shuffle(y)
    litera=""
    print(len(y[0][0][0]),len(y[0][0]))
    '''for x in range(0,100):
        for i in y[x][0]:
            print(i,len(i))
        print(y[x][1],len(y[x][0]))
        print()'''