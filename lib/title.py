import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State



title = html.H1(id='div-title',
                  children='Dashboard de análisis demográfico y electoral',
                  className='dash-title')