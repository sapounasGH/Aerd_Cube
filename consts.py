# STAC Configuration
CATALOG_URL = "https://earth-search.aws.element84.com/v1"
DEFAULT_COLLECTION = "sentinel-2-l2a"

# Default spatial and temporal parameters
DEFAULT_BBOX = [10, 50, 10.1, 50.1]  # [min_lon, min_lat, max_lon, max_lat]
DEFAULT_DATETIME = "2023-01-01/2023-01-07"

# Data loading configuration
DEFAULT_BANDS = ["red", "green", "blue"]
DEFAULT_RESOLUTION = 100  # meters
DEFAULT_CHUNKS = {"x": 1000, "y": 1000}

# Sentinel-2 bands
SENTINEL2_BANDS = {
    "coastal": "B01",
    "blue": "B02",
    "green": "B03",
    "red": "B04",
    "rededge1": "B05",
    "rededge2": "B06",
    "rededge3": "B07",
    "nir": "B08",
    "nir08": "B8A",
    "nir09": "B09",
    "swir16": "B11",
    "swir22": "B12",
    "scl": "SCL"
}

# Coordinate reference systems
EPSG_WGS84 = "EPSG:4326"
EPSG_UTM32N = "EPSG:32632"
