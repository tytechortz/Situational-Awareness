from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go




from figures_utils import (
    get_figure,
)
from utils import (
    get_employees_data,
    get_svi_data
)


app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color
# colors = {"background": "#1F2630", "text": "#7FDBFF"}

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

Arap_outline = gpd.read_file("/Users/jamesswank/Python_Projects/Arap_SVI_Dash/us-county-boundaries")

counties = [
    "Arapahoe"
]

employees = get_employees_data()
svi_data = get_svi_data()


def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }

app.layout = dbc.Container([
    header,
    dbc.Row(dcc.Graph(id='ct-map', figure=blank_fig(500))),
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                id='graph-type',
                options=[
                    {"label": i, "value": i}
                    for i in ["Pop", "Density"]
                ],
                value="Pop",
                inline=True
            ),
        ], width=2)
    ])
])

@app.callback(
    Output('ct-map', 'figure'),
    Input('graph-type', 'value'),
)
def update_Chropleth(gtype):
    print(gtype)
    # if gtype in ['Pop', 'Density']:
    df = svi_data
    df['FIPS'] = df['FIPS'].astype(str)
    # print(df)
    # gtype = "Pop"
    # county = "Arapahoe"

    


    # changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
   
    # selected_tracts = dict()
   
    fig = get_figure(df)
    

  
    return fig

   


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)