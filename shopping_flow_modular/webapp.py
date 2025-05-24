from typing import Optional
from interface import ProductStoreInterface

class WebApp:
    def __init__(self, store: ProductStoreInterface):
        self.store = store

    def load_home(self):
        return self.store.get_latest_products(10)

    def search_products(self, keyword: str, brand: Optional[str], max_price: Optional[int]):
        results = self.store.search(keyword)
        filtered = self.store.filter(results, brand, max_price)
        return sorted(filtered, key=lambda x: x.price)

    def show_detail(self, product_id: int):
        return self.store.get_detail(product_id)