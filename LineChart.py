import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Waste Transfer Line Plot Visualization")

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

waste_columns = [
    'Waste destination: factory', 
    'Waste destination: unknown', 
    'Waste destination: internal dumpsite', 
    'Waste destination: external dumpsite', 
    'Waste destination: sanitary landfill'
]

df_grouped = df.groupby(['Region_Category'])[waste_columns].sum().reset_index()
df_melted = df_grouped.melt(id_vars='Region_Category', var_name='Waste Transfer Type', value_name='Count')

fig = px.line(
    df_melted, 
    x='Region_Category', 
    y='Count', 
    color='Waste Transfer Type', 
    title='Waste Transfer Types Across Regions',
    markers=True, 
    text='Count'
)
fig.update_traces(textposition='top center')

st.plotly_chart(fig)
