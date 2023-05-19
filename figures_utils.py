import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd
from config import config as cfg

# df = svi_data





# print(geo_data)

def get_scattergeo(df):
    fig = go.Figure()
    fig.add_trace(
        px.scatter_mapbox(df,
                          lat="Latitude", lon="Longitude"
        ).data[0]
    )
    fig.update_traces(hovertemplate=df['Name'])

    return fig

def get_Choropleth(df, arg, marker_opacity,
                   marker_line_width, marker_line_color, fig=None):

    if fig is None:
        fig = go.Figure()

    gdf_2020 = gpd.read_file('2020_CT/ArapahoeCT.shp')
    geo_data = gdf_2020.merge(df, on='FIPS')
    geo_data = geo_data.set_index('FIPS')


    fig.add_trace(
            go.Choroplethmapbox(
                geojson = geo_data,
                locations = geo_data.index,
                featureidkey = "properties.name",
                colorscale = arg['colorscale'],
                z = arg['z_vec'],
                # zmin = arg['min_value'],
                # zmax = arg['max_value'],
                # text = arg['text_vec'],
                hoverinfo="text",
                marker_opacity = marker_opacity,
                marker_line_width = marker_line_width,
                marker_line_color = marker_line_color,
                # colorbar_title = arg['title'],
          )
    )
    
    return fig


def get_figure(df):
    config = {'doubleClickDelay': 1000} #Set a high delay to make double click easier

    _cfg = cfg['plotly_config']["Arapahoe"]

    arg = dict()
    # if gtype == 'Pop':
    arg['z_vec'] = df['E_TOTPOP']
    arg['colorscale'] = "earth"
    # print(arg)

    county = "Arapahoe"
    dtype = "Pop"



    
    fig = get_Choropleth(df, arg, marker_opacity=0.4,
                         marker_line_width=1, marker_line_color='#6666cc')
    
    # if len(employees) > 0:
    #     fig.update_traces(showscale=False)
    #     employee_fig = get_scattergeo(employee_locations)
    #     fig.add_trace(employee_fig.data[0])

    fig.update_layout(mapbox_style="open-street-map",
                      mapbox_zoom=_cfg['zoom'],
                      autosize=True,
                      font=dict(color="#7FDBFF"),
                      paper_bgcolor="#1f2630",
                      mapbox_center = {"lat": _cfg['center'][0] , "lon": _cfg['center'][1]},
                    #   uirevision=county,
                      margin={"r":0,"t":0,"l":0,"b":0}
                     )
    
    #-------------------------------------------#
    # Highlight selections:
    # if geo_sectors is not None and len(employees)==0:
    #     fig = get_Choropleth(df, geo_sectors, arg, marker_opacity=1.0,
    #                          marker_line_width=3, marker_line_color='aqua', fig=fig)
    

    return fig






