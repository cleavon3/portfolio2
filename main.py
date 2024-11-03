import streamlit as st
import pandas

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Cleavon A")
    content = """
    Hi i am cleavon! i am a python developer. Backend ethusiast
    """
    st.info(content)

content2 = """
Below you can some of my projecct built in python
"""
st.write(content2)

col3, col4 = st.columns(2)


df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        st.write(row["title"])

with col4:
    for index, row in df.iterrows():
        st.header(row["title"])