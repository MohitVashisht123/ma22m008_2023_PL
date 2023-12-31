# -*- coding: utf-8 -*-
"""Assignemnt10b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18s1tZW4R93H3iiclzNxN__LGMs3dTyR1
"""

pip install geopandas matplotlib plotly pandas

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
type(world)

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Load the 'naturalearth_lowres' dataset from GeoPandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Load the COVID-19 data (replace with your actual COVID-19 dataset)
covid_data = pd.read_csv('covid_data.csv')

# Merge the COVID-19 data with the GeoPandas dataset based on country names
merged_data = world.set_index('name').join(covid_data.set_index('Country_Region'))

# Plot the chloropleth map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='Confirmed', cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_title('COVID-19 Cases Worldwide')
plt.axis('off')

# Save the chloropleth map as a PNG file
plt.savefig('covid_choropleth.png')

# Show the map
plt.show()



print(covid_data)



