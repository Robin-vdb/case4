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


#data
df2= pd.read_csv('df2')
df_scatterdata= pd.read_csv('df_scatterdata')
dfPROV= pd.read_csv('dfPROV')
dfPROV_totaal= pd.read_csv('dfPROV_totaal')


# In[3]:


#variable
jaartallen= ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']


# In[4]:


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


# In[12]:


fig4= px.scatter(dfPROV_totaal, x= '2021', y= 'Woontevredenheid', hover_data= {'index': dfPROV_totaal.index}, labels= {'2021': 'huizenprijs 2021 (€)'}, title= 'woontevredenheid tegenover huizenprijs (2021)', trendline= 'ols')


# In[6]:



fig = px.box(df2, y= jaartallen, points="outliers",labels= {'variable': 'jaartallen', 'value':'prijs huizen(€)'}, title= 'boxplot huizenprijs per jaar(€)')


# In[7]:


fig6= px.scatter(df_scatterdata, x='huurverhogin_exclusief_Huurharmonisatie', y='verkoopprijs (€)', color= 'RegioS', hover_data=['Perioden'], title= 'stijging huur tegenover stijging huizenprijs per provincie')


# In[8]:


fig5= px.scatter(df_scatterdata, x='huurverhoging', y='verkoopprijs (€)', color= 'RegioS', hover_data=['Perioden'], title= 'stijging huur tegenover stijging huizenprijs per provincie')


# In[9]:


#page_config
st.set_page_config(layout='wide')


# In[10]:


#row 1 (scatter's)
a1, a2 = st.columns((5,5))
with a1:
    st.markdown('scatterplots')
    st.plotly_chart(fig5)
with a2:
    st.plotly_chart(fig6)


# In[13]:


#row 2 (box + hist)
b1, b2 = st.columns((5,5))
with b1:
    st.markdown('### boxplot')
    st.plotly_chart(fig)
with b2:
    st.markdown('### histogram')
    st.plotly_chart(fig1)


# In[15]:


#row 3 (linear regression model)
c1, c2, c3= st.columns(3)
with c1:
    st.markdown('### linear regression')
    st.plotly_chart(fig4)
c2.dataframe(data= dfPROV_totaal)
c3.metric('jaar','2021')


# In[ ]:



