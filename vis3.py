import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.plotly as py

def get_users_insights(df):    
    a=0
    b=0
    c=0
    d=0
    e=0    
    for row in df['1SPI']:
         if(row>=5.0 and row<6.0):
            a+=1 
         if(row>=6.0 and row<7.0):
            b+=1 
         if(row>=7.0 and row<8.0):
            c+=1 
         if(row>=8.0 and row<9.0):
            d+=1 
         if(row>=9.0 and row<10.0):
            e+=1   
    
    traces = [
            go.Bar(
                x=['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'],
                y=[a,b,c,d,e],
                name='SEM-1',
                marker=go.bar.Marker(
                    color='rgb(55, 83, 109)'
                )
            )]


    labels = ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI']
    values = [a,b,c,d,e]

    trace = go.Pie(labels=labels, values=values)

    
    a=0
    b=0
    c=0
    d=0
    e=0    
    for row in df['2SPI']:
         if(row>=5.0 and row<6.0):
            a+=1 
         if(row>=6.0 and row<7.0):
            b+=1 
         if(row>=7.0 and row<8.0):
            c+=1 
         if(row>=8.0 and row<9.0):
            d+=1 
         if(row>=9.0 and row<10.0):
            e+=1   
    

    trace1 = go.Bar(
        x=['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'],
        y=[a,b,c,d,e],
        name='SEM-2'
    )
    a=0
    b=0
    c=0
    d=0
    e=0    
    for row in df['3SPI']:
         if(row>=5.0 and row<6.0):
            a+=1 
         if(row>=6.0 and row<7.0):
            b+=1 
         if(row>=7.0 and row<8.0):
            c+=1 
         if(row>=8.0 and row<9.0):
            d+=1 
         if(row>=9.0 and row<10.0):
            e+=1   
    
    trace2 = go.Bar(
        x=['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'],
        y=[a,b,c,d,e],
        name='SEM-3'
    )
    data = traces
   
    return data
  

   
