from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go
import pandas as pd




# from figures_utils import (
#     get_figure,
# )
# from utils import (
#     get_employees_data,
#     get_svi_data
# )


app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color
# colors = {"background": "#1F2630", "text": "#7FDBFF"}

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

Arap_outline = gpd.read_file("/Users/jamesswank/Python_Projects/Arap_SVI_Dash/us-county-boundaries")

counties = [
    "Arapahoe"
]

# employees = get_employees_data()
# svi_data = get_svi_data()


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
    
    fig = go.Figure()
    # if fig is None:
    #     fig = go.Figure()
    df_SVI_2020 = pd.read_csv('/Users/jamesswank/Python_Projects/Situational_Awareness/appData/Colorado_SVI_2020.csv')
    df_SVI_2020['YEAR'] = 2020
    df = df_SVI_2020
    df['FIPS'] = df['FIPS'].astype(str)

    gdf_2020 = gpd.read_file('2020_CT/ArapahoeCT.shp')
    geo_data = gdf_2020.merge(df, on='FIPS')
    geo_data = geo_data.set_index('FIPS')

    fig.add_trace(
        go.Choroplethmapbox(
            geojson = eval(geo_data['geometry'].to_json()),
            locations = geo_data.index,
            # featureidkey = "properties.name",
            # colorscale = arg['colorscale'],
            colorscale = "earth",
            # z = arg['z_vec'],
            z = geo_data['E_TOTPOP'],
            # zmin = arg['min_value'],
            # zmax = arg['max_value'],
            # text = arg['text_vec'],
            # hoverinfo="text",
            # marker_opacity = marker_opacity,
            # marker_line_width = marker_line_width,
            # marker_line_color = marker_line_color,
            # # colorbar_title = arg['title'],
        )
    )

    fig.update_layout(mapbox_style="open-street-map",
                    #   mapbox_zoom=_cfg['zoom'],
                      autosize=True,
                      font=dict(color="#7FDBFF"),
                      paper_bgcolor="#1f2630",
                    #   mapbox_center = {"lat": _cfg['center'][0] , "lon": _cfg['center'][1]},
                    #   uirevision=county,
                      margin={"r":0,"t":0,"l":0,"b":0}
                     )
    
    return fig

   


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)