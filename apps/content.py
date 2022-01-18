import streamlit as st
import streamlit.components.v1 as components

def app():
    st.title("Deployed Playlists")

    st.header("Plane Ride")
    components.html("""
    <iframe src="https://open.spotify.com/embed/playlist/16wXhDDNgt8wvTO7nzZpWs?utm_source=generator" 
    width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; 
    clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
    """,
    width=500,
    height=380,
    )

    st.header("Resort")
    components.html("""
    <iframe src="https://open.spotify.com/embed/playlist/5TwGPZwGmneoPL63jmPzui?utm_source=generator" 
    width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay;
     clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
    """,
    width=500,
    height=380,
    )

    st.header('Hotel')
    components.html("""
    <iframe src="https://open.spotify.com/embed/playlist/178u79wlFXTZm5eCFlTGwb?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
    """,
    width=500,
    height=380,
    )

    st.header('Restaurant')
    components.html("""
    <iframe src="https://open.spotify.com/embed/playlist/1jWVPo2KyPemqXU3xagk01?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
    """,
    width=500,
    height=380,
    )

    st.header('Travel')
    components.html("""
    <iframe src="https://open.spotify.com/embed/playlist/3FrLOj53B2Hq1gXvLcpr7Q?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen=""
     allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe> 
    """,
    width=500,
    height=380,
    )

