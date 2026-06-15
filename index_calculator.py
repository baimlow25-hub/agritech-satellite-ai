import numpy as np
import os
import rasterio

def calculate_ndvi(file_path):
    """
    Ingests a specific satellite image file path and extracts the 
    mean vegetation health index safely.
    """
    satellite_file = file_path
    file_name = os.path.basename(satellite_file)
    
    print(f"🛰️ Ingesting real satellite band data from: {file_name}...")
    
    try:
        with rasterio.open(satellite_file) as src:
            red_band = src.read(1).astype('float64')
            nir_band = src.read(3).astype('float64')
    except FileNotFoundError:
        print(f"\n❌ ERROR: Could not find '{file_name}'!")
        return None

    # Safe matrix calculation block to bypass 0/0 division warnings
    denominator = nir_band + red_band
    numerator = nir_band - red_band
    
    ndvi = np.zeros_like(numerator)
    valid_mask = denominator > 0
    ndvi[valid_mask] = numerator[valid_mask] / denominator[valid_mask]
    
    mean_health = float(np.mean(ndvi))
    print(f"🌲 Extracted Canopy Health Score: {mean_health:.4f}")
    print("-" * 50)
    
    return mean_health
import numpy as np
import os
import rasterio

def calculate_ndvi(file_path):
    """
    Ingests a specific satellite image file path and extracts the 
    mean vegetation health index safely.
    """
    satellite_file = file_path
    file_name = os.path.basename(satellite_file)
    
    print(f"🛰️ Ingesting real satellite band data from: {file_name}...")
    
    try:
        with rasterio.open(satellite_file) as src:
            red_band = src.read(1).astype('float64')
            nir_band = src.read(3).astype('float64')
    except FileNotFoundError:
        print(f"\n❌ ERROR: Could not find '{file_name}'!")
        return None

    # Safe matrix calculation block to bypass 0/0 division warnings
    denominator = nir_band + red_band
    numerator = nir_band - red_band
    
    ndvi = np.zeros_like(numerator)
    valid_mask = denominator > 0
    ndvi[valid_mask] = numerator[valid_mask] / denominator[valid_mask]
    
    mean_health = float(np.mean(ndvi))
    print(f"🌲 Extracted Canopy Health Score: {mean_health:.4f}")
    print("-" * 50)
    
    return mean_health