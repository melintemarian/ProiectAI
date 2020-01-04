import transformare
import os

#! ATENTIE acest modul nu o sa functioneze daca este apelat singur in consola in folderul in care se afla
#! Fie rulati fisierul in cadrul proiectului, fie rulati fisierul din folderul repositoriului

def obtineLista():
    absolute_path = os.path.dirname(os.path.realpath("char_trainable_split")) # Cautam dinamic fisierul char_trainable_split
    dir_path_train=os.path.join(absolute_path,"char_trainable_split","train") # Obtinem path-ul pentru folderul de antrenare
    dir_path_test=os.path.join(absolute_path,"char_trainable_split","test") # Obtinem path-ul pentru folderul de test
    lista_litere=os.listdir(dir_path_test) # Obtinem lista de litere a alfabetului
    dictionarFinal=dict() # creem dictionarul in care sa stocam tot
    for i in lista_litere:
        listaPozeTrain=[] # creem listele in care sa stocam datele de antrenare si test
        listaPozeTest=[]

        director=os.path.join(dir_path_train,i)
        aux=os.listdir(director)
        for j in aux: # pentru fiecare poza de antrenare creem o matrice
            temp=transformare.transformaImagineInMatrice(os.path.join(director,j))
            listaPozeTrain.append(temp)

        director=os.path.join(dir_path_test,i)
        aux=os.listdir(director)
        for j in aux: # pentru fiecare poza de testare creem o matrice
            temp=transformare.transformaImagineInMatrice(os.path.join(director,j))
            listaPozeTest.append(temp)
        
        (listaPozeTrain,listaPozeTest)=transformare.eliminaExcesul((listaPozeTrain,listaPozeTest)) # optimizam tot
        dictionarFinal[i]=(listaPozeTrain,listaPozeTest) # adaugam in dictionar o tupla; prima data lista de antrenament, dupa lista de test
    return dictionarFinal # retrunam dicionarul

if __name__ == "__main__":
    #procesarea ia in jur de 18-19 secunde
    y=obtineLista()
    print(len(y))
    x=y['j']
    for i in x[0]:
        for j in i:
            print(j)
        print()
