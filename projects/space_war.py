import streamlit as st
import subprocess
import sys

# Configure the Streamlit page
st.set_page_config(page_title="Snake Game", layout="centered")

st.markdown(
    """
    <style>
    /* ===== Global fun background (CSS key-frame animation) ===== */
    @keyframes funkyGradient {
        0%   { background-position:   0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position:   0% 50%; }
    }
    .stApp {
        background: linear-gradient(60deg,
            #ff9a9e 0%,  #fad0c4 25%, 
            #fad0c4 25%, #fbc8d4 50%, 
            #fbc8d4 50%, #a1c4fd 75%,
            #a1c4fd 75%, #c2e9fb 100%);
        background-size: 300% 300%;
        animation: funkyGradient 20s ease infinite;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    /* ===== Center container ===== */
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        width: 100%;
    }

    /* ===== Button styling ===== */
    .stButton > button {
        background-color: #15ccbe;
        color: white;
        font-size: 1rem;
        padding: 0.8em 2.2em;
        border: none;
        border-radius: 8px;
        transition: background-color 0.25s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    .stButton > button:hover {
        background-color: #0f988e;
    }

    /* ===== Center & space out the Play button ===== */
    .stButton {
        display: flex !important;
        justify-content: center !important;
        width: 100%;
        margin-top: 1.5rem;  /* push button down slightly */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="center-container" style="border:2px solid lightblue; padding:20px; border-radius:10px; display:inline-block; background: lightskyblue;">
        <h1 style="color:blue; margin:0;">Space War</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Play button that launches the Pygame snake_game.py script
if st.button("Play"):
    st.write("Launching Space War...")
    subprocess.Popen([sys.executable, "games/SpaceWar/SpaceWar.py"])
