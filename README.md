# Land Surface Temperature & NDVI Analysis: Mersin, Türkiye
**A Geospatial Study on Urban Vegetation Health**

## 🌍 Project Overview
This project investigates the spatial distribution of vegetation health in Mersin using NASA satellite data. By integrating Google Earth Engine (GEE), QGIS, and Python, I've created a workflow to monitor environmental changes and urban greening patterns.

## 🛠️ Tech Stack
* **Data Acquisition:** Google Earth Engine (Landsat 8 Collection 2)
* **GIS Software:** QGIS 3.x (Styling, Basemapping, & Cartography)
* **Analysis:** Python (Rasterio, NumPy, Matplotlib)
* **Version Control:** GitHub

## 📊 Key Results
* **Visual Analysis:** The generated map highlights a clear contrast between the dense urban coastal core (Low NDVI) and the surrounding agricultural zones to the North and East.
* **Statistics:**
    * **Mean NDVI:** 0.1275 (Indicates mixed urban/shrubland landscape)
    * **Max NDVI:** 0.5405 (Points to healthy agricultural pockets)

## 📁 Repository Structure
```text
project/
├── data/           # Satellite TIFF files (Mersin_NDVI_2025.tif)
├── maps/           # Final QGIS Exports (Mersin_Final_Map.png)
├── scripts/        # Python analysis scripts
└── README.md       # Project documentation