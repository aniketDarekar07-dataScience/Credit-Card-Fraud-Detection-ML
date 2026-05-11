import streamlit as st
def apply_style():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg,#000000,#1c1c1c,#434343);
        color:white;
    }
    .stButton>button {
        width:100%;
        height:3em;
        border-radius:12px;
        background:linear-gradient(90deg,#ff0000,#ff7300);
        color:white;
        font-size:18px;
    }
    </style>
    """, unsafe_allow_html=True)
