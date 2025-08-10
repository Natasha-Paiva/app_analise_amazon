# Escreva o seu código aqui :-)
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# pandas lendo arquivos tipo csv obtidos no Kaggle
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

#df_reviews
#exibe a tabela

#definindo os preços mínimos e máximos baseados no arquivo
price_min = df_top100_books["book price"].min()
price_max = df_top100_books["book price"].max()

#criando um slider utilizando os preços obtidos
max_price = st.sidebar.slider("Média de Preço", price_min, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

df_books

fig = px.bar(df_books["year of publication"].value_counts())
st.plotly_chart(fig)



