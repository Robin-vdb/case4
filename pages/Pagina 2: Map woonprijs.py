#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install cbsodata')
#get_ipython().system('pip install geopy')


import plotly.express as px
import pandas as pd
#import Seaborn as sb 
import cbsodata
import numpy as np
import streamlit_folium as st_folium
from streamlit_folium import folium_static
from folium import plugins
import streamlit as st

dfMarker = pd.read_csv('Markermap.csv')


import folium 
from folium import plugins

st.title('Gemiddelde verkoop map per jaar')
st.write('Op deze pagina wordt de dataset van woning prijzen door de jaren heen gevisualiseerd. Dit wordt gedaan in een folium map. Zo is er te zien dat deze map de gemiddelde verkoop prijzen van huizen per gemeente aantoont.')

#clustermap
m = folium.Map(location=[52.1009166, 5.6462914], tiles= None, zoom_start=7)
basemap = folium.FeatureGroup(name = 'basemap', overlay = True, control = False)
folium.TileLayer(tiles = 'OpenStreetMap').add_to(basemap)
basemap.add_to(m)


for i in range(1995,2022):
    globals()['%s' %i] = folium.plugins.MarkerCluster(name=str(i), control = True, overlay = False)
    m.add_child(globals()['%s' %i])        
    for index, row in dfMarker.iterrows():
        if str(row[str(i)]) != 'nan':
            popup = row['Regio'] + '\n' +str(row[str(i)])
            globals()['%s' %i].add_child(folium.Marker(location = [row['latitude'], row['longitude']], popup = popup)).add_to(m)


folium.LayerControl(position = 'bottomleft', collapsed = False).add_to(m)   

st_data = folium_static(m)




st.code('''m = folium.Map(location=[52.1009166, 5.6462914], tiles= None, zoom_start=7)
basemap = folium.FeatureGroup(name = 'basemap', overlay = True, control = False)
folium.TileLayer(tiles = 'OpenStreetMap').add_to(basemap)
basemap.add_to(m)

for i in range(1995,2022):
    globals()['%s' %i] = folium.plugins.MarkerCluster(name=str(i), control = True, overlay = False)
    m.add_child(globals()['%s' %i])        
    for index, row in dfMarker.iterrows():
        if str(row[str(i)]) != 'nan':
            popup = row['Regio'] + '\n' +str(row[str(i)])
            globals()['%s' %i].add_child(folium.Marker(location = [row['latitude'], row['longitude']], popup = popup)).add_to(m)

folium.LayerControl(position = 'bottomleft', collapsed = False).add_to(m)   

m''')
