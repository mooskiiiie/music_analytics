import streamlit as st
import streamlit.components.v1 as components

def app():
    
    st.title("Developing a Recommender Engine using Streaming Analytics")


    components.html("""
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT0QKktYbh7H5tVzW8WEUNdH0mm0IrvhBi4vMEAOkbD3cQcahYWmq--YZfkCviHAA/embed?start=false&loop=false&delayms=3000" 
    allowfullscreen="true" height=500 width=850></iframe>
    """,
    height=500,
    width=850
    )

    