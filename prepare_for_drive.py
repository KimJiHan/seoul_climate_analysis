#!/usr/bin/env python3
"""
Prepare Seoul Heatwave Course data for Google Drive sharing
This script renames and organizes files for easier sharing
"""

import os
import shutil
import zipfile
from pathlib import Path
import pandas as pd

def prepare_drive_structure():
    """Create Google Drive friendly structure"""
    
    # Create base directories
    base_path = Path('drive_upload')
    data_path = base_path / 'seoul_heatwave_course' / 'data'
    
    # Create directory structure
    (data_path / 'raw' / 's-dot').mkdir(parents=True, exist_ok=True)
    (data_path / 'external' / 'sgis_boundaries').mkdir(parents=True, exist_ok=True)
    (data_path / 'processed').mkdir(parents=True, exist_ok=True)
    
    print("📁 Created directory structure")
    return data_path

def rename_sdot_files(source_dir, target_dir):
    """Rename S-DoT files to Google Drive friendly names"""
    
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Mapping of original to new names
    file_mapping = {
        'S-DoT_NATURE_2025.04.28-05.04.csv': 'sdot_2025_04_28_05_04.csv',
        'S-DoT_NATURE_2025.05.05-05.11.csv': 'sdot_2025_05_05_05_11.csv',
        'S-DoT_NATURE_2025.05.12-05.18.csv': 'sdot_2025_05_12_05_18.csv',
        'S-DoT_NATURE_2025.05.19-05.25.csv': 'sdot_2025_05_19_05_25.csv',
        'S-DoT_NATURE_2025.05.26-06.01.csv': 'sdot_2025_05_26_06_01.csv',
        'S-DoT_NATURE_2025.06.02-06.08.csv': 'sdot_2025_06_02_06_08.csv',
        'S-DoT_NATURE_2025.06.09-06.15.csv': 'sdot_2025_06_09_06_15.csv',
        'S-DoT_NATURE_2025.06.16-06.22.csv': 'sdot_2025_06_16_06_22.csv',
        'S-DoT_NATURE_2025.06.23-06.29.csv': 'sdot_2025_06_23_06_29.csv',
        'S-DoT_NATURE_2025.06.30-07.06.csv': 'sdot_2025_06_30_07_06.csv',
        'S-DoT_NATURE_2025.07.07-07.13.csv': 'sdot_2025_07_07_07_13.csv',
        'S-DoT_NATURE_2025.07.14-07.20.csv': 'sdot_2025_07_14_07_20.csv',
        'S-DoT_NATURE_2025.07.21-07.27.csv': 'sdot_2025_07_21_07_27.csv',
        'S-DoT_NATURE_2025.07.28-08.03.csv': 'sdot_2025_07_28_08_03.csv',
        'S-DoT_NATURE_2025.08.04-08.10.csv': 'sdot_2025_08_04_08_10.csv',
        'S-DoT_NATURE_2025.08.11-08.17.csv': 'sdot_2025_08_11_08_17.csv',
    }
    
    copied_files = 0
    for old_name, new_name in file_mapping.items():
        old_path = source_path / old_name
        new_path = target_path / new_name
        
        if old_path.exists():
            shutil.copy2(old_path, new_path)
            print(f"  ✅ {old_name} → {new_name}")
            copied_files += 1
    
    print(f"📊 Copied {copied_files} S-DoT files")
    return copied_files

def prepare_external_data(source_dir, target_dir):
    """Prepare external data with simplified names"""
    
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Copy and rename sensor location file
    sensor_file = source_path / '서울시 도시데이터 센서(S-DoT) 환경정보 설치 위치정보.xlsx'
    if sensor_file.exists():
        shutil.copy2(sensor_file, target_path / 'sensor_locations.xlsx')
        print("  ✅ Copied sensor_locations.xlsx")
    
    # Zip SGIS boundary files
    sgis_source = source_path / 'sgis_boundaries'
    sgis_target = target_path / 'sgis_boundaries'
    
    if sgis_source.exists():
        # Zip each boundary type
        boundary_dirs = {
            '1. 2024년 2분기 기준 시도 경계': 'seoul_sido.zip',
            '2. 2024년 2분기 기준 시군구 경계': 'seoul_sigungu.zip',
            '3. 2024년 2분기 기준 행정동 경계': 'seoul_dong.zip'
        }
        
        for dir_name, zip_name in boundary_dirs.items():
            dir_path = sgis_source / dir_name
            if dir_path.exists():
                zip_path = sgis_target / zip_name
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for file in dir_path.iterdir():
                        zipf.write(file, file.name)
                print(f"  ✅ Created {zip_name}")

def create_compressed_bundle(data_path):
    """Create a compressed bundle of all data"""
    
    bundle_path = data_path.parent.parent / 'seoul_heatwave_data.zip'
    
    print("\n📦 Creating compressed bundle...")
    with zipfile.ZipFile(bundle_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(data_path):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(data_path.parent.parent)
                zipf.write(file_path, arcname)
    
    # Check size
    size_mb = bundle_path.stat().st_size / (1024 * 1024)
    print(f"✅ Created bundle: {bundle_path.name} ({size_mb:.1f} MB)")
    
    return bundle_path

def create_sample_data(source_dir, target_dir, sample_size=10000):
    """Create smaller sample dataset for testing"""
    
    source_path = Path(source_dir)
    sample_path = Path(target_dir) / 'sample'
    sample_path.mkdir(parents=True, exist_ok=True)
    
    print("\n🔬 Creating sample dataset...")
    
    csv_files = list(source_path.glob('*.csv'))[:3]  # First 3 files
    
    for csv_file in csv_files:
        try:
            # Read with Korean encoding
            df = pd.read_csv(csv_file, encoding='euc-kr', nrows=sample_size)
            
            # Save sample
            output_name = f"sample_{csv_file.name.replace('S-DoT_NATURE_', '').replace('.', '_').lower()}.csv"
            output_path = sample_path / output_name
            df.to_csv(output_path, index=False, encoding='utf-8')
            
            print(f"  ✅ Created {output_name} ({sample_size} rows)")
        except Exception as e:
            print(f"  ❌ Error with {csv_file.name}: {e}")

def main():
    """Main preparation function"""
    
    print("🚀 Preparing Seoul Heatwave Course data for Google Drive\n")
    
    # Setup paths (adjust these to your actual paths)
    current_dir = Path.cwd()
    source_data = current_dir / 'data'
    
    if not source_data.exists():
        print("❌ Error: 'data' directory not found!")
        print("Please run this script from the seoul_heatwave_course directory")
        return
    
    # Create Drive structure
    data_path = prepare_drive_structure()
    
    # Process S-DoT files
    print("\n📊 Processing S-DoT files...")
    sdot_source = source_data / 'raw' / 's-dot'
    sdot_target = data_path / 'raw' / 's-dot'
    
    if sdot_source.exists():
        rename_sdot_files(sdot_source, sdot_target)
    else:
        print("  ⚠️ S-DoT source directory not found")
    
    # Process external data
    print("\n📁 Processing external data...")
    external_source = source_data / 'external'
    external_target = data_path / 'external'
    
    if external_source.exists():
        prepare_external_data(external_source, external_target)
    else:
        print("  ⚠️ External data directory not found")
    
    # Create compressed bundle
    bundle_path = create_compressed_bundle(data_path)
    
    # Create sample data
    if sdot_source.exists():
        create_sample_data(sdot_source, data_path.parent)
    
    print("\n✅ Preparation complete!")
    print(f"\n📁 Upload this folder to Google Drive: {data_path.parent}")
    print(f"📦 Or upload the compressed bundle: {bundle_path}")
    print("\n💡 Tips:")
    print("  1. Upload to: My Drive/seoul_heatwave_course/")
    print("  2. Share folder with students (view-only)")
    print("  3. Students can add shortcut to their Drive")

if __name__ == "__main__":
    main()