from dash import dcc
from dash import html
import plotly.graph_objs as go

def render_tab(df):

    layout = html.Div([html.H1('Kanały sprzedaży a dni tygodnia',style={'text-align':'center'}),
                        html.Div([dcc.Dropdown(id='store_dropdown',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='pie-store-type')],style={'width':'50%'}),
                                    html.Div(id='temp-out'),
                        html.Div([dcc.Dropdown(id='day_dropdown',
                                    options=[{'label':dzień,'value':dzień} for dzień in df['tran_date_days'].unique()],
                                    value=df['tran_date_days'].unique()[0]),
                                    dcc.Graph(id='pie-day')],style={'width':'50%'}),
                                    html.Div(id='temp-out')
                        ])

    return layout
