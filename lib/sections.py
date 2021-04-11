import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

drop_ciudad = dcc.Dropdown(id='drop-ciudad-demog',
                           options=[{'label':'Villavicencio', 'value':'VILLAVICENCIO'}],
                           value='VILLAVICENCIO')

radio_tipo_mapa = dbc.RadioItems(id='radio-mapa',
                                 options=[{'label':'Estrato', 'value':'estrato'},
                                          {'label':'Educacion mas alta', 'value':'educacion'},
                                          {'label':'Porcentaje de acceso a internet', 'value':'internet'}])



section_demog = html.Div(id='div_demog',
                         children=[html.Div('Seleccione una ciudad: '),
                                   drop_ciudad,
                                   html.Br(),
                                   html.Div('Seleccione un tipo de mapa: '),
                                   radio_tipo_mapa,
                                   html.Div(html.Br())
                                
                                  ])

section_elect = html.Div(id='div-elect',
                         children=[html.Div('Seleccione una ciudad: '),
                                   html.Br(),
                                   html.Div('Seleccione un tipo de mapa: '),
                                   html.Div(html.Br())
                                  ])

tab1 = dbc.Tab(tab_id='tab-demografia',
               id='tab-demografia',
               label='Datos demográficos')

tab2 = dbc.Tab(tab_id='tab-electoral',
               id='tab-electoral',
               label='Datos Electorales')

tab3 = dbc.Tab(tab_id='tab-comparativo',
               id='tab-comparativo',
               label='Datos Comparativos')



tabs = dbc.Tabs(children=[tab1,
                          tab2,
                          tab3,
                          html.Hr(),
                          html.Div(id='content-filters')],
                id='tabs-side',
                active_tab='tab-electoral'
                )
