# Escreva o seu código aqui :-)
import streamlit as st

import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# pandas lendo arquivos tipo csv
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

