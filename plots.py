import plotly.express as px


def plotly_ex_map(data, style, layers):
    fig = px.scatter_mapbox(data, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers= layers)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(mapbox_style=style)
    return fig
