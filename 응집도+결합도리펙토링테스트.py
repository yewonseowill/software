# 두 코드의 응집도/결합도 요소를 수치화하고 비교하는 분석기
# 기준: 클래스 수, 인터페이스 존재 여부, 의존 방향, 책임 수(간이 측정)

import ast
import pandas as pd

def analyze_code(code: str, name: str):
    tree = ast.parse(code)
    class_metrics = {
        "source": name,
        "class_count": 0,
        "interface_used": False,
        "explicit_dependency": 0,
        "method_total": 0,
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_metrics["class_count"] += 1
            for b in node.body:
                if isinstance(b, ast.FunctionDef):
                    class_metrics["method_total"] += 1
                if isinstance(b, ast.ClassDef) and "Protocol" in [b.name for b in ast.walk(b) if isinstance(b, ast.Name)]:
                    class_metrics["interface_used"] = True
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ["ProductRepository", "WebApp"]:
                class_metrics["explicit_dependency"] += 1

    # 가중치 기반 스코어 계산
    cohesion_score = max(0, 10 - abs(5 - class_metrics["method_total"]) // 2)
    coupling_score = max(0, 10 - class_metrics["explicit_dependency"] * 2 + (2 if class_metrics["interface_used"] else 0))
    
    class_metrics["cohesion_score"] = cohesion_score
    class_metrics["coupling_score"] = coupling_score

    return class_metrics

# 코드 1: 개선 버전 (인터페이스 사용, AppService 분리)
with open("/mnt/data/shopping_flow_modular/main.py") as f:
    main_code = f.read()
with open("/mnt/data/shopping_flow_modular/service.py") as f:
    service_code = f.read()
with open("/mnt/data/shopping_flow_modular/webapp.py") as f:
    webapp_code = f.read()
with open("/mnt/data/shopping_flow_modular/repository.py") as f:
    repository_code = f.read()
with open("/mnt/data/shopping_flow_modular/interface.py") as f:
    interface_code = f.read()
with open("/mnt/data/shopping_flow_modular/product.py") as f:
    product_code = f.read()

modular_code = "\n".join([main_code, service_code, webapp_code, repository_code, interface_code, product_code])
modular_result = analyze_code(modular_code, "개선 구조")

# 코드 2: 기존 구조
original_path = "/mnt/data/shopping_flow_original.py"
original_code = """
from typing import List, Optional

# 상품 클래스
class Product:
    def __init__(self, product_id: int, name: str, brand: str, price: int):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.brand}) - {self.price}원"

class ProductRepository:
    def __init__(self):
        self.products = [
            Product(1, "로지텍 무선 마우스", "로지텍", 25000),
            Product(2, "HP 유선 마우스", "HP", 15000),
            Product(3, "로지텍 게이밍 마우스", "로지텍", 45000),
            Product(4, "삼성 블루투스 마우스", "삼성", 29000),
            Product(5, "LG 유선 마우스", "LG", 18000),
            Product(6, "로지텍 무선 키보드", "로지텍", 32000),
            Product(7, "애플 매직 마우스", "애플", 79000),
            Product(8, "델 유선 마우스", "델", 14000),
            Product(9, "MS 블루투스 마우스", "MS", 31000),
            Product(10, "로지텍 사일런트 마우스", "로지텍", 27000),
        ]

    def get_latest_products(self, count: int = 10) -> List[Product]:
        return self.products[:count]

    def search(self, keyword: str) -> List[Product]:
        return [p for p in self.products if keyword in p.name]

    def filter(self, products: List[Product], brand: Optional[str], max_price: Optional[int]) -> List[Product]:
        result = products
        if brand:
            result = [p for p in result if p.brand == brand]
        if max_price:
            result = [p for p in result if p.price <= max_price]
        return result

    def get_detail(self, product_id: int) -> Optional[Product]:
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None

class WebApp:
    def __init__(self, repository: ProductRepository):
        self.repo = repository

    def load_home(self):
        return self.repo.get_latest_products()

    def search_products(self, keyword: str, brand: Optional[str], max_price: Optional[int]):
        result = self.repo.search(keyword)
        return sorted(self.repo.filter(result, brand, max_price), key=lambda x: x.price)

    def show_detail(self, product_id: int):
        return self.repo.get_detail(product_id)

class User:
    def __init__(self, app: WebApp):
        self.app = app

    def run(self):
        print("📲 쇼핑몰 접속")
        latest = self.app.load_home()
        print("🛒 최신 상품 리스트:")
        for p in latest:
            print("-", p)

        print("\\n🔍 '마우스' 검색 + 로지텍 브랜드 + 가격 ≤ 30000원")
        filtered = self.app.search_products("마우스", "로지텍", 30000)
        for p in filtered:
            print("🎯 검색결과:", p)

        if filtered:
            detail = self.app.show_detail(filtered[0].product_id)
            print("\\n📄 상세 페이지:")
            print("📝", detail)

repo = ProductRepository()
app = WebApp(repo)
user = User(app)
user.run()
"""
original_result = analyze_code(original_code, "기존 구조")

# 결과 통합 및 시각화
comparison_df = pd.DataFrame([modular_result, original_result])
import ace_tools as tools; tools.display_dataframe_to_user("구조별 응집도/결합도 비교", comparison_df)
