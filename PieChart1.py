import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Proportion of Waste Transfer Types - Pie Chart")

file_path = 'C:/Users/User/Desktop/WasteByRegion.csv'
df = pd.read_csv(file_path)

df.rename(columns={
    'Waste transfer destination - factory': 'Waste destination: factory',
    'Waste transfer destination - unknown': 'Waste destination: unknown',
    'Waste transfer destination - internal dumpsite': 'Waste destination: internal dumpsite',
    'Waste transfer destination - external dumpsite': 'Waste destination: external dumpsite',
    'Waste transfer destination - sanitary landfill': 'Waste destination: sanitary landfill'
}, inplace=True)

df_melted = df.melt(id_vars=['Region_Category'], 
                    value_vars=waste_columns, 
                    var_name='Waste Transfer Type', 
                    value_name='Count')

fig = px.pie(
    df_melted, 
    names='Waste Transfer Type', 
    values='Count', 
    title='Proportion of Waste Transfer Types (Overall)',
    height=600
)

st.plotly_chart(fig)
