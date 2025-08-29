# 📁 Google Drive Data Sharing Guide for Seoul Heatwave Course

## 🎯 Overview

This guide explains how to share and access course data via Google Drive for Google Colab users.

## 📂 Google Drive Folder Structure

### Recommended Structure in Google Drive

```
My Drive/
└── seoul_heatwave_course/
    ├── notebooks/              # Course notebooks (optional, can use GitHub)
    ├── data/                   # Main data folder
    │   ├── raw/
    │   │   └── s-dot/         # S-DoT sensor data
    │   │       ├── sdot_2025_04_28_05_04.csv
    │   │       ├── sdot_2025_05_05_05_11.csv
    │   │       ├── sdot_2025_05_12_05_18.csv
    │   │       ├── sdot_2025_05_19_05_25.csv
    │   │       ├── sdot_2025_05_26_06_01.csv
    │   │       ├── sdot_2025_06_02_06_08.csv
    │   │       ├── sdot_2025_06_09_06_15.csv
    │   │       ├── sdot_2025_06_16_06_22.csv
    │   │       ├── sdot_2025_06_23_06_29.csv
    │   │       ├── sdot_2025_06_30_07_06.csv
    │   │       ├── sdot_2025_07_07_07_13.csv
    │   │       ├── sdot_2025_07_14_07_20.csv
    │   │       ├── sdot_2025_07_21_07_27.csv
    │   │       ├── sdot_2025_07_28_08_03.csv
    │   │       ├── sdot_2025_08_04_08_10.csv
    │   │       └── sdot_2025_08_11_08_17.csv
    │   ├── processed/          # Empty initially
    │   └── external/
    │       ├── sensor_locations.xlsx
    │       └── sgis_boundaries/
    │           ├── seoul_sido.zip
    │           ├── seoul_sigungu.zip
    │           └── seoul_dong.zip
    └── outputs/                # Results (optional)
```

## 📝 File Naming Conventions

### S-DoT Data Files

**Original Names** (Korean):
```
S-DoT_NATURE_2025.04.28-05.04.csv
```

**Google Drive Names** (Simplified):
```
sdot_2025_04_28_05_04.csv
```

### External Data Files

**Original Name**:
```
서울시 도시데이터 센서(S-DoT) 환경정보 설치 위치정보.xlsx
```

**Google Drive Name**:
```
sensor_locations.xlsx
```

### SGIS Boundary Files

**Original Structure**:
```
1. 2024년 2분기 기준 시도 경계/
├── bnd_sido_00_2024_2Q.shp
├── bnd_sido_00_2024_2Q.dbf
└── ...
```

**Google Drive Structure** (Zipped):
```
seoul_sido.zip      # Contains all sido boundary files
seoul_sigungu.zip   # Contains all sigungu boundary files  
seoul_dong.zip      # Contains all dong boundary files
```

## 🚀 Setup Instructions

### Step 1: Upload to Google Drive

1. **Create folder structure**:
   ```python
   # In Google Colab
   from google.colab import drive
   drive.mount('/content/drive')
   
   import os
   os.makedirs('/content/drive/MyDrive/seoul_heatwave_course/data/raw/s-dot', exist_ok=True)
   os.makedirs('/content/drive/MyDrive/seoul_heatwave_course/data/external/sgis_boundaries', exist_ok=True)
   os.makedirs('/content/drive/MyDrive/seoul_heatwave_course/data/processed', exist_ok=True)
   ```

2. **Upload files via Colab**:
   ```python
   from google.colab import files
   
   # Upload S-DoT files
   uploaded = files.upload()  # Select all S-DoT CSV files
   
   # Move to correct location
   import shutil
   for filename in uploaded.keys():
       shutil.move(filename, f'/content/drive/MyDrive/seoul_heatwave_course/data/raw/s-dot/{filename}')
   ```

### Step 2: Share Folder (For Instructors)

1. Right-click on `seoul_heatwave_course` folder in Google Drive
2. Click "Share"
3. Choose one option:
   - **Public Link**: "Anyone with the link can view"
   - **Specific Users**: Add student emails
   - **Organization**: Share within your institution

4. Copy the sharing link

### Step 3: Access Shared Data (For Students)

**Option A: Direct Mount**
```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Navigate to shared folder
import os
data_path = '/content/drive/MyDrive/seoul_heatwave_course/data'

# Or if accessing shared folder
data_path = '/content/drive/Shared drives/seoul_heatwave_course/data'
```

**Option B: Copy from Shared Link**
```python
# If instructor provides folder ID
# Folder ID is the part after /folders/ in the sharing link
# Example: https://drive.google.com/drive/folders/1ABC123xyz...
folder_id = '1ABC123xyz...'  # Replace with actual ID

# Download using gdown
!pip install -q gdown
!gdown --folder https://drive.google.com/drive/folders/{folder_id} -O /content/seoul_data
```

## 📊 Data Size Optimization

### Compression Options

To reduce upload/download time:

```python
# Compress S-DoT data before upload
import zipfile
import os

# Create compressed archive
with zipfile.ZipFile('sdot_data_2025.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('data/raw/s-dot'):
        for file in files:
            if file.endswith('.csv'):
                zipf.write(os.path.join(root, file))

# Size reduction: ~800MB → ~200MB
```

### Partial Data Option

For testing/development, create a sample dataset:

```python
import pandas as pd
import glob

# Load and sample data
csv_files = glob.glob('data/raw/s-dot/*.csv')
for file in csv_files[:3]:  # First 3 files only
    df = pd.read_csv(file, encoding='euc-kr')
    df_sample = df.sample(n=10000)  # 10K rows per file
    df_sample.to_csv(f'sample_{os.path.basename(file)}', index=False)
```

## 🔧 Colab Notebook Configuration

Add this to the beginning of your Colab notebooks:

```python
# Auto-detect and setup paths
import os
import sys

def setup_colab_paths():
    """Setup paths for Google Colab with Drive"""
    from google.colab import drive
    drive.mount('/content/drive')
    
    # Check multiple possible locations
    possible_paths = [
        '/content/drive/MyDrive/seoul_heatwave_course/data',
        '/content/drive/Shared drives/seoul_heatwave_course/data',
        '/content/seoul_heatwave_course/data'
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    # If not found, create structure
    base_path = '/content/drive/MyDrive/seoul_heatwave_course/data'
    os.makedirs(base_path, exist_ok=True)
    return base_path

# Setup paths
DATA_PATH = setup_colab_paths()
print(f"📁 Using data path: {DATA_PATH}")
```

## 📋 File Checklist

Essential files for the course:

### S-DoT Data (Required)
- [ ] 16 CSV files covering April-August 2025
- [ ] Total size: ~800MB (or ~200MB compressed)
- [ ] Encoding: EUC-KR or CP949

### External Data (Required)
- [ ] sensor_locations.xlsx (sensor coordinates)
- [ ] seoul_sido.zip (province boundaries)
- [ ] seoul_sigungu.zip (district boundaries)
- [ ] seoul_dong.zip (dong boundaries)

### Optional Data
- [ ] SGIS statistics (population, demographics)
- [ ] Additional reference materials

## 🔗 Sharing Best Practices

1. **Use descriptive folder names** without special characters
2. **Compress large files** before uploading
3. **Set appropriate permissions** (view-only for students)
4. **Create a README** with data descriptions
5. **Include sample notebooks** for data verification

## 🚨 Troubleshooting

### Common Issues

**1. Drive storage limit**
```python
# Check available space
!df -h /content/drive
```

**2. Mount timeout**
```python
# Try remounting
from google.colab import drive
drive.flush_and_unmount()
drive.mount('/content/drive', force_remount=True)
```

**3. File encoding errors**
```python
# Try different encodings
encodings = ['euc-kr', 'cp949', 'utf-8']
for enc in encodings:
    try:
        df = pd.read_csv(file_path, encoding=enc)
        print(f"Success with {enc}")
        break
    except:
        continue
```

## 📝 Example Sharing Message

Send this to students:

```
📚 Seoul Heatwave Course - Data Access

Google Drive Link: [your_link_here]

📁 Folder Structure:
- data/raw/s-dot/ → S-DoT sensor data (16 files)
- data/external/ → Reference data and boundaries

💻 To use in Colab:
1. Open the shared folder
2. Add shortcut to your Drive
3. Mount Drive in Colab
4. Run Week01 notebook to verify

❓ Issues? Check GOOGLE_DRIVE_SETUP.md
```

---

*Last Updated: December 2024*