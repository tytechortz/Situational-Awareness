import plotly.graph_objs as go
import plotly.express as px
import numpy as np



def get_scattergeo(df):
    fig = go.Figure()
    fig.add_trace(
        px.scatter_mapbox(df,
                          lat="Latitude", lon="Longitude",
                          color="Best Rank",
                          # color_discrete_sequence=['White'],
                          size=np.ones(len(df)),
                          size_max=8,
                          opacity=1
        ).data[0]
    )
    fig.update_traces(hovertemplate=df['Info'])

    return fig