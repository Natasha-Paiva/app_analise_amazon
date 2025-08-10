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

# gráfico que exibe o valor dos livros por ano de publicação
grafico_qt = px.bar(df_books["year of publication"].value_counts())

# criação de histograma que exibe o valor dos livros por ano de publicação
grafico_valor = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(grafico_qt)
col2.plotly_chart(grafico_valor)

