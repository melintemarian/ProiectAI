import os
import pandas as pd
import matplotlib.pyplot as plt

#! ATENTIE acest modul nu o sa functioneze daca este apelat singur in consola in folderul in care se afla
#! Fie rulati fisierul in cadrul proiectului, fie rulati fisierul din folderul repositoriului

def obtineStatistici(): #Aceasta functie numara cate poze avem pentru antrenare si testare pentru fiecare litera
    absolute_path = os.path.dirname(os.path.realpath("char_trainable_split")) # Cautam dinamic fisierul char_trainable_split
    dir_path_train=os.path.join(absolute_path,"char_trainable_split","train") # Obtinem path-ul pentru folderul de antrenare
    dir_path_test=os.path.join(absolute_path,"char_trainable_split","test") # Obtinem path-ul pentru folderul de test
    lista_litere=os.listdir(dir_path_test) # Obtinem lista de litere a alfabetului
    dictionar_litere=dict() 
    for i in lista_litere:
        nr_antrenare=len(os.listdir(os.path.join(dir_path_train,i))) # Se numara imaginile din folderul de antrenare
        nr_test=len(os.listdir(os.path.join(dir_path_test,i))) # Se numara imaginile din folderul de test
        dictionar_litere[i]=(nr_antrenare,nr_test) # Adaugam in dictionar
    return dictionar_litere

if __name__ == "__main__":

	lista = list(obtineStatistici().values())
	litere = obtineStatistici().keys()
	print(lista)
	list1, list2 = zip(*lista)

	print(list1)
	print(list2)
	print(litere)

	plt.bar(litere, list1)
	plt.show()

	plt.bar(litere, list2)
	plt.show()
