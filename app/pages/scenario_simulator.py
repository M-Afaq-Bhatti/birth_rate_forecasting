import streamlit as st

st.set_page_config(
    page_title="Scenario Simulator",
    page_icon="📈",
    layout="wide"
)

# --- Title ---
st.title("📈 Scenario Simulator")

# --- Info ---
st.markdown("""
This feature will allow you to simulate different birth rate scenarios in the future based on variables like:
- Healthcare improvements
- Economic changes
- Policy shifts
- Pandemic events, etc.

🔧 **Coming soon:** Upload CSV, modify trends, and visualize outcomes.
""")

# --- Placeholder for future tool ---
st.info("Scenario simulation tools are under development. Stay tuned!")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 | Scotland Birth Forecasting Project")
