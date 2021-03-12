#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import plotly.express as px


# In[2]:


st.title("Locations of Earthquakes off Fiji")
st.markdown('The data set give the locations of 1000 seismic events of MB > 4.0. The events occurred in a cube near Fiji since 1964.')


# In[3]:


st.subheader("Details")
st.markdown('There are two clear planes of seismic activity. One is a major plate junction; the other is the Tonga trench off New Zealand. These data constitute a subsample from a larger dataset of containing 5000 observations.')


# In[4]:


st.subheader("Format")
st.markdown('A data frame with 1000 observations on 5 variables.')
st.markdown('lat - Latitude of event, long - Longitude, depth - Depth (km), mag - Richter Magnitude')


# In[5]:


st.subheader("Import Data")


# In[6]:


df = pd.read_csv("quakes.csv")


# In[7]:


df


# In[8]:


st.text("---" * 100)


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


df.stations.unique()


# In[12]:


st.subheader("Data Preparation")


# In[13]:


statscount = df.groupby("stations").count()
statscount


# In[14]:


st.subheader("Grouping by Stations")


# In[15]:


statscount.reset_index(inplace=True)
statscount


# In[16]:


st.subheader("Grouping by Top 10 Stations")


# In[17]:


statscount2 = statscount.nlargest(10, columns="lat")


# In[18]:


statscount2


# In[19]:


st.text("---" * 100)


# In[20]:


st.subheader("Line Chart")


# In[21]:


st.line_chart(df[["depth","mag"]])


# In[22]:


st.text("---" * 100)


# In[23]:


st.subheader("Pie Chart")


# In[24]:


fig = px.pie(data_frame=statscount2, labels=statscount2.stations, values=statscount2.lat, 
      title="Top 10 Stations", names=statscount2.stations, hole=0.5)

fig.show()


# In[25]:


st.plotly_chart(fig)


# In[26]:


st.text("---" * 100)


# In[27]:


st.subheader("Bar Chart")


# In[28]:


st.subheader("Grouping by Stations with Mean values")


# In[29]:


meanquakes = df.groupby("stations").mean()
meanquakes


# In[30]:


fig = px.bar(data_frame=meanquakes, x=meanquakes.index, y=meanquakes.mag, title="Mean Quakes detected per Station")
fig.show()


# In[31]:


st.plotly_chart(fig)


# In[32]:


st.text("---" * 100)


# In[33]:


st.subheader("Scatterplot Chart")


# In[34]:


fig = px.scatter(data_frame=meanquakes,x=meanquakes.depth, y=meanquakes.mag, color=meanquakes.index,
           hover_name=meanquakes.index,
           title="Scatterplot of Magnitude vs Depth by Stations")

fig.show()


# In[35]:


st.plotly_chart(fig)


# In[36]:


st.text("---" * 100)


# In[37]:


st.subheader("Box Plots")


# In[38]:


fig = px.box(data_frame=df, title="Box Plots for each feature")
fig.show()


# In[39]:


st.plotly_chart(fig)

