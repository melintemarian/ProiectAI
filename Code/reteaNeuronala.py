import procesare
import random

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
import numpy
from tensorflow import keras as ks
from keras.utils import to_categorical
from keras.callbacks import Callback,ModelCheckpoint
from keras.models import load_model
from keras.layers import Dropout
from keras.wrappers.scikit_learn import KerasClassifier
import keras.backend as K

def get_f1(y_true, y_pred): #taken from old keras source code
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val

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
    model.add(Dense(32,activation="softmax"))

    model.compile(loss='categorical_crossentropy',optimizer="adam",metrics=['accuracy',get_f1])
    
    model.fit(X_Train,Y_Train,epochs=10,batch_size=100,validation_data=(X_Test,Y_Test))

    scores=model.evaluate(X_Test,Y_Test)
    print(scores)
    '''for i in list(set([j[1] for j in listaTest])):
        auxiliarX=[]
        auxiliarY=[]
        auxiliarX=[k[0] for k in listaTest if k[1]==i]
        o=len(auxiliarX)
        auxiliarX=numpy.array(auxiliarX)
        auxiliarX=auxiliarX.reshape(o,dimensiune[1]*dimensiune[2])
        auxiliarY=numpy.array([amb[k[1]] for k in listaTest if k[1]==i])
        auxiliarY=to_categorical(auxiliarY)
        scores=model.evaluate(auxiliarX,auxiliarY)
        print("Litera {}: Acuratete: {}, F1 Score: {}".format(i,scores[1],scores[2]))'''


if __name__ == "__main__":
    reteaNeuronala()