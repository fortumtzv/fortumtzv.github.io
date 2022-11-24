import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("Dashboard Programas Internacionales ITESM 2022")

df = pd.read_csv("programas_internacionales_final.csv")

f=px.choropleth(df, locations="PaisOportunidadAsignada",
                color="Promedio",
                hover_name="PaisOportunidadAsignada",
                scope='world',
                title = "Promedio por Pachangepoint_prior_scaleises",
                projection='robinson',
                color_continuous_scale=px.colors.diverging.BrBG)



st.plotly_chart(f)

st.markdown("_")