import pandas as pd
import streamlit as st
import plotly.express as px
from plots import plotly_ex_map

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

st.title('Geo_EDA')
st.write(us_cities.head())

Sat_street = st.sidebar.checkbox("satellite-streets")

if Sat_street:
    style = "satellite-streets"
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

st.plotly_chart(plotly_ex_map(us_cities, style, layers))





# [
#             {
#                 "below": 'traces',
#                 "sourcetype": "raster",
#                 "source": [
#                     "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
#                 ]
#             },
#             {
#                 "sourcetype": "raster",
#                 "source": ["https://geo.weather.gc.ca/geomet/?"
#                         "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
#                         "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
#             }
#         ]