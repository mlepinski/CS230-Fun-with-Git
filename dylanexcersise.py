import folium
map = folium.Map(
    location=[50.50, 57.57],
    zoom_start=10, 
    tiles="OpenStreetMap"
)
#folium.TileLayer("OpenStreetMap").add_to(map)
fg = folium.FeatureGroup(name="Mymap")
fg.add_child(folium.Marker(location=[31.481889,-83.528281], popup="Abraham Baldwin Agricultural College", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[57.57, 50.50], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map2.html")
