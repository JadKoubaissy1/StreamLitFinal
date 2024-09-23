import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Waste Transfer Bubble Map Visualization")

file_path = 'C:/Users/User/Desktop/WasteByRegion.csv'
df = pd.read_csv(file_path)

df.rename(columns={
    'Waste transfer destination - factory': 'Waste destination: factory',
    'Waste transfer destination - unknown': 'Waste destination: unknown',
    'Waste transfer destination - internal dumpsite': 'Waste destination: internal dumpsite',
    'Waste transfer destination - external dumpsite': 'Waste destination: external dumpsite',
    'Waste transfer destination - sanitary landfill': 'Waste destination: sanitary landfill'
}, inplace=True)

def categorize_region(area):
    if 'Beirut' in area:
        return 'Beirut'
    elif 'North' in area:
        return 'North'
    elif 'South' in area:
        return 'South'
    elif 'Bekaa' in area or 'Baalbek' in area or 'Hermel' in area or 'Zahle' in area:
        return 'East'
    elif 'Mount Lebanon' in area:
        return 'West'
    else:
        return 'West'

df['Region_Category'] = df['refArea'].apply(lambda x: categorize_region(x))

region_coords = {
    'Beirut': (33.8938, 35.5018),
    'North': (34.4367, 35.8506),
    'South': (33.2707, 35.2037),
    'East': (33.8765, 36.089),
    'West': (33.8172, 35.5428)
}

df_grouped = df.groupby(['Region_Category'])[waste_columns].sum().reset_index()
df_grouped['lat'] = df_grouped['Region_Category'].map(lambda x: region_coords[x][0])
df_grouped['lon'] = df_grouped['Region_Category'].map(lambda x: region_coords[x][1])

fig = px.scatter_mapbox(
    df_grouped, 
    lat='lat', 
    lon='lon', 
    size='Total Waste', 
    color='Region_Category', 
    hover_name='Region_Category', 
    title='Waste Transfer by Region',
    mapbox_style="open-street-map", 
    size_max=50, 
    zoom=6
)

st.plotly_chart(fig)
