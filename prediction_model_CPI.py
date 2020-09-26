import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import re
import pickle


from sklearn.ensemble import RandomForestClassifier

def predict(n_clicks,input1, input2, input3,input4, input5,input6,input7,input8):
     with open('finalized_model_CPI.sav', 'rb') as f:
        loaded_model = pickle.load(f)

        X_test=[input1, input2, input3, input4, input5, input6, input7, input8]
        X_test = np.array(X_test).astype(np.float)
        print("x_test : ", X_test,flush=True)
        pkp=loaded_model.predict(X_test.reshape(1,-1))
        print('pkp : ', pkp,flush=True)
        final='none'
        if(pkp==0):
        	final='Bellow 6.5'
        if(pkp==1):
        	final='Greater than 6.5 and Less than 7.5'
        if(pkp==2):
        	final='Greater than 7.5 and Less than 8.5'
        if(pkp==3):	
        	final='Greater than 8.5 and Less than 10'
        return final







