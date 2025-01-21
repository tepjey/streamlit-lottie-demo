import json
import streamlit as st
from streamlit_lottie import st_lottie

def showaura():
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    
    lottie_aura = load_lottiefile("lottiefiles/aurarobot.json")

    st_lottie(
        lottie_aura,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=None,
        width=None,
        key=None,
    )

showaura()