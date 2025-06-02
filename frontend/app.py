import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab

st.set_page_config(page_title="Expense Tracker", layout = 'wide')
st.markdown("# 💸 Expense Tracking Dashboard")

tab1, tab2, tab3 = st.tabs([
    "➕ Add / Update Expenses", 
    "📊 Analytics by Category", 
    "📅 Analytics by Month"
])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()
