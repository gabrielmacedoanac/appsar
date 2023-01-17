import streamlit as st
import pandas as pd
import streamlit_pandas as sp

st.write('# Appsar')
st.write('## Um app para localizar os normativos da ANAC')

@st.cache
def load_data():
    df = pd.read_csv(file)
    return df

file = "https://raw.githubusercontent.com/gabrielmacedoanac/flat-data-anac/main/regulamentos-anac-tags.csv"
df = load_data()

create_data = {"ementa": "text",
               "tipo_normatico" : "multiselect",
               "tags": "text"}

all_widgets = sp.create_widgets(df, create_data)
res = sp.filter_df(df, all_widgets)
st.write(res)