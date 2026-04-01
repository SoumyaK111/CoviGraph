# -*- coding: utf-8 -*-
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

WAVES = {
    "Wave 1 Peak": "2020-09-16",
    "Wave 2 Delta": "2021-05-07",
    "Wave 3 Omicron": "2022-01-20",
}

def plot_national_timeline(df):
    national = df.groupby("Date")[["New_Cases", "Rolling_7"]].sum().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=national["Date"], y=national["New_Cases"],
        name="Daily New Cases", marker_color="rgba(192,57,43,0.25)"))
    fig.add_trace(go.Scatter(x=national["Date"], y=national["Rolling_7"],
        name="7-Day Average", line=dict(color="#c0392b", width=2.5)))
    for label, date in WAVES.items():
        fig.add_vline(x=pd.Timestamp(date), line_dash="dot",
                      line_color="#e67e22", line_width=1.5)
        fig.add_annotation(x=pd.Timestamp(date), y=1, yref="paper",
            text=label, showarrow=False,
            font=dict(size=10, color="#e67e22"),
            xanchor="left", xshift=5)
    fig.update_layout(title="India COVID-19 Daily Cases - All Waves",
        xaxis_title="Date", yaxis_title="New Cases",
        plot_bgcolor="white", hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02))
    return fig

def plot_choropleth(df, geojson):
    latest = df.sort_values("Date").groupby("State").last().reset_index()
    fig = px.choropleth(latest, geojson=geojson,
        locations="State", featureidkey="properties.NAME_1",
        color="Confirmed", color_continuous_scale="Reds",
        hover_data={"Confirmed": ":,", "Deaths": ":,",
                    "Recovered": ":,", "Active": ":,"},
        title="Total Confirmed Cases by State")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    return fig

def plot_state_comparison(df, states):
    fig = go.Figure()
    colors = px.colors.qualitative.Plotly
    for i, state in enumerate(states):
        s_df = df[df["State"] == state]
        fig.add_trace(go.Scatter(x=s_df["Date"], y=s_df["Rolling_7"],
            name=state, line=dict(color=colors[i % len(colors)], width=2)))
    fig.update_layout(title="7-Day Rolling Average - State Comparison",
        xaxis_title="Date", yaxis_title="Daily Cases (7-day avg)",
        plot_bgcolor="white", hovermode="x unified")
    return fig

def plot_vaccination_bars(vdf, top_n=15):
    latest_vax = (vdf.sort_values("Updated On")
                     .groupby("State").last().reset_index()
                     .sort_values("Total Doses Administered", ascending=False)
                     .head(top_n))
    fig = go.Figure()
    if "First Dose Administered" in latest_vax.columns:
        fig.add_trace(go.Bar(y=latest_vax["State"],
            x=latest_vax["First Dose Administered"],
            name="Dose 1", orientation="h", marker_color="#3498db"))
    if "Second Dose Administered" in latest_vax.columns:
        fig.add_trace(go.Bar(y=latest_vax["State"],
            x=latest_vax["Second Dose Administered"],
            name="Dose 2", orientation="h", marker_color="#27ae60"))
    fig.update_layout(title=f"Vaccination Progress - Top {top_n} States",
        barmode="group", plot_bgcolor="white",
        xaxis_title="Doses Administered", height=520)
    return fig
