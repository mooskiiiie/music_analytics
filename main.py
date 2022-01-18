import streamlit as st
from multiapp import MultiApp
from apps import home, content

app = MultiApp()

app.add_app('Analysis', home.app)
app.add_app('Playlists', content.app)


app.run()