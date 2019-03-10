
# coding: utf-8

# In[123]:


import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library


# In[124]:


df_datascience=pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/coursera/Topic_Survey_Assignment.csv',
                          index_col=0)


# In[125]:


df_datascience


# In[126]:


get_ipython().magic(u'matplotlib inline')

import matplotlib as mpl
import matplotlib.pyplot as plt


# In[127]:


df_datascience.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)


# In[128]:


df_datascience['Very interested'] = df_datascience['Very interested']/2233
df_datascience['Somewhat interested'] = df_datascience['Somewhat interested']/2233
df_datascience['Not interested'] = df_datascience['Not interested']/2233


# In[129]:


df_datascience.style.format({
    'Very interested': '{:,.2%}'.format,
    'Somewhat interested': '{:,.2%}'.format,
    'Not interested': '{:,.2%}'.format,
})


# In[130]:


# step 2: plot data
ax=df_datascience.plot(kind='bar', 
                    figsize=(20, 8),
                    color=['#5cb85c', '#5bc0de', '#d9534f'],
                    fontsize=12,
                   )
ax.spines['top'].set_visible(False) #removes borders
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.get_yaxis().set_ticks([]) #removes values on y axis

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.annotate('{:.0%}'.format(height), (p.get_x()+.15*width, p.get_y() + height + 0.01))

plt.title('Percentage of respondents'' interest in data science area',fontsize=14) # add title to the plot

plt.show()


# In[131]:


df_crime = pd.read_csv('https://cocl.us/sanfran_crime_dataset')

print('Dataset downloaded and read into a pandas dataframe!')


# In[132]:


df_crime.head()


# In[133]:


df_crime.columns


# In[134]:


df_crime.shape


# In[135]:


df_crime.drop(['IncidntNum', 'Category', 'Descript', 'DayOfWeek', 'Date', 'Time'
       , 'Resolution', 'Address', 'X', 'Y', 'Location', 'PdId'], axis=1, inplace=True)
df_crime.head()


# In[136]:


df_crime=df_crime.groupby(["PdDistrict"])["PdDistrict"].count().reset_index(name="Count")


# In[137]:


df_crime.rename(columns={df_crime.columns[0]:'Neighborhood'}, inplace=True)
df_crime


# In[138]:


get_ipython().system(u'conda install -c conda-forge folium=0.5.0 --yes')
import folium

print('Folium installed and imported!')


# In[139]:


# download San Fran geojson file
get_ipython().system(u'wget --quiet https://cocl.us/sanfran_geojson -O sanfran.json')
    
print('GeoJSON file downloaded!')


# In[148]:


sanfran_geo = 'sanfran.json' # geojson file

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42

# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)

# display the map of San Francisco
sanfran_map


# In[149]:


# generate choropleth map
sanfran_map.choropleth(
    geo_data=sanfran_geo,
    data=df_crime,
    columns=['Neighborhood','Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime rate in San Francisco',
)

# display map
sanfran_map

