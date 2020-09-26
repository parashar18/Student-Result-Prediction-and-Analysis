import pandas as pd
import numpy as np
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.tools as tls
import prediction_model_CPI as pmc
import prediction_model_Maths as pmm
from dash.dependencies import Input, Output,State
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import tables as ts
import vis3 as vss
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Load the data
VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)



df = pd.read_csv('data.csv') 
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
a1=0
b1=0
c1=0
d1=0
e1=0    
for row in df['2SPI']:
         if(row>=5.0 and row<6.0):
            a1+=1 
         if(row>=6.0 and row<7.0):
            b1+=1 
         if(row>=7.0 and row<8.0):
            c1+=1 
         if(row>=8.0 and row<9.0):
            d1+=1 
         if(row>=9.0 and row<10.0):
            e1+=1 
a2=0
b2=0
c2=0
d2=0
e2=0    
for row in df['3SPI']:
         if(row>=5.0 and row<6.0):
            a2+=1 
         if(row>=6.0 and row<7.0):
            b2+=1 
         if(row>=7.0 and row<8.0):
            c2+=1 
         if(row>=8.0 and row<9.0):
            d2+=1 
         if(row>=9.0 and row<10.0):
            e2+=1 
a3=0
b3=0
c3=0
d3=0
e3=0    
for row in df['4SPI']:
         if(row>=5.0 and row<6.0):
            a3+=1 
         if(row>=6.0 and row<7.0):
            b3+=1 
         if(row>=7.0 and row<8.0):
            c3+=1 
         if(row>=8.0 and row<9.0):
            d3+=1 
         if(row>=9.0 and row<10.0):
            e3+=1 
app = dash.Dash(__name__)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server
app.title = 'STUDENT RESULT'
app.layout = html.Div(children=[
    html.H1(
        children='STUDENT RESULT PREDICTION PORTAL',
        style={'text-align': 'center'}
    ),
    #style={'font-size': 18}
    

    

    dcc.Tabs(id="tabs", children=[

        dcc.Tab(label=
            'DATA',
                children=[
                    ts.ek_func(df)
            ]
        ),
        dcc.Tab(label='VISUALIZATION', children=[
        

            html.Div([
                    dcc.Graph(
                    id='Sem wise',
                    figure={
                        'data': [
                            {'x': ['Sem 1','Sem 2','Sem 3', 'Sem 4'], 'y': [a,a1,a2,a3], 'type': 'bar', 'name': '5 SPI '},
                            {'x': ['Sem 1','Sem 2','Sem 3', 'Sem 4'], 'y': [b,b1,b2,b3], 'type': 'bar', 'name': '6 SPI'},
                            {'x': ['Sem 1','Sem 2','Sem 3', 'Sem 4'], 'y': [c,c1,c2,c3], 'type': 'bar', 'name': '7 SPI'},
                            {'x': ['Sem 1','Sem 2','Sem 3', 'Sem 4'], 'y': [d,d1,d2,d3], 'type': 'bar', 'name': '8 SPI'},
                            {'x': ['Sem 1','Sem 2','Sem 3', 'Sem 4'], 'y': [e,e1,e2,e3], 'type': 'bar', 'name': '9 SPI'},
                                               
                        ],
                        
                   'layout': {
                    'title': 'SEMESTER WISE SPI'}
                    }
                
                )
             ],className='1'), 
            html.Div([  
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a,b,c,d,e], 'type': 'bar', 'name': 'Sem1'},
                            {'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a1,b1,c1,d1,e1], 'type': 'bar', 'name': 'Sem2'},
                            {'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a2,b2,c2,d2,e2], 'type': 'bar', 'name': 'Sem3'},
                            {'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a3,b3,c3,d3,e3], 'type': 'bar', 'name': 'Sem4'},
                        ],
                        
                    
                    'layout': {
                    'title': 'SPI WISE SEMESTER'
                     }
                    }
                ) 


            ],className='2' ),
            html.Div(children=[
            dcc.Graph(
            id='example-graphpie',
            figure={
                'data': [
                     { 'values': [a,b,c,d,e], 'type': 'pie', 'name': 'Sem1', 'labels': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI']
                        },
                    ],
                'layout': {
                    'title': 'SEMESTER 1'
                }
            }
            )
            ]),
            html.Div(children=[
            dcc.Graph(
            id='example-graphpie1',
            figure={
                'data': [
                     { 'values': [a1,b1,c1,d1,e1], 'type': 'pie', 'name': 'Sem2', 'labels': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI']
                        },
                    
                    #{'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a1,b1,c1,d1,e1], 'type': 'pie', 'name': u'Sem2'},
                    #{'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a2,b2,c2,d2,e2], 'type': 'pie', 'name': u'Sem3'},
                ],
                'layout': {
                    'title': 'SEMESTER 2'
                }
            }
            )
            ]),
            html.Div(children=[
            dcc.Graph(
            id='example-graphpie2',
            figure={
                'data': [
                     { 'values': [a2,b2,c2,d2,e2], 'type': 'pie', 'name': 'Sem3', 'labels': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI']
                        },
                    
                    #{'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a1,b1,c1,d1,e1], 'type': 'pie', 'name': u'Sem2'},
                    #{'x': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI', '10 SPI'], 'y': [a2,b2,c2,d2,e2], 'type': 'pie', 'name': u'Sem3'},
                ],
                'layout': {
                    'title': 'SEMESTER 3'
                }
            }
            )
            ]),
            html.Div(children=[
            dcc.Graph(
            id='example-graphpie3',
            figure={
                'data': [
                     { 'values': [a3,b3,c3,d3,e3], 'type': 'pie', 'name': 'Sem4', 'labels': ['5 SPI','6 SPI','7 SPI', '8 SPI', '9 SPI']
                        },
                ],
                'layout': {
                    'title': 'SEMESTER 4'
                }
            }
            )
            ])   



          
        ]),
        dcc.Tab(label=
            'CPI PREDICTION',
                children=[

                          
                            
                            html.Div(children='SSC Board'),(dcc.Input(id='SSC_BoardType', type='text')),
                            html.Div(children='SSC result'),
                            dcc.Input(id='SSC_Board', type='text'),
                            html.Div(children='hSC Board'),(dcc.Input(id='hSC_BoardType', type='text')),
                            html.Div(children='HSC result'),(dcc.Input(id='HSC_Board', type='text')),
                            html.Div(children='Sem 1 SPI'),(dcc.Input(id='1SPI', type='text')),
                            html.Div(children='Sem 2 SPI'),(dcc.Input(id='2SPI', type='text')),
                            html.Div(children='Sem 3 SPI'),(dcc.Input(id='3SPI', type='text')),
                            html.Div(children='Sem 4 SPI'),(dcc.Input(id='4SPI', type='text')),
                            html.Button('Submit', id='button',n_clicks=0),
                            html.Div(id='output-container-button',
                                     children='Enter a value and press submit')
                        
           
                        ]
              ),          

        dcc.Tab(label=
            'MATHS PREDICTION',
                children=[

                          
                           html.Div(children='Enter details of Maths Marks'),
                           html.Div(children='Maths 1 External Marks'),(dcc.Input(id='EXTERNAL_MATHS_1', type='text')),
                           html.Div(children='MATHS 1 Internal Marks'),dcc.Input(id='INTENAL_MATHS_1', type='text'),
                           html.Div(children='Maths 2 External Marks'),(dcc.Input(id='EXTERNAL_MATHS_2', type='text')),
                           html.Div(children='MATHS 2 Internal Marks'),(dcc.Input(id='INTENAL_MATHS_2', type='text')),
                           html.Button('Submit', id='button1',n_clicks=0),
                           html.Div(id='output-container-button1',
                                                     children='Enter a value and press submit'),
                                                    
                        


                       
                    
                    
            ]
        )
           


    ]),
])

@app.callback(
                 Output('output-container-button', 'children'),
                 [Input('button','n_clicks')],
                 [State('SSC_BoardType', 'value'),
                 State('SSC_Board', 'value'),
                 State('hSC_BoardType', 'value'),
                 State('HSC_Board', 'value'),
                 State('1SPI', 'value'),
                 State('2SPI', 'value'),
                 State('3SPI', 'value'),
                 State('4SPI', 'value')])
def update_output(n_clicks,input1,input2,input3,input4,input5,input6,input7,input8):
                #print()
                te = []
                for i in [n_clicks,input1,input2,input3,input4,input5,input6,input7,input8]:
                    try:
                        print(i, flush=True)
                    except Exception as e:
                        print('eror : ', e, flush=True)
                    '''
                    if i is None:
                        te.append(0)
                    else:
                        te.append(i)
                    
                    x = np.array(i)


                    for j in x:
                        if np.isnan(j):
                            te.append(0.0)
                        else:
                            te.append(j)
                    '''
                #n_clicks,input1,input2,input3,input4,input5,input6,input7,input8 = te
                #print('HIIIIIIIIIIIIIIIIIIIIIIIIII', flush=True)
                #print(input1.dtype)

                result=pmc.predict(n_clicks,input1,input2,input3,input4,input5,input6,input7,input8)
                return 'CPI  Will be {}'.format(
                         result       
                          )

                 #return 'The input value was {} {} {} and the button has been clicked  times'.format(
                              #input1,input2,input3,input4,input5,input6,n_clicks
@app.callback(
                Output('output-container-button1', 'children'),
                 [Input('button1', 'n_clicks')],
                 [State('EXTERNAL_MATHS_1', 'value'),
                 State('INTENAL_MATHS_1', 'value'),
                 State('EXTERNAL_MATHS_2', 'value'),
                 State('INTENAL_MATHS_2', 'value')
                 ]
              )
def update_output1(n_clicks,input1,input2,input3,input4):
             #print()
                te = []
                for i in [n_clicks,input1,input2,input3,input4]:
                    try:
                        print(i, flush=True)
                    except Exception as e:
                        print('eror : ', e, flush=True)
                    '''
                    if i is None:
                        te.append(0)
                    else:
                        te.append(i)
                    
                    x = np.array(i)


                    for j in x:
                        if np.isnan(j):
                            te.append(0.0)
                        else:
                            te.append(j)
                    '''
                #n_clicks,input1,input2,input3,input4,input5,input6,input7,input8 = te
                #print('HIIIIIIIIIIIIIIIIIIIIIIIIII', flush=True)
                #print(input1.dtype)

                result1=pmm.predict1(n_clicks,input1,input2,input3,input4)
                return 'Maths Marks  Will be {}'.format(
                         result1       
                )   
                                         

@app.callback(
    Output('datatable-simple', 'selected_row_indices'),
    [Input('datatable-simple', 'rows')],
    [State('datatable-simple', 'selected_row_indices')])
 

def update_selected_row_indices(clickData, selected_row_indices):
    if clickData:
        for point in clickData['points'].values:
            if point['pointNumber'] in selected_row_indices:
                selected_row_indices.remove(point['pointNumber'])
            else:
                selected_row_indices.append(point['pointNumber'])
    return selected_row_indices
app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})
# Loading screen CSS
app.css.append_css(
    {"external_url": "https://codepen.io/chriddyp/pen/brPBPO.css"})

app.scripts.config.serve_locally = True
if __name__ == '__main__':
    app.run_server(debug=True)
