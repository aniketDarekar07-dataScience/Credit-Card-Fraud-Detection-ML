import streamlit as st
import pandas as pd

def show_charts(df):
    st.subheader("📊 Fraud Analysis")
    counts = df["Fraud"].value_counts()
    st.bar_chart(counts)

    pie_data = pd.DataFrame({
        "Type": ["Normal", "Fraud"],
        "Count": [counts.get(0,0), counts.get(1,0)]
    })
    st.subheader("📈 Fraud Distribution")
    st.dataframe(pie_data)
