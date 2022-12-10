from dash import dcc
from dash import html
import plotly.graph_objs as go

from dash import html, dcc
import plotly.graph_objects as go

def render_tab(df):

    layout = html.Div([html.H1('Kanały sprzedaży a klienci',style={'text-align':'center'}),
                        html.Div([dcc.Dropdown(id='store_dropdown_gender',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='pie-gender')],style={'width':'50%'}),
                                    html.Div(id='temp-out'),
                        html.Div([dcc.Dropdown(id='store_dropdown_country',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='pie-country')],style={'width':'50%'}),
                                    html.Div(id='temp-out')
                        ])

    return layout