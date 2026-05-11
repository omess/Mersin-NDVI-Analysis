import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

# Update these paths if your folder name is different
file_path = r"C:\Users\omare\Desktop\Mersin_Project\data\Mersin_NDVI_2025.tif"
output_path = r"C:\Users\omare\Desktop\Mersin_Project\maps\Mersin_Map_Visual.png"

if not os.path.exists(file_path):
    print(f"Error: Could not find the file at {file_path}")
else:
    with rasterio.open(file_path) as src:
        ndvi = src.read(1).astype('float32')
        # Mask out values outside the valid NDVI range
        ndvi = np.where((ndvi >= -1) & (ndvi <= 1), ndvi, np.nan)

    plt.figure(figsize=(12, 10))
    # 'RdYlGn' is the standard color ramp for NDVI
    img = plt.imshow(ndvi, cmap='RdYlGn', vmin=-0.1, vmax=0.6)
    
    cbar = plt.colorbar(img, fraction=0.046, pad=0.04)
    cbar.set_label('NDVI Value (Vegetation Health)')
    
    plt.title('Mersin Satellite Analysis - NDVI Spatial Distribution (2025)', fontsize=15)
    plt.axis('off') 
    
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Success! Map visualization saved to: {output_path}")
