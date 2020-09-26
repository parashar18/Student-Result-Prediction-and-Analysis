import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import re
import pickle


from sklearn.ensemble import RandomForestClassifier

def predict1(n_clicks,input1=0, input2=0, input3=0,input4=0):
     with open('finalized_model_Maths.sav', 'rb') as f:
        loaded_model = pickle.load(f)

        X_test=[input1, input2, input3, input4]
        X_test = np.array(X_test).astype(np.float)
        print("x_test : ", X_test,flush=True)
        print("inputs : ", input1,input2,input3,input4, type(input1),flush=True)
                

        totalM1=float(input1)+float(input2)

        if(totalM1>85.0):
          gradeM1=0
        if(totalM1>75.0 and totalM1<=85.0):
          gradeM1=1
        if(totalM1>65.0 and totalM1<=75.0):
          gradeM1=2
        if(totalM1>55.0 and totalM1<=65.0):
          gradeM1=3
        if(totalM1>45.0 and totalM1<=55.0):
          gradeM1=4
        if(totalM1>=35.0 and totalM1<=45.0):
          gradeM1=5
        if(totalM1<35.0):
          gradeM1=6  
        totalM2=float(input3)+float(input4)
        if(totalM2>85.0):
          gradeM2=0
        if(totalM2>75.0 and totalM2<=85.0):
          gradeM2=1
        if(totalM2>65.0 and totalM2<=75.0):
          gradeM2=2
        if(totalM2>55.0 and totalM2<=65.0):
          gradeM2=3
        if(totalM2>45.0 and totalM2<=55.0):
          gradeM2=4
        if(totalM2>=35.0 and totalM2<=45.0):
          gradeM2=5
        if(totalM2<35.0):
          gradeM2=6  
        temp=[input1,input2,totalM1,gradeM1,input3,input4,totalM2,gradeM2] 
        temp = np.array(temp).astype(np.float) 
        pkp=loaded_model.predict(temp.reshape(1,-1))
        print('pkp : ', pkp,flush=True)
        final='none'
        if(pkp==0):
          final='greater than 85'
        if(pkp==1):
          final='greater than 75 Less than 85'
        if(pkp==2):
          final='greater than 65 Less than 75'
        if(pkp==3):
          final='greater than 55 Less than 65'
        if(pkp==4):
          final='greater than 45 Less than 55'
        if(pkp==5):
          final='greater than 35 Less than 45'
        if(pkp==6):
          final='less than 35'
        print(" extra: ", gradeM2, gradeM1,totalM2,totalM1 ,flush=True)
        
        return final