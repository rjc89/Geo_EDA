import pandas as pd
import streamlit as st
import plotly.express as px
# import plotly.graph_objects as go
# import json



st.title('Geo_EDA')
st.write('https://github.com/rjc89/Geo_EDA')
example_data = st.checkbox('Use example .csv')

#uploaded_file = st.file_uploader("Choose a dataset .csv", type="csv")
#us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
#if uploaded_file:
#data = pd.read_csv(uploaded_file)
if example_data:
    data = pd.read_csv("./us_cities_top_1k.csv")
st.write(data.head(3))

cols = list(data.columns)

# GeoJSON = st.sidebar.file_uploader('Choose a GeoJSON')
# locations = st.sidebar.selectbox('Choose a chloropleth color column', cols)
#marker_color = st.sidebar.slider('marker color', )
marker_size = st.sidebar.selectbox('marker size', cols)
latitude = st.sidebar.selectbox('latitude', cols)
longitude = st.sidebar.selectbox('longitude', cols)
hover = st.sidebar.selectbox('hover label', cols)
#hover_data = st.sidebar.multiselect('hover', cols)
terrain = st.sidebar.checkbox('Terrain')

#GeoJSON_data = json.load(GeoJSON)

if terrain:
    style = 'stamen-terrain'
else:
    style = "open-street-map"

layers = []

weather = {
                "sourcetype": "raster",
                "source": ["https://geo.weather.gc.ca/geomet/?"
                        "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                        "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
            }

USGS = {
                "below": 'traces',
                "sourcetype": "raster",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
USGS_box = st.sidebar.checkbox("USGS")
Weather_box = st.sidebar.checkbox("Weather")

if USGS_box:
    layers.append(USGS)
if Weather_box:
    layers.append(weather)

def plotly_ex_map(data, style, layers, latitude, longitude, hover, marker_size):
    fig = px.scatter_mapbox(data, lat=latitude, lon=longitude, hover_name=hover, 
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300, size = marker_size)
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers= layers)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(mapbox_style=style)
    return fig

if example_data:
    st.plotly_chart(plotly_ex_map(data, style, layers, data['lat'], data['lon'], data['City'], data['Population']))
else:
    st.plotly_chart(plotly_ex_map(data, style, layers, data[latitude], data[longitude], data[hover], data[marker_size]))

