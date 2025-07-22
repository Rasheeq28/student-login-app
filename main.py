import streamlit as st
import pandas as pd

# Load Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("Edumail list, BBA-23 (B-48).xlsx")
    df.columns = df.columns.str.strip()  # Strip any accidental whitespace
    return df

df = load_data()

# UI
st.title("🎓 Student Login Portal")

student_id = st.text_input("Enter your Student ID")
mobile_no = st.text_input("Enter your Mobile No")

if st.button("Get Credentials"):
    if not student_id or not mobile_no:
        st.warning("Please enter both Student ID and Mobile No.")
    else:
        # Filter based on inputs
        match = df[
            (df["STUDENT ID"].astype(str).str.strip() == student_id.strip()) &
            (df["Mobile No."].astype(str).str.strip() == mobile_no.strip())
        ]

        if not match.empty:
            username = match.iloc[0]["Username"]
            password = match.iloc[0]["Password"]
            st.success("✅ Match found!")
            st.write(f"**Username:** `{username}`")
            st.write(f"**Password:** `{password}`")
        else:
            st.error("❌ No match found. Please check your inputs.")
