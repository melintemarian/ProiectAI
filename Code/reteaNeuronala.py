import procesare
import random

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
import numpy
from tensorflow import keras as ks
from keras.utils import to_categorical

def codare(lista):
    final=dict()
    counter=0
    for i in lista:
        final[i]=counter
        counter+=1
    return final

def ambiguizare(inp):
    dic=dict()
    counter=-1
    for i in inp:
        counter+=1
        dic[i]=counter
    return dic

def reteaNeuronala():
    (listaTrain,listaTest)=procesare.obtineLista()   
    dimensiune=(len(listaTrain),len(listaTrain[0][0]),len(listaTrain[0][0][0]))
    random.shuffle(listaTrain)
    random.shuffle(listaTest)
    amb=ambiguizare(list(set([i[1] for i in listaTrain])))
    X_Train=numpy.array([i[0] for i in listaTrain])
    Y_Train=numpy.array([amb[i[1]] for i in listaTrain])
    X_Test=numpy.array([i[0] for i in listaTest])
    Y_Test=numpy.array([amb[i[1]] for i in listaTest])
    
    X_Train=X_Train.reshape(dimensiune[0],dimensiune[1]*dimensiune[2])
    X_Test=X_Test.reshape(len(listaTest),dimensiune[1]*dimensiune[2])
    Y_Train=to_categorical(Y_Train)
    Y_Test=to_categorical(Y_Test)
    model = Sequential()
    model.add(Dense(dimensiune[1]*dimensiune[2],input_shape=(dimensiune[1]*dimensiune[2],)))
    model.add(Dense(int(dimensiune[1]*dimensiune[2]/4),activation="relu"))
    model.add(Dense(int(dimensiune[1]*dimensiune[2]/16),activation="relu"))
    model.add(Dense(int(dimensiune[1]*dimensiune[2]/64),activation="relu"))
    model.add(Dense(32,activation="sigmoid"))

    model.compile(loss='categorical_crossentropy',optimizer="adam",metrics=['accuracy'])
    
    model.fit(X_Train,Y_Train,epochs=2,batch_size=10)

    scores=model.evaluate(X_Test,Y_Test)
    
    print(scores)

if __name__ == "__main__":
    reteaNeuronala()