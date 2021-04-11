import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

drop_ciudad_demog = dbc.Row([
                        dbc.Col(dcc.Dropdown(id='drop-ciudad-demog',
                            options=[{'label':'Villavicencio', 'value':'VILLAVICENCIO'}],
                            value='VILLAVICENCIO')),
                        dbc.Col(),
                        dbc.Col()
])
radio_tipo_mapa = dbc.RadioItems(id='radio-mapa',
                                 options=[{'label':'Estrato', 'value':'estrato'},
                                          {'label':'Educacion mas alta', 'value':'educacion'},
                                          {'label':'Porcentaje de acceso a internet', 'value':'internet'}],
                                 value='estrato',
                                 )



section_demog = html.Div(id='div_demog',
                         children=[html.Div('Seleccione una ciudad: '),
                                   drop_ciudad_demog,
                                   html.Br(),
                                   html.Div('Seleccione un tipo de mapa: '),
                                   radio_tipo_mapa,
                                   html.Br(),
                                   dbc.Button('Aplicar filtros',id='btn-demog',n_clicks=0),
                                   html.Div(html.Br())
                                
                                  ])



drop_ciudad_elect = dbc.Row([
                        dbc.Col(dcc.Dropdown(id='drop-ciudad-elect',
                            options=[{'label':'Villavicencio', 'value':'VILLAVICENCIO'}],
                            value='VILLAVICENCIO')),
                        dbc.Col(),
                        dbc.Col()
                        ])



section_elect = html.Div(id='div-elect',
                         children=[html.Div('Seleccione una ciudad: '),
                                   drop_ciudad_elect,
                                   html.Br(),
                                   html.Div('Seleccione un tipo de mapa: '),
                                   html.Br(),
                                   dbc.Button('Aplicar filtros',id='btn-elect',n_clicks=0),
                                   html.Div(html.Br())
                                  ])





body = html.Div([html.Div(id='div-filtros', children=[html.Div('Filtros'),
                           section_demog]),
                 html.Iframe(id='iframe-body',
                             src='https://www.google.com/maps/@4.149239,-73.5576744,12.5z?hl=es',
                             width='100%',
                             height=800)],
                 className='dash-body')