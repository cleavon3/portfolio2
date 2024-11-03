import streamlit as st

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