import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://localhost:8000"

def analytics_category_tab():
    st.markdown("### 📊 Expense Analytics by Category")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("📈 Generate Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[cat]["total"] for cat in response],
            "Percentage": [response[cat]["percentage"] for cat in response]
        }
        df = pd.DataFrame(data).sort_values(by="Percentage", ascending=False)

        fig = px.bar(df, x="Category", y="Percentage", color="Category",
                     title="Category-wise Expense Breakdown",
                     text_auto='.2f', labels={"Percentage": "Percentage (%)"})
        st.plotly_chart(fig, use_container_width=True)

        df["Total"] = df["Total"].map("{:.2f}".format)
        df["Percentage"] = df["Percentage"].map("{:.2f}".format)

        st.dataframe(df, use_container_width=True)
