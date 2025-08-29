# 📂 Seoul Heatwave Course - Data Setup Guide

## 🎯 Overview
This guide explains how to set up the data directory structure for the Seoul Heatwave Analysis Course.

## 📁 Required Directory Structure

```
seoul_heatwave_course/
├── notebooks/          # Jupyter notebooks (Week 01-10)
├── data/              # All data files (NOT tracked by Git)
│   ├── raw/           # Original data files
│   │   └── s-dot/     # S-DoT sensor CSV files
│   ├── processed/     # Processed/cleaned data
│   └── external/      # External reference data
│       ├── sgis_boundaries/    # SGIS administrative boundaries
│       ├── sgis_statistics/    # SGIS statistical data
│       └── *.xlsx              # Sensor location info
└── requirements.txt   # Python dependencies
```

## 🔧 Data Setup Instructions

### Step 1: Create Directory Structure
```bash
cd seoul_heatwave_course
mkdir -p data/raw/s-dot
mkdir -p data/processed
mkdir -p data/external/sgis_boundaries
mkdir -p data/external/sgis_statistics
```

### Step 2: Add S-DoT Sensor Data
Place all S-DoT CSV files in `data/raw/s-dot/`:
- Files should be named like: `S-DoT_NATURE_2025.MM.DD-MM.DD.csv`
- Total size: ~0.8GB (16 files from April-August 2025)
- Each file contains 10-minute interval sensor measurements

### Step 3: Add External Data

#### 3.1 Sensor Location File
Place in `data/external/`:
- `서울시 도시데이터 센서(S-DoT) 환경정보 설치 위치정보.xlsx`
- Contains sensor coordinates and installation details

#### 3.2 SGIS Boundary Data
Place in `data/external/sgis_boundaries/`:
- `1. 2024년 2분기 기준 시도 경계/` - Province boundaries
- `2. 2024년 2분기 기준 시군구 경계/` - District boundaries  
- `3. 2024년 2분기 기준 행정동 경계/` - Administrative dong boundaries

Each folder should contain:
- `.shp` - Shapefile (geometry)
- `.dbf` - Database file (attributes)
- `.shx` - Shape index
- `.prj` - Projection information
- `.cpg` - Character encoding

#### 3.3 SGIS Statistics (Optional)
Place in `data/external/sgis_statistics/`:
- Population and demographic data
- Economic indicators
- Other statistical data

## 📊 Data Sources

### S-DoT Data
- **Source**: Seoul Open Data Portal
- **URL**: https://data.seoul.go.kr
- **Format**: CSV with Korean encoding (EUC-KR)
- **Variables**: Temperature, Humidity, PM2.5, PM10, Noise

### SGIS Data
- **Source**: Statistics Korea (KOSTAT)
- **URL**: https://sgis.kostat.go.kr
- **Format**: Shapefiles and Excel
- **Purpose**: Administrative boundaries for spatial analysis

## 🌍 Environment-Specific Setup

### Local Environment
Use the directory structure as shown above with relative paths.

### Google Colab
```python
# Option 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
# Copy data to: /content/drive/MyDrive/seoul_heatwave_course/data/

# Option 2: Clone from GitHub (code only)
!git clone https://github.com/KimJiHan/seoul_climate_analysis.git
# Then upload data files separately
```

### Kaggle
1. Upload data as a Kaggle Dataset
2. Add dataset to your notebook
3. Data will be available at `/kaggle/input/`

## ⚠️ Important Notes

1. **Git Ignore**: Data files are excluded from version control due to size
2. **Encoding**: S-DoT CSV files use Korean encoding (EUC-KR or CP949)
3. **File Size**: Total data size is approximately 1GB
4. **Privacy**: Do not share sensor serial numbers or sensitive location data

## ✅ Verification

Run Section 4.1 in Week01 notebook to verify data setup:
```python
# Should show:
# ✅ S-DoT data directory found
# 📊 Found 16 CSV files (Total: 0.80 GB)
# 📋 External data files found
```

## 📞 Support

If you have issues accessing the data:
1. Check file permissions
2. Verify directory structure matches above
3. Ensure sufficient disk space (>2GB recommended)
4. Contact course instructor for data access

---
*Last Updated: December 2024*