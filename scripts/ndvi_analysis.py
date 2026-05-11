import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

file_path = r"C:\Users\omare\Desktop\Data_Scientist\Mersin\Mersin_NDVI_2025.tif"
output_path = r"C:\Users\omare\Desktop\Data_Scientist\Mersin\ndvi_Histogram_final.png"

if not os.path.exists(file_path):
    print(f"Error: Could not find the file at {file_path}")
else:
    with rasterio.open(file_path) as src:
        ndvi = src.read(1).astype('float32')

    valid_mask = (ndvi >= -1) & (ndvi <= 1)
    ndvi_valid = np.where(valid_mask, ndvi, np.nan)

    print(f"Mean NDVI: {np.nanmean(ndvi_valid):.4f}")
    print(f"Maximum NDVI: {np.nanmax(ndvi_valid):.4f}")
    print(f"Standard Deviation: {np.nanstd(ndvi_valid):.4f}")

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(ndvi_valid[~np.isnan(ndvi_valid)], bins=50, color='forestgreen', edgecolor='black')
    ax.set_title('NDVI Distribution - Mersin 2025')
    ax.set_xlabel('NDVI Value')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=300)
    print(f"Success! Histogram saved to: {output_path}")
