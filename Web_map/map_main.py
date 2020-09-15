import folium
import pandas


data = pandas.read_csv ("points/Volcanoes.txt")  # reading the file
lat = list (data["LAT"])          #}
lon = list (data["LON"])          #}  # creating variables to get the values in the perticular colomns
elv = list (data["ELEV"])         #}

html = """<h5>Volcano information:</h5>
Height: %s m
"""


def color_produce(elevation):
    if elevation < 1000:
        return "lightgreen"
    elif 1000 <= elevation < 2000:
        return "green"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


mymap = folium.Map (location=[38.58, -99.09], max_zoom=18,)

fgv = folium.FeatureGroup (name="points/Volcanoes")  #adding secific feature group for volcanoes.

for lt, ln, el in zip (lat, lon, elv):  # zip function reads the values simultaneously
    iframe = folium.IFrame (html=html % str (el), width="180px", height=100)
    fgv.add_child (folium.CircleMarker (location=[lt, ln], radius=6,
    popup=folium.Popup (iframe), color="grey", fill_color=(color_produce (el)),
    fill_opacity=0.8))

fgp = folium.FeatureGroup (name="Population") #adding secific feature group for population.

fgp.add_child(folium.GeoJson(data=open("points/world.json","r",encoding="utf-8-sig").read(),        #reading the json file using "geojson"
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']< 10000000
else 'orange' if 20000000 <= x ['properties']['POP2005']<=30000000 else 'red',}))

mymap.add_child (fgv)
mymap.add_child(fgp)

mymap.add_child(folium.LayerControl())    # layer control funtion controls the different layers of the map.
 
mymap.save ("mymap.html")
