import folium
import pandas

data = pandas.read_csv ("points/Volcanoes.txt")  # reading the file
lat = list (data["LAT"])
lon = list (data["LON"])  # creating variables to get the values in the particular columns
info = list (data["ELEV"])

map = folium.Map (location=[38.58, -99.09], max_zoom=18, tiles="Stamen Terrain")

fg = folium.FeatureGroup (name="my map")

for lt, ln, inf in zip (lat, lon, info):  # zip function reads the values simunteneously
    fg.add_child (folium.Marker (location=[lt, ln],
                                 popup=str (inf) + "m", icon=folium.Icon (color='red')))

map.add_child (fg)

map.save ("simple.html")
