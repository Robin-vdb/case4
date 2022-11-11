#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
#import Seaborn as sns 
import cbsodata
import folium
from plotly.subplots import make_subplots
import statsmodels as sm 
#import statsmodels.formula.api as smf
import streamlit as st


# In[2]:

df2= pd.read_csv('df2')
dfPROV= pd.read_csv('dfPROV')
dfPROV_totaal= pd.read_csv('dfPROV_totaal', index_col= 'RegioS')
df_scatterdata= pd.read_csv('df_scatterdata')


# In[ ]:





# In[5]:


#variable
jaartallen= ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']


# In[6]:


fig1= px.histogram(dfPROV, x= 'RegioS', y= jaartallen, title= 'verhoging van huizenwaarde per provincie', labels= {'RegioS': 'Provincies', 'sum of value': 'waarde woning (€)'})
fig1.update_layout(updatemenus= [dict(active=0, buttons=list([dict(label= 'alles'
                                                                   ,method= 'update',
                                                                   args=[{'visible': [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,True]},
                                                                         {'showlegend': True}]),
                                                              dict(label="1995",method="update",args=[{"visible": [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="1996",method="update",args=[{"visible": [False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="1997",method="update",args=[{"visible": [False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="1998",method="update",args=[{"visible": [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="1999",method="update",args=[{"visible": [False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2000",method="update",args=[{"visible": [False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2001",method="update",args=[{"visible": [False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2002",method="update",args=[{"visible": [False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2003",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2004",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2005",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2006",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2007",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2008",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2009",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2010",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2011",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2012",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2013",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,False, False]}]),
                                                             dict(label="2014",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False,False, False]}]),
                                                             dict(label="2015",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False,False, False]}]),
                                                             dict(label="2016",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False,False, False]}]),
                                                             dict(label="2017",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False,False, False]}]),
                                                             dict(label="2018",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False,False, False]}]),
                                                             dict(label="2019",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,False, False]}]),
                                                             dict(label="2020",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,True, False]}]),
                                                             dict(label="2021",method="update",args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,False, True]}]),
                                                             ]))])


# In[7]:

fig4= px.scatter(dfPROV_totaal, x= '2021', y= 'Woontevredenheid', hover_data= {'index': dfPROV_totaal.index}, labels= {'2021': 'huizenprijs 2021 (€)'}, title= 'woontevredenheid tegenover huizenprijs (2021)', trendline= 'ols')


# In[8]:



fig = px.box(df2, y= jaartallen, points="outliers",labels= {'variable': 'jaartallen', 'value':'prijs huizen(€)'}, title= 'boxplot huizenprijs per jaar(€)')


# In[9]:


fig6= px.scatter(df_scatterdata, x='huurverhogin_exclusief_Huurharmonisatie', y='verkoopprijs (€)', color= 'RegioS', hover_data=['Perioden'], title= 'stijging huur tegenover stijging huizenprijs per provincie')


# In[10]:


fig5= px.scatter(df_scatterdata, x='huurverhoging', y='verkoopprijs (€)', color= 'RegioS', hover_data=['Perioden'], title= 'stijging huur tegenover stijging huizenprijs per provincie')


# In[11]:


#page_config
st.set_page_config(layout='wide')


# In[15]:

st.markdown('### Dashboard huizenprijs')

#row 1 (scatter's)
a1, a2 = st.columns((4,6))
with a1:
    
    st.plotly_chart(fig5)
with a2:
    st.plotly_chart(fig6)


# In[13]:


#row 2 (box + hist)
b1, b2 = st.columns((5,5))
with b1:
    st.plotly_chart(fig)
with b2:
    st.plotly_chart(fig1)


# In[14]:


#row 3 (linear regression model)
c1, c2= st.columns((7,3))
with c1:
    st.plotly_chart(fig4)
with c2:
  st.markdown('### bronnenlijst')
  st.write('CBS Statline. (n.d.). Retrieved November 4, 2022, from https://opendata.cbs.nl/statline/,  Va-eindpresentatie. (2022, November 3). Github. https://github.com/Robin-vdb/case4, Stack Overflow - Where Developers Learn, Share, & Build Careers. (n.d.). Stack Overflow. https://stackoverflow.com/')
  


# In[ ]:
