from keras.models import Sequential, load_model
import numpy as np
import pandas as pd
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score
from sklearn.preprocessing import LabelEncoder, MinMaxScaler,StandardScaler
import keras as k 
import tensorflow as tf
from sklearn.tree import DecisionTreeClassifier 
import joblib 
import pickle
sc=StandardScaler()
def predection(sg,al,sod,hemo,pcv,htn,dm):
 #For ckd data=(3,4,19,49,24,0,0)
 #For non ckd(0.50,0.8,0.393939,0.412281,0.609756,1.0,0.0 )
  data=(sg,al,sod,hemo,pcv,htn,dm)
  data=np.array(data)
  data=data.reshape((1,-1))
  print(data)
 # data=sc.fit_transform(data)
  print(data)
  filename='CKD_pred.pkl'
  #loaded_model=k.models.load_model('C:\Anaconda\envs\capstone\deployment\ckd_model.h5')
  loaded_model=pickle.load(open(filename,'rb'))
  #loaded_model=joblib.load(filename)
  data=loaded_model.predict(data)  
  return data

#x=predection(3,4,19,49,24,0,0)
#print(x)
#sg,al,sod,hemo,pcv,htn,dm
