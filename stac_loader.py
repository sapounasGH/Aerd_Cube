from typing import List, Dict, Any, Optional, Iterator
from pystac_client import Client
from pystac_client.item_search import ItemSearch
from pystac import Item
import odc.stac
import xarray as xr
import consts

class StacLoader:
    def __init__(self, catalog_url: str = consts.CATALOG_URL) -> None:
        self.catalog: Client = Client.open(catalog_url)
    
    def search(self, collections: List[str], bbox: List[float], datetime: str) -> ItemSearch:
        return self.catalog.search(
            collections=collections,
            bbox=bbox,
            datetime=datetime
        )
    
    def load(self, query: ItemSearch, bands: List[str], resolution: int = consts.DEFAULT_RESOLUTION, chunks: Optional[Dict[str, int]] = None) -> xr.Dataset:
        if chunks is None:
            chunks = consts.DEFAULT_CHUNKS
        
        return odc.stac.load(
            query.items(),
            bands=bands,
            resolution=resolution,
            chunks=chunks
        )
