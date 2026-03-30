import folium
import webbrowser
import os

# Location
latitude = 14.7526
longitude = 78.5541

m = folium.Map(
    location=[latitude, longitude],
    zoom_start=13,
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri Satellite'
)

# Add marker
folium.Marker(
    [latitude, longitude],
    popup="Satellite View - Pollution Area",
    icon=folium.Icon(color="green")
).add_to(m)

# Save & open
file_path = os.path.abspath("satellite_map.html")
m.save(file_path)

webbrowser.open(file_path)
