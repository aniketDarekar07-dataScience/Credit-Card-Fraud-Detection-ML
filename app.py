import streamlit as st
import pandas as pd
import time
from model.model import load_model, evaluate_model
from utils.style import apply_style
from utils.charts import show_charts

st.set_page_config(page_title="Fraud Detection AI", layout="wide")
apply_style()

st.title("💳 AI Credit Card Fraud Detection")
st.caption("Advanced ML system with analytics dashboard")

model, X_test, y_test = load_model()

accuracy = evaluate_model(model, X_test, y_test)
st.sidebar.success(f"🎯 Model Accuracy: {accuracy:.2f}%")

file = st.file_uploader("📂 Upload Transaction CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("🔍 Analyze Transactions"):
        with st.spinner("Analyzing..."):
            time.sleep(2)

        preds = model.predict(df)
        df["Fraud"] = preds

        st.success("✅ Analysis Complete")
        st.dataframe(df)

        fraud_count = sum(preds)
        st.error(f"🚨 Fraud Transactions: {fraud_count}")

        show_charts(df)
