# 🇮🇳 CoviGraph

An interactive COVID-19 analytics and visualization dashboard that explores India's pandemic journey through state-wise case trends, vaccination progress, and geographical insights.

Built using Streamlit, Plotly, Pandas, and GeoJSON, CoviGraph transforms raw COVID-19 datasets into meaningful visual stories and interactive dashboards.

---

## 📸 Overview

CoviGraph enables users to:

* Monitor India's COVID-19 progression over time
* Analyze major pandemic waves
* Compare COVID-19 trends across states
* Visualize case distribution on an interactive map
* Explore vaccination progress across India
* Identify patterns using interactive charts and dashboards

---

## ✨ Features

### 📈 National COVID Timeline

* Daily new COVID-19 cases visualization
* 7-Day rolling average trend analysis
* Highlighted major pandemic waves:

  * First Wave Peak
  * Delta Wave Peak
  * Omicron Wave Peak

### 🗺️ State-wise Choropleth Map

* Interactive India map visualization
* State-level COVID statistics
* Hover details including:

  * Confirmed Cases
  * Active Cases
  * Recoveries
  * Deaths

### 📊 State Comparison Dashboard

* Compare multiple states simultaneously
* Interactive state selection
* Trend analysis through dynamic visualizations
* Rolling average case tracking

### 💉 Vaccination Analytics

* Dose 1 vs Dose 2 comparison
* State-wise vaccination progress
* Top-performing states analysis
* Interactive filtering options

### ⚡ Performance Optimization

* Cached data loading using Streamlit
* Efficient data processing with Pandas
* Fast and responsive visualizations

---

## 🛠️ Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core Programming Language       |
| Streamlit  | Interactive Dashboard Framework |
| Pandas     | Data Processing & Analysis      |
| NumPy      | Numerical Computation           |
| Plotly     | Interactive Data Visualization  |
| GeoJSON    | Geographic Mapping              |
| Requests   | Data Retrieval                  |

---

## 📂 Project Structure

```text
CoviGraph/
│
├── app.py
├── charts.py
├── data_loader.py
├── requirements.txt
│
├── data/
│   ├── covid_19_india.csv
│   ├── covid_vaccine_statewise.csv
│   ├── StatewiseTestingDetails.csv
│   └── india_states.geojson
│
└── README.md
```

---

## 📊 Data Sources

### COVID-19 Case Data

Contains state-wise statistics including:

* Confirmed Cases
* Active Cases
* Recoveries
* Deaths

### Vaccination Data

Contains:

* First Dose Administration
* Second Dose Administration
* Total Vaccinations
* State-wise Vaccination Progress

### Geographic Data

GeoJSON boundary data for Indian states used in map visualizations.

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/SoumyaK111/CoviGraph.git
cd CoviGraph
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 📈 Data Processing Pipeline

1. Load COVID-19 and vaccination datasets
2. Clean and standardize state names
3. Convert and validate date fields
4. Compute analytical metrics:

   * Active Cases
   * Daily New Cases
   * Rolling Averages
   * Mortality Statistics
5. Generate interactive visualizations
6. Render dashboards using Streamlit

---

## 🔍 Key Insights Provided

### COVID-19 Metrics

* Total Confirmed Cases
* Active Cases
* Recoveries
* Deaths

### Trend Analysis

* Daily Case Growth
* Pandemic Wave Detection
* Rolling Average Analysis

### Vaccination Analysis

* State-wise Vaccination Progress
* Dose Distribution
* Comparative Vaccination Insights

---

## 🚀 Future Enhancements

* Real-time COVID-19 API integration
* Predictive forecasting using Machine Learning
* Testing and hospitalization analytics
* Downloadable reports and dashboards
* Mobile-responsive interface improvements
* Advanced filtering and customization

---

## 🎯 Learning Outcomes

This project demonstrates practical experience in:

* Data Cleaning and Transformation
* Exploratory Data Analysis (EDA)
* Interactive Dashboard Development
* Geospatial Data Visualization
* Streamlit Application Development
* Plotly Visualization Techniques
* Data Engineering Workflows

---

## 👨‍💻 Author

### Soumya Kushwaha

GitHub: https://github.com/SoumyaK111

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.

---

## 📄 License

This project is developed for educational, research, and portfolio purposes.
