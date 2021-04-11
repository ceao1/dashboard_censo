import dash
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

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
                          ],
                id='tabs-side',
                active_tab='tab-demografia'
                )


sidebar = html.Div(
    [   html.H4("Escoja qué información desea ver", className='display-10'),
        html.Hr(),
        tabs
        
    ],
    className='dash-sidebar',
    id='sidebar-id'
)