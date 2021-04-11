import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np

from lib import body, sections, sidebar, title
from app import app


app.layout = html.Div([title.title,
                       sidebar.sidebar,
                       body.body
                      ],
                      className='dash-app',
                      )
                        

#####CALLBACKS SECTION####

@app.callback(Output("div-filtros", "children"),
              [Input("tabs-side", "active_tab")])
def update_filters(at):
    if at == 'tab-demografia':
        return [html.H4('Filtros', className='display-5'),
                body.section_demog]
    elif at =='tab-electoral':
        return [html.H4('Filtros', className='display-5'),
                body.section_elect]
    else:
        return [html.Div('seleccione')]



@app.callback(Output("iframe-body","src"),
              [Input("btn-demog", "n_clicks")],
              [State("radio-mapa", 'value')])
def update_map(nclicks,map_kind):
    if nclicks == 0:
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Meta_in_Colombia_%28mainland%29.svg/800px-Meta_in_Colombia_%28mainland%29.svg.png"
    else:

        if map_kind == 'estrato':
            return "assets/mapa_estrato.html"
        elif map_kind == 'educacion':
            return "assets/mapa_educacion_mas_alta.html"
        else:
            return "assets/mapa_porcentaje_internet.html"





if __name__ == '__main__':
    app.run_server('0.0.0.0', debug=True)
