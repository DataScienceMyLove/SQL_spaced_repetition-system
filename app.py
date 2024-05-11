import streamlit as st
import pandas as pd
import duckdb
import io

st.write("""
        # Spaced repetition system for SQL practice

        App designed by DataScienceMyLove

        """)

csv = '''
beverage,price
orange juice,2.5
Expresso,2
Tea,3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()

with st.sidebar:
    option = st.selectbox("How would you like to practice",
                          ['Joins', 'Aggregations', 'Window Functions'],
                          index=None,
                          placeholder='Select theme',
                          )
    st.write("You selected", option)

st.header("Enter your code: ")
query = st.text_area(label="Enter your SQL query:", key="user_input")

if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

# Creation of tabs
tab2, tab3 = st.tabs(["Tables", "Solution"])

# Inside each tab

with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)
