import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def add_update_tab():
    st.subheader("Add or Update Your Expenses")
    st.markdown("You can add up to 5 expenses for the selected date.")
    st.markdown("---")

    selected_date = st.date_input("Choose Date", datetime(2024, 8, 1))

    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses.")
        existing_expenses = []

    # Category mapping with emojis
    category_emojis = {
        "Rent": "🏠",
        "Food": "🍽️",
        "Shopping": "🛍️",
        "Entertainment": "🎮",
        "Other": "🧾"
    }

    categories = list(category_emojis.keys())

    with st.form(key="expense_form"):
        st.markdown("### Daily Expenses")

        expenses = []
        for i in range(5):
            st.markdown(f"##### Expense #{i+1}")
            with st.container():
                col1, col2, col3 = st.columns([1, 2.2, 2])

                # Pre-fill existing values
                amount = existing_expenses[i]['amount'] if i < len(existing_expenses) else 0.0
                category = existing_expenses[i]['category'] if i < len(existing_expenses) else "Shopping"
                notes = existing_expenses[i]['notes'] if i < len(existing_expenses) else ""

                with col1:
                    amount_input = st.number_input(
                        label="Amount", min_value=0.0, step=1.0, value=amount,
                        key=f"amount_{i}", label_visibility="collapsed"
                    )

                with col2:
                    emoji_buttons = [f"{category_emojis[cat]} {cat}" for cat in categories]
                    default_index = categories.index(category)
                    selected = st.radio(
                        "Select Category",
                        emoji_buttons,
                        index=default_index,
                        key=f"category_{i}",
                        horizontal=True,
                        label_visibility="collapsed"
                    )
                    category_input = selected.split(" ", 1)[1]  # Extract "Food" from "🍽️ Food"

                with col3:
                    notes_input = st.text_input("Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

                expenses.append({
                    'amount': amount_input,
                    'category': category_input,
                    'notes': notes_input
                })

            st.markdown("---")

        submit_button = st.form_submit_button("💾 Save Expenses")

        if submit_button:
            filtered_expenses = [e for e in expenses if e['amount'] > 0]
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("✅ Expenses updated successfully!")
            else:
                st.error("❌ Failed to update expenses.")
