from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go



app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

bgcolor = "#f3f3f1"  # mapbox light map land color

header = html.Div("Arapahoe Situational Awareness", className="h2 p-2 text-white bg-primary text-center")

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

Arap_outline = gpd.read_file("/Users/jamesswank/Python_Projects/Arap_SVI_Dash/us-county-boundaries")




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
            dcc.Dropdown(
                id='variable-dropdown',
            ),
        ], width=2)
    ])
])

@app.callback(
    Output('ct-map', 'figure'),
    # Input('year-map-data', 'data'),
    Input('variable-dropdown', 'value'),
    # Input('year', 'value'),
    # Input('opacity', 'value')
)
def get_figure(dropdown):
  
    # df = pd.read_json(selected_data)
    # # df['FIPS'] = df["FIPS"].astype(str)
    # # df = df_SVI_2016
    # df['FIPS'] = df["FIPS"].astype(str)
    
    # selection = dropdown
    
    # if year == 2016:
    #     tgdf = gdf_2016.merge(df, on='FIPS')
    # elif year == 2018:
    #     tgdf = gdf_2018.merge(df, on='FIPS')
    # else:
    #     tgdf = gdf_2020.merge(df, on='FIPS')
    # tgdf = tgdf.set_index('FIPS')

    fig = go.Figure(go.Scattermapbox(
            mode = "markers",
            lon = [-73.605], lat = [45.51],
            # showlegend=True
            ))
  

    # fig = px.choropleth_mapbox(tgdf, 
    #                             geojson=tgdf.geometry, 
    #                             color=selection,                               
    #                             locations=tgdf.index, 
    #                             # featureidkey="properties.TRACTCE20",
    #                             opacity=opacity)

    layer = [
        {
            "source": Arap_outline["geometry"].__geo_interface__,
            "type": "line",
            "color": "black"
        }
    ]

    fig.update_layout(mapbox_style="carto-positron", 
                      mapbox_zoom=10.4,
                      mapbox_layers=layer,
                      mapbox_center={"lat": 39.65, "lon": -104.8},
                      margin={"r":0,"t":0,"l":0,"b":0},
                      uirevision='constant')


    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=8080)