#!/usr/bin/env python
# coding: utf-8

# # final version va-eindpresentatie

# In[14]:


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


# In[4]:


data = cbsodata.get_data('83625NED')
data3= cbsodata.get_data('83162NED')
data2= cbsodata.get_data('84571NED')


# In[ ]:


df1 = pd.DataFrame(data)


# In[ ]:



jaartallen2= ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
dfhuizen= df1.loc[df1['RegioS'].str.contains('(PV)')]
dfhuizen= dfhuizen.rename(columns= {'HuurverhogingInclusiefHuurharmonisatie_1': 'huurverhoging'}, index= {'Fryslân (PV)': 'Friesland (PV)'})
dfhuizen= dfhuizen.loc[dfhuizen['Perioden'].isin(['2015', '2016', '2017', '2018', '2019', '2020', '2021'])]

df_tevredenheid= pd.DataFrame(data2)
df_tevredenheid= df_tevredenheid.rename(columns={'Regio': 'RegioS'})
df_tevredenheid= df_tevredenheid.set_index('RegioS')
df_tevredenheid= df_tevredenheid.drop(columns= ['ID','TevredenheidMetDeHuidigeWoonomgeving_2'])

dftotaal = df_tevredenheid.loc[df_tevredenheid['EigenaarOfHuurder'] == 'Totaal']
dftotaal2 = dftotaal.loc[dftotaal['Perioden']== '2021']
dftotaal3 = dftotaal2.loc[dftotaal2['Woningkenmerken']== 'Totaal woningen']
dftotaal4 = dftotaal3.loc[dftotaal3['Marges'] == 'Waarde']

dfPROV_tevredenheid= dftotaal4.filter(like='(PV)', axis=0)
dfPROV_tevredenheid2= dfPROV_tevredenheid.rename(columns= {'TevredenheidMetDeHuidigeWoning_1' : 'Woontevredenheid'})

df2 = df1.pivot(index='RegioS', columns='Perioden', values='GemiddeldeVerkoopprijs_1')            .reset_index()
df2.columns.name=None

dfPROV = df2.loc[df2['RegioS'].str.contains("(PV)")]
dfPROV2= dfPROV.set_index('RegioS')
dfPROV3 = dfPROV2.rename(index= {'Fryslân (PV)': 'Friesland (PV)'})

dfPROV_totaal= dfPROV3.merge(dfPROV_tevredenheid2, on= 'RegioS',how= 'outer')

dfGEM = df2.drop([164,201,203,207,236,359,446,447,448,473,494,618,676,715,462,727,728])
dfGEM = dfGEM.set_index('RegioS')

df_huur= pd.DataFrame(data3)
df_huur= df_huur.loc[df_huur['RegioS'].str.contains('(PV)')]
df_huur= df_huur.rename(columns= {'HuurverhogingInclusiefHuurharmonisatie_1': 'huurverhoging', 'HuurverhogingExclusiefHuurharmonisatie_2': 'huurverhogin_exclusief_Huurharmonisatie'}, index= {'Fryslân (PV)': 'Friesland (PV)'})

df_scatterdata= dfhuizen.merge(df_huur, how= 'inner', on= ['Perioden', 'RegioS'])
df_scatterdata= df_scatterdata.rename(columns={'GemiddeldeVerkoopprijs_1': 'verkoopprijs (€)',})
df_scatterdata= df_scatterdata.drop(columns= ['ID_x', 'ID_y'])


# # code

# In[ ]:


st.title('Huizenmarkt van Nederland')
st.image('huizenmarktplaatje.jpg')
st.markdown('### api')
st.code('''data = cbsodata.get_data('83625NED')
data3= cbsodata.get_data('83162NED') 
data2= cbsodata.get_data('84571NED')''',language= 'python')
st.dataframe(df1)


# In[ ]:


st.markdown('### opschonen data')
st.code('''jaartallen2= ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
dfhuizen= df1.loc[df1['RegioS'].str.contains('(PV)')]
dfhuizen= dfhuizen.rename(columns= {'HuurverhogingInclusiefHuurharmonisatie_1': 'huurverhoging'}, index= {'Fryslân (PV)': 'Friesland (PV)'})
dfhuizen= dfhuizen.loc[dfhuizen['Perioden'].isin(['2015', '2016', '2017', '2018', '2019', '2020', '2021'])]

df_tevredenheid= pd.DataFrame(data2)
df_tevredenheid= df_tevredenheid.rename(columns={'Regio': 'RegioS'})
df_tevredenheid= df_tevredenheid.set_index('RegioS')
df_tevredenheid= df_tevredenheid.drop(columns= ['ID','TevredenheidMetDeHuidigeWoonomgeving_2'])

dftotaal = df_tevredenheid.loc[df_tevredenheid['EigenaarOfHuurder'] == 'Totaal']
dftotaal2 = dftotaal.loc[dftotaal['Perioden']== '2021']
dftotaal3 = dftotaal2.loc[dftotaal2['Woningkenmerken']== 'Totaal woningen']
dftotaal4 = dftotaal3.loc[dftotaal3['Marges'] == 'Waarde']

dfPROV_tevredenheid= dftotaal4.filter(like='(PV)', axis=0)
dfPROV_tevredenheid2= dfPROV_tevredenheid.rename(columns= {'TevredenheidMetDeHuidigeWoning_1' : 'Woontevredenheid'})

df2 = df1.pivot(index='RegioS', columns='Perioden', values='GemiddeldeVerkoopprijs_1')\
            .reset_index()
df2.columns.name=None

dfPROV = df2.loc[df2['RegioS'].str.contains("(PV)")]
dfPROV2= dfPROV.set_index('RegioS')
dfPROV3 = dfPROV2.rename(index= {'Fryslân (PV)': 'Friesland (PV)'})

dfPROV_totaal= dfPROV3.merge(dfPROV_tevredenheid2, on= 'RegioS',how= 'outer')

dfGEM = df2.drop([164,201,203,207,236,359,446,447,448,473,494,618,676,715,462,727,728])
dfGEM = dfGEM.set_index('RegioS')

df_huur= pd.DataFrame(data3)
df_huur= df_huur.loc[df_huur['RegioS'].str.contains('(PV)')]
df_huur= df_huur.rename(columns= {'HuurverhogingInclusiefHuurharmonisatie_1': 'huurverhoging', 'HuurverhogingExclusiefHuurharmonisatie_2': 'huurverhogin_exclusief_Huurharmonisatie'}, index= {'Fryslân (PV)': 'Friesland (PV)'})

df_scatterdata= dfhuizen.merge(df_huur, how= 'inner', on= ['Perioden', 'RegioS'])
df_scatterdata= df_scatterdata.rename(columns={'GemiddeldeVerkoopprijs_1': 'verkoopprijs (€)',})
df_scatterdata= df_scatterdata.drop(columns= ['ID_x', 'ID_y'])''')


# In[ ]:


st.markdown('### resultaat (voorbeelden)')
col1, col2 = st.columns((5,5))
col1.dataframe(df_scatterdata)
col2.dataframe(dfPROV_totaal)
st.dataframe(df2)


# # plots
# 

# In[10]:


st.markdown('### plots')
jaartallen= ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
fig = px.box(df2, y= jaartallen, points="outliers",labels= {'variable': 'jaartallen', 'value':'prijs huizen(€)'}, title= 'boxplot huizenprijs per jaar(€)')
st.plotly_chart(fig, use_container_width= True)


# In[9]:


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
st.plotly_chart(fig1, use_container_width= True)


# In[11]:


fig4= px.scatter(dfPROV_totaal, x= '2021', y= 'Woontevredenheid', hover_data= {'index': dfPROV_totaal.index}, labels= {'2021': 'huizenprijs 2021 (€)'}, title= 'woontevredenheid tegenover huizenprijs (2021)', trendline= 'ols')
st.plotly_chart(fig4, use_container_width= True)


# In[12]:


fig5= px.scatter(df_scatterdata, x='huurverhoging', y='verkoopprijs (€)', color= 'RegioS', hover_data=['Perioden'], title= 'stijging huur tegenover stijging huizenprijs per provincie')
st.plotly_chart(fig5, use_container_widt= True)


# In[13]:


fig6= px.scatter(df_scatterdata, x='huurverhogin_exclusief_Huurharmonisatie', y='verkoopprijs (€)', color= 'RegioS', hover_data=['Perioden'], title= 'stijging huur tegenover stijging huizenprijs per provincie')
st.plotly_chart(fig6, use_container_width= True)


# In[ ]:




