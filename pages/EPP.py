#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install cbsodata')
get_ipython().system('pip install geopy')


# In[2]:


import plotly.express as px
import pandas as pd
#import Seaborn as sb 
import cbsodata
import numpy as np


# In[3]:


data = cbsodata.get_data('83625NED')
pd.set_option('display.float_format', lambda x: ('%f' % x).rstrip('0'))


# In[4]:


df1 = pd.DataFrame(data)
df1


# In[ ]:





# In[5]:


df2 = df1.pivot(index='RegioS', columns='Perioden', values='GemiddeldeVerkoopprijs_1')            .reset_index()
df2.columns.name=None
df2


# In[6]:


df2=df2.rename(columns={'RegioS': 'Regio'})
df2


# In[ ]:





# In[ ]:





# In[7]:


from geopy.geocoders import Nominatim

adressen= pd.DataFrame(df2.Regio.unique())
geolocator = Nominatim(user_agent="robbbin")
longitude= []
latitude= []
Adres= adressen[0]

for i in range(len(adressen)):
    loc= geolocator.geocode(Adres[i], timeout= 10)
    if loc is None:
        latitude.append(None)
        longitude.append(None)
       
    else:
            latitude.append(loc.latitude)
            longitude.append(loc.longitude)
adressen['latitude']= latitude
adressen['longitude']= longitude
adressen


# In[8]:


adressen1= adressen.rename(columns={0: 'Regio'})
adressen1

dfLOC= df2.merge(adressen1, on= 'Regio', how='outer')
dfLAT = dfLOC[dfLOC['latitude'].notna()]
dfLAT


# In[9]:


dfNL = dfLOC.loc[dfLOC['Regio'] == 'Nederland']
dfNL


# In[10]:


dfLD = dfLOC.loc[dfLOC['Regio'].str.contains("(LD)")]
dfLD


# In[11]:


dfPROV = dfLOC.loc[dfLOC['Regio'].str.contains("(PV)")]
dfPROV


# In[ ]:





# In[12]:


dfGEM = dfLOC.drop([7,23,92,95,100,125,164,196,201,203,207,236,253,255,257,275,304,319,339,359,364,386,389,402,416,446,447,448,462,473,494,503,507,526,573,605,618,676,685,686,715,700,727,728],axis=0, inplace=True)
#dfGEM.drop([23,100], axis=0)
dfGEM= dfLOC[dfLOC['latitude'].notna()]
dfGEM


# In[ ]:





# In[13]:


import folium 
from folium import plugins


# In[14]:


m = folium.Map(location=[52.1009166, 5.6462914], tiles="Stamen Terrain", zoom_start=7)
for i, row in dfGEM.iterrows():
    location = [row['latitude'],row['longitude']]
    popup = row['Regio'], row['1995']
    marker = folium.Marker(location = location, popup = popup)
    marker.add_to(m)
m


# In[15]:


dfLOC.loc[dfLOC['Regio'].str.contains("Borne")]


# In[16]:


m = folium.Map(location=[52.1009166, 5.6462914], tiles= None, zoom_start=7)
basemap = folium.FeatureGroup(name = 'basemap', overlay = True, control = False)
folium.TileLayer(tiles = 'OpenStreetMap').add_to(basemap)
basemap.add_to(m)

# Om het jaar te selecteren, hier alvast wat tips:
# Maak per jaar folium featuregroups aan

for i in range(1995,2022):
    globals()['%s' %i] = folium.FeatureGroup(name=i, control = True, overlay = False)
    m.add_child(globals()['%s' %i])        
    for index, row in dfGEM.iterrows():
        if str(row[str(i)]) != 'nan':
            popup = row['Regio'] + '\n' +str(row[str(i)])
            globals()['%s' %i].add_child(folium.Marker(location = [row['latitude'], row['longitude']], popup = popup)).add_to(m)

folium.LayerControl(position = 'bottomleft', collapsed = False).add_to(m)   

m


# In[17]:


str(dfGEM['2014'][0]) != 'nan'


# In[18]:


dfGEM['latitude'][0]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




