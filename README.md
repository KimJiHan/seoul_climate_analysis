# Seoul Heatwave Analysis Course
## Data Science Approach to Urban Climate Analysis

### 📚 Course Overview
This course provides hands-on experience analyzing heatwave patterns in Seoul using real S-DoT (Smart Seoul Data of Things) sensor data. Students will learn to apply data science techniques, statistical methods, and GIS tools to understand urban climate phenomena and their impacts on residential areas.

### 🎯 Learning Objectives
Upon completion of this course, students will be able to:

1. **Quantify** the frequency, intensity, and duration of heat waves in Seoul
2. **Calculate** and analyze the Heat Index using the **KMA (Korea Meteorological Administration) formula**
3. **Perform** spatial analysis to identify vulnerable areas using GIS
4. **Investigate** correlations between urban characteristics and heat wave intensity
5. **Conduct** temporal analysis to identify seasonal patterns
6. **Assess** the impact on vulnerable populations using demographic data
7. **Develop** predictive models for future heat wave events
8. **Evaluate** and propose heat wave mitigation strategies

### 👨‍🏫 Instructor
**Sohn Chul**

### 📂 Repository Structure
```
seoul_heatwave_course/
├── notebooks/          # Weekly Jupyter notebooks (Week 01-10)
├── data/              # Data directory
│   ├── raw/           # Original sensor data
│   │   └── s-dot/     # S-DoT CSV files (16 files, 0.8GB)
│   ├── processed/     # Cleaned and processed datasets
│   └── external/      # Reference and boundary data
│       ├── sgis_boundaries/    # Administrative boundaries (SHP files)
│       ├── sgis_statistics/    # SGIS statistical data  
│       ├── sgis_codes/         # Administrative codes
│       ├── sgis_manual/        # Documentation
│       └── *.xlsx              # Sensor location info
├── src/               # Reusable Python modules
├── assignments/       # Weekly assignments
├── outputs/           # Analysis results
│   ├── figures/       # Charts and plots
│   ├── maps/          # GIS visualizations
│   └── reports/       # Analysis reports
└── docs/              # Additional documentation
```

### 📅 Course Schedule (Complete - 10 Weeks)

| Week | Topic | Key Activities |
|------|-------|----------------|
| 1 | **Introduction & Setup** | Environment setup, Git/GitHub, Course overview |
| 2 | **Data Collection & Preprocessing** | Load S-DoT data, Data cleaning, EDA |
| 3 | **Heat Index Calculation** | **KMA formula implementation**, Temperature conversions |
| 4 | **Spatial Analysis & GIS** | GeoPandas, Heat maps, Spatial autocorrelation |
| 5 | **Temporal Pattern Analysis** | Time series decomposition, Seasonality analysis |
| 6 | **Urban Heat Island Analysis** | UHI effect quantification, Vulnerability mapping |
| 7 | **Statistical Modeling** | Regression analysis, Model validation |
| 8 | **Machine Learning Applications** | ML models, Clustering, Anomaly detection |
| 9 | **Advanced Visualization** | Interactive dashboards, Real-time monitoring |
| 10 | **Final Project** | Comprehensive analysis system development |

### 🛠️ Prerequisites

#### Software Requirements
- Python 3.8 or higher
- Jupyter Notebook/Lab
- Git

#### Python Libraries
```bash
pip install -r requirements.txt
```

Key libraries include:
- `pandas`, `numpy` - Data manipulation
- `matplotlib`, `seaborn`, `plotly` - Visualization
- `geopandas`, `folium` - GIS and mapping
- `scikit-learn`, `xgboost` - Machine learning
- `tensorflow`, `keras` - Deep learning
- `statsmodels` - Statistical analysis
- `streamlit` - Dashboard creation

### 📊 Dataset Information

#### S-DoT Sensor Data
- **Period**: April - August 2025
- **Frequency**: 10-minute intervals
- **Variables**: Temperature, Humidity, PM2.5, PM10, Noise levels
- **Format**: CSV files (weekly batches)

#### Heat Index Formula
**KMA (Korea Meteorological Administration) Formula** using Stull's wet-bulb temperature estimation:
```python
# Wet-bulb temperature calculation
Tw = Ta * arctan(0.151977 * (RH + 8.313659)^0.5) + 
     arctan(Ta + RH) - arctan(RH - 1.67633) + 
     0.00391838 * RH^1.5 * arctan(0.023101 * RH) - 4.686035

# KMA Heat Index
HI = -0.2442 + 0.55399*Tw + 0.45535*Ta - 0.0022*Tw² + 0.00278*Tw*Ta + 3.0
```

#### Additional Data
- **SGIS Administrative Boundaries** (Statistics Korea, 2024 Q2)
  - Seoul administrative dong boundaries (Shapefile)
  - District (gu) and city (si/do) boundaries 
  - Statistical area codes and reference data
- **Sensor Location Information** (Excel format)
  - S-DoT sensor coordinates and installation details
  - District and location type classifications

### 🚀 Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/KimJiHan/seoul_climate_analysis.git
cd seoul_climate_analysis/seoul_heatwave_course
```

2. **Set up Python environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Launch Jupyter Notebook**
```bash
jupyter notebook
```

4. **Start with Week 1 notebook**
Navigate to `notebooks/Week01_Introduction_Setup.ipynb`

### 📈 Assessment

| Component | Weight | Description |
|-----------|--------|-------------|
| Weekly Assignments | 30% | Hands-on coding exercises |
| Midterm Project | 25% | Spatial analysis project |
| Final Project | 35% | Comprehensive analysis system |
| Participation | 10% | Class engagement |

### ✅ Completed Course Materials

All 10 weeks of course materials have been completed and include:

- **Week 01-02**: Setup and data preprocessing
- **Week 03**: KMA heat index calculation implementation
- **Week 04**: Advanced spatial analysis with GeoPandas
- **Week 05**: Time series and temporal pattern analysis
- **Week 06**: Urban heat island effect analysis
- **Week 07**: Statistical modeling and regression
- **Week 08**: Machine learning and deep learning applications
- **Week 09**: Interactive visualization and dashboard creation
- **Week 10**: Final project - comprehensive analysis system

### 📝 Assignment Submission

1. Fork this repository
2. Complete assignments in your fork
3. Submit via Pull Request
4. Include your name and week number in PR title

### 🔗 Resources

- [S-DoT Open Data Portal](https://data.seoul.go.kr)
- [Korea Meteorological Administration](https://www.kma.go.kr)
- [SGIS Statistical Geographic Information Service](https://sgis.kostat.go.kr)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [GeoPandas Documentation](https://geopandas.org)

### 📧 Support

For questions and support:
- Create an issue in the [GitHub repository](https://github.com/KimJiHan/seoul_climate_analysis/issues)
- Check existing issues before creating a new one

### 📄 License

This course material is provided for educational purposes. The S-DoT data is provided by Seoul Metropolitan Government.

---
*Last Updated: December 2024 | Instructor: Sohn Chul*
