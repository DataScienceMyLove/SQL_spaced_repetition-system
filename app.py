import streamlit as st
import pandas as pd
import duckdb

st.write("""
        # Spaced repetition system for SQL practice
        
        App designed by DataScienceMyLove
        
        """)

option = st.selectbox("How would you like to practice",
                      ['Joins', 'Aggregations', 'Window Functions'],
                      index=None,
                      placeholder='Select theme',
                      )

st.write("You selected", option)

# Creation and print the DataFrame in the streamlit app
data = {"a": [1, 2, 3, 5, 45], "b": [4, 5, 6, 8, 9]}
df = pd.DataFrame(data)
st.write(
    "Salut, voici ma première app pour lire les requêtes SQL et regarder des images d'animaux :D, faîtes votre requête sur cette table df")
st.write(df)

# Creation of tabs
tab1, tab2, tab3 = st.tabs(["SQL QUERY", "Dog", "Owl"])

# Inside each tab
with tab1:
    sql_query = st.text_area(label="Entrez votre requête SQL")
    result = duckdb.sql(sql_query).df()
    st.write(f"Voici le résultat de la requête : {sql_query}")
    st.dataframe(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("A owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
