import os

def obtineStatistici(): #Aceasta functie numara cate poze avem pentru antrenare si testare pentru fiecare litera
    absolute_path = os.path.dirname(os.path.realpath("char_trainable_split")) # Cautam dinamic fisierul char_trainable_split
    dir_path_train=os.path.join(absolute_path,"char_trainable_split","test") # Obtinem path-ul pentru folderul de antrenare
    dir_path_test=os.path.join(absolute_path,"char_trainable_split","train") # Obtinem path-ul pentru folderul de test
    lista_litere=os.listdir(dir_path_test) # Obtinem lista de litere a alfabetului
    dictionar_litere=dict() 
    for i in lista_litere:
        nr_antrenare=len(os.listdir(os.path.join(dir_path_train,i))) # Se numara imaginile din folderul de antrenare
        nr_test=len(os.listdir(os.path.join(dir_path_test,i))) # Se numara imaginile din folderul de test
        dictionar_litere[i]=(nr_antrenare,nr_test) # Adaugam in dictionar
    return dictionar_litere

if __name__ == "__main__":
    print(obtineStatistici())