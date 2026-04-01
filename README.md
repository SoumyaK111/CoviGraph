# CoviGraph #
Interactive 5-page dashboard visualizing India's complete COVID-19 journey across all 36 states and union territories.

📊 Features
National timeline with 7-day rolling average and wave annotations
State-wise choropleth heatmap using Plotly + India GeoJSON
Multi-state comparison with dynamic dropdowns
Vaccination progress (Dose 1 / Dose 2) by state
KPI metrics: total cases, deaths, CFR, recovery rate

🛠️ Tech Stack
Tool	Purpose
Python 3.10	Core Language
Pandas	Data cleaning & wrangling
NumPy	Rolling averages
Plotly	Interactive charts & choropleths
Streamlit	Dashboard framework & deployment

📂 Dataset
Source: COVID-19 India Dataset on Kaggle
Records: ~500,000 statewise daily records
Date range: Jan 2020 - May 2023
GeoJSON: India state boundaries (github.com/geohacker/india)

📝 Key Findings
Wave 2 (Delta, May 2021) was 3.4x larger than Wave 1 by daily cases
Maharashtra consistently had the highest case burden nationally
Kerala showed a distinct wave pattern offset by 3-4 weeks from national trend
Southern states achieved higher Dose 2 coverage % relative to population