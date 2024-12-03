import folium

# Define the center of the map
map_center =[44.4783, 25.8882]

# Create the map
mymap = folium.Map(location=map_center, zoom_start=15)

# Add a marker to the map
folium.Marker(
[52.5200, 13.4050],
popup="Berlin",
icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mymap)

# Display the map
mymap.save("map.html")

