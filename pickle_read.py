import os

import pickle

model_list=[]

def readPickle() : 


    path = 'data\models'
    file_list = os.listdir(path)
    file_list_py = [file for file in file_list if file.endswith('.pkl')]

    for i in range(len(file_list_py)) :
        file=open('data/models/' + file_list_py[i],'rb')
        clf=pickle.load(file)
        model_list.append(clf)
        file.close()

  
readPickle()

print(model_list[0])



