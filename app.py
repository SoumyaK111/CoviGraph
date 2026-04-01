import streamlit as st
import pandas as pd

# Import your modules

from data_loader import load_covid_data, load_vaccination_data, load_geojson
from charts import (
plot_national_timeline,
plot_choropleth,
plot_state_comparison,
plot_vaccination_bars
)

# ------------------ PAGE CONFIG ------------------

st.set_page_config(
page_title="India COVID-19 Dashboard",
layout="wide"
)

st.title("🇮🇳 India COVID-19 Dashboard")

# ------------------ LOAD DATA ------------------

@st.cache_data
def load_data():
    df = load_covid_data()
    vdf = load_vaccination_data()
    geojson = load_geojson()
    return df, vdf, geojson
df, vdf, geojson = load_data()

# ------------------ SIDEBAR ------------------

st.sidebar.header("Filters")

states = sorted(df["State"].unique())
selected_states = st.sidebar.multiselect(
"Select States for Comparison",
options=states,
default=states[:5]
)

top_n = st.sidebar.slider(
"Top N States (Vaccination)",
min_value=5,
max_value=25,
value=15
)

# ------------------ MAIN DASHBOARD ------------------

# 1. National Timeline

st.subheader("📈 National Trend")
fig1 = plot_national_timeline(df)
st.plotly_chart(fig1, use_container_width=True)

# 2. Choropleth Map

st.subheader("🗺️ State-wise Spread")
fig2 = plot_choropleth(df, geojson)
st.plotly_chart(fig2, use_container_width=True)

# 3. State Comparison

st.subheader("📊 State Comparison (7-day avg)")
if selected_states:
    fig3 = plot_state_comparison(df, selected_states)
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("Please select at least one state")

# 4. Vaccination Progress

st.subheader("💉 Vaccination Progress")
fig4 = plot_vaccination_bars(vdf, top_n)
st.plotly_chart(fig4, use_container_width=True)

# ------------------ FOOTER ------------------

st.markdown("---")

