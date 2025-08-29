# ☁️ Google Drive Upload Checklist

## 📤 Upload Instructions

### Step 1: Open Google Drive
1. Go to https://drive.google.com
2. Sign in with your Google account

### Step 2: Upload Folder
1. Click "New" → "Folder upload"
2. Select: `drive_upload/seoul_heatwave_course/`
3. Wait for upload to complete (~1GB, may take 10-30 minutes)

### Step 3: Verify Upload
Check that the following structure exists in Google Drive:

```
My Drive/
└── seoul_heatwave_course/
    ├── data/
    │   ├── raw/
    │   │   └── s-dot/
    │   │       ├── sdot_2025_04_28_05_04.csv ✓
    │   │       ├── sdot_2025_05_05_05_11.csv ✓
    │   │       └── ... (16 files total)
    │   ├── external/
    │   │   ├── sensor_locations.xlsx ✓
    │   │   └── sgis_boundaries/
    │   │       ├── seoul_sido.zip ✓
    │   │       ├── seoul_sigungu.zip ✓
    │   │       └── seoul_dong.zip ✓
    │   └── processed/
    └── sample/
        └── (3 sample CSV files)
```

## 📋 Verification Checklist

### ✅ Required Files

#### S-DoT Data (16 files)
- [ ] sdot_2025_04_28_05_04.csv (32.9 MB)
- [ ] sdot_2025_05_05_05_11.csv (50.0 MB)
- [ ] sdot_2025_05_12_05_18.csv (48.6 MB)
- [ ] sdot_2025_05_19_05_25.csv (54.9 MB)
- [ ] sdot_2025_05_26_06_01.csv (48.5 MB)
- [ ] sdot_2025_06_02_06_08.csv (44.2 MB)
- [ ] sdot_2025_06_09_06_15.csv (46.0 MB)
- [ ] sdot_2025_06_16_06_22.csv (47.9 MB)
- [ ] sdot_2025_06_23_06_29.csv (49.9 MB)
- [ ] sdot_2025_06_30_07_06.csv (57.0 MB)
- [ ] sdot_2025_07_07_07_13.csv (50.5 MB)
- [ ] sdot_2025_07_14_07_20.csv (51.9 MB)
- [ ] sdot_2025_07_21_07_27.csv (53.9 MB)
- [ ] sdot_2025_07_28_08_03.csv (59.4 MB)
- [ ] sdot_2025_08_04_08_10.csv (52.5 MB)
- [ ] sdot_2025_08_11_08_17.csv (57.4 MB)

#### External Data
- [ ] sensor_locations.xlsx (112 KB)
- [ ] seoul_sido.zip (55 MB)
- [ ] seoul_sigungu.zip (63 MB)
- [ ] seoul_dong.zip (91 MB)

#### Sample Data (Optional)
- [ ] sample_2025_06_02-06_08_csv.csv (1.5 MB)
- [ ] sample_2025_07_14-07_20_csv.csv (1.5 MB)
- [ ] sample_2025_08_11-08_17_csv.csv (1.5 MB)

## 🔗 Sharing Settings

### For Instructors

1. **Right-click** on `seoul_heatwave_course` folder
2. Click **"Share"**
3. Choose sharing option:
   - **Option A**: "Anyone with the link" → "Viewer"
   - **Option B**: Add specific email addresses
   - **Option C**: Share with organization

4. **Copy link** and share with students

### Sharing Message Template

```
📚 Seoul Heatwave Analysis Course - Data Access

Dear Students,

The course data is now available on Google Drive:
📁 Link: [YOUR_SHARE_LINK_HERE]

Instructions:
1. Click the link above
2. Click "Add shortcut to Drive" (star icon)
3. Open Google Colab
4. Run test_google_drive.ipynb to verify access
5. Start with Week01 notebook

Data includes:
- 16 S-DoT sensor CSV files (April-August 2025)
- Sensor location information
- SGIS administrative boundaries
- Sample datasets for testing

If you have any issues accessing the data, please let me know.

Best regards,
Instructor Sohn Chul
```

## 🧪 Testing Access

### In Google Colab

1. Open `test_google_drive.ipynb`
2. Run all cells
3. Verify all checks pass:
   - ✅ Google Drive Mounted
   - ✅ Data Folder Found
   - ✅ S-DoT Data (16 files)
   - ✅ Sensor Locations
   - ✅ SGIS Boundaries
   - ✅ Data Loadable

### Quick Test Code

```python
from google.colab import drive
drive.mount('/content/drive')

import os
path = '/content/drive/MyDrive/seoul_heatwave_course'
if os.path.exists(path):
    print("✅ Data found!")
else:
    print("❌ Data not found")
```

## 🚨 Troubleshooting

### Issue: Upload taking too long
**Solution**: Upload the compressed file instead
- Upload `seoul_heatwave_data.zip` (291 MB)
- Extract in Google Drive

### Issue: Students can't access
**Check**:
1. Sharing permissions set to "Viewer"
2. Link sharing is enabled
3. Students are signed into Google

### Issue: Path not found in Colab
**Try these paths**:
```python
paths = [
    '/content/drive/MyDrive/seoul_heatwave_course',
    '/content/drive/My Drive/seoul_heatwave_course',
    '/content/drive/Shareddrives/seoul_heatwave_course'
]
```

## ✅ Final Confirmation

Once uploaded and shared:
1. [ ] All files uploaded successfully
2. [ ] Folder shared with proper permissions
3. [ ] Test notebook verifies data access
4. [ ] Students notified with access link
5. [ ] At least one student confirmed access

---

**Upload Date**: _______________
**Share Link**: _______________
**Total Size**: ~1.0 GB
**Files Count**: 24 files

*Last Updated: December 2024*