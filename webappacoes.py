import streamlit as st 
import pandas as pd
from datetime import date
from annotated_text import annotated_text


# Nome da aplicação


annotated_text(
    
     "Acompanhamento ",
    ("das", "*"),
    " Ações ",
    ("Bovespa", "*"),
    ("2023", "*"),
    " Stoncks ",
    ":"
   
    
)


# Criando o side bar

st.sidebar.header('Escolha sua Ação')

# Ler arquivo de ações

def get_data():
    path = 'bovespa.csv'
    return pd.read_csv(path)
    
df = get_data()

df_data = pd.to_datetime(df['data_pregao']).dt.date.drop_duplicates()

min_date = min(df_data)

max_date = max(df_data)

stock = df['sigla_acao'].drop_duplicates()
stock_choices = st.sidebar.selectbox('Escolha sua ação:', stock)

start_date = st.sidebar.text_input('Digite a data de início:', min_date)
end_date = st.sidebar.text_input('Digite a data de fim:', max_date)

start = pd.to_datetime(start_date)
end = pd.to_datetime(end_date)

if start > end :
    st.error('Data final deve ser *MAIOR* que a data inicial.')
    
df = df[(df['sigla_acao'] == stock_choices) & (pd.to_datetime(df['data_pregao']) >= start) & (
            pd.to_datetime(df['data_pregao']) <= end)]

df = df.set_index(pd.DatetimeIndex(df['data_pregao'].values))

# criando o gráfico

st.header('AÇÃO: ' + stock_choices.upper())
st.write('Preço de fechamento: ')
st.line_chart(df['preco_fechamento']) 

st.write('Volume negociado:')
st.line_chart(df['volume_negocios'])

   

