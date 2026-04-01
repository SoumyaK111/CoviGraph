import pandas as pd
import numpy as np
import json
import os
import requests

def download_geojson():
    url = "https://raw.githubusercontent.com/geohacker/india/master/state/india_state.geojson"
    filepath = "data/india_states.geojson"
    if not os.path.exists(filepath):
        print("Downloading GeoJSON...")
        r = requests.get(url)
        with open(filepath, "w") as f:
            f.write(r.text)
        print("GeoJSON saved!")

def load_covid_data():
    df = pd.read_csv("data/covid_19_india.csv")
    print("Actual columns:", df.columns.tolist())
    df.rename(columns={"State/UnionTerritory": "State", "Cured": "Recovered", "Death": "Deaths"}, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"], format="mixed", dayfirst=True, errors="coerce")
    df.dropna(subset=["Date"], inplace=True)
    state_rename = {"Telengana": "Telangana"}
    df["State"] = df["State"].replace(state_rename)
    df = df[~df["State"].isin(["Total", "Cases being reassigned to states"])]
    for col in ["Confirmed", "Deaths", "Recovered"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)
    df.sort_values(["State", "Date"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df["Active"] = (df["Confirmed"] - df["Recovered"] - df["Deaths"]).clip(lower=0)
    df["New_Cases"] = df.groupby("State")["Confirmed"].diff().fillna(0).clip(lower=0)
    df["Rolling_7"] = df.groupby("State")["New_Cases"].transform(lambda x: x.rolling(7, min_periods=1).mean())
    df["Mortality_Rate"] = (df["Deaths"] / df["Confirmed"].replace(0, 1) * 100).round(2)
    return df

def load_vaccination_data():
    vdf = pd.read_csv("data/covid_vaccine_statewise.csv")
    vdf["Updated On"] = pd.to_datetime(vdf["Updated On"], dayfirst=True, errors="coerce")
    cols = ["Updated On", "State", "Total Doses Administered", "First Dose Administered", "Second Dose Administered"]
    vdf = vdf[[c for c in cols if c in vdf.columns]].copy()
    vdf.dropna(inplace=True)
    return vdf

def load_geojson():
    download_geojson()
    with open("data/india_states.geojson", "r") as f:
        return json.load(f)
