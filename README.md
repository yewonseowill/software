# 🌟 소프트웨어공학 - 개인 실습 과제

- '일상 속 상품 검색 기능'을 구현한 프로젝트



---

## 1. 프로젝트 개요

* 사용자가 상품을 검색하고 조건(브랜드 / 가격)에 맞는 검색결과 보기
* 반환된 검색 결과에서 하나를 선택하여 상세정보 확인
  
<img width="690" alt="스크린샷 2025-05-24 오후 1 35 39" src="https://github.com/user-attachments/assets/e20d83c5-2a48-4be9-951a-35b2b74ecbea" />

---

## 2. 프로젝트 프로세스 플로우차트 (Mermaid Flowchart)


## 🔗 Mermaid 시퀀스 다이어그램

[▶ Mermaid 다이어그램 열기](https://www.mermaidchart.com/play?utm_source=mermaid_live_editor&utm_medium=toggle#pako:eNqdVE1rGlEU_SsXIZBAYk3TlbSBBjfuCkW6cWPNUFzUWDXdlIIfk9RE02gaW6OjjCU1pDVlohMwIPS_dDnvvv_Qq-9px4xjSmc1zJx77znnvvPeeaI724rH70kpb3aVeFQJxCKvkpHX4TjQs7QEmOti_RJb5VVAXcWeCZjP8pMCYNvg9RL83j8Bq5fB_MH4FfUq07sPeFXlqiG-5LOoDoD1TWtgWLclvMhgszZpxptl1lHDcTEvEUmmY9FYIhJPQyilJCGS-kvACXmhvHyaSIxBH4a8WmHfDcDGLVavYTkUXHEWPFeSb2VXVWM91Yl4ltzZ3o2mA1tjkFAa2JrwIz983js-sE4XD8_54QDQLJBEYG2NfdJEwUjE2uamIOq309QruH8kQOIvwQQ9v_uA-in2rkSRwFLRlDHV3WhY1Cd16z7L0OSaRM0UumYfdneKqGNGjZ_VZmbZhbgxbFZY8WZGFlWNXPBDKIhfyrPkeIUIazZ3173AT0us9YMfD2lHOs835xv5S-elNvCsyTpXbi5KzFkBtSEtZUSTFc-xaTL9gMjaxj70yjM8d1jYw7omkQF2UcC6QVLDHonHz2RCa4_p31xIyGiIzcGyrUpXWbG74r5MnjvHRolOEtChom3M5m7BQuVIq2dY_eF0j1OtG14ZUvp1DDKoqGcpZC7qLSNj9S6B5X5iMwNY0Ei-bLFgReTagDY5ysITcp9iz_eOVkE2ewwbPnqwUaZmExK2ZnMy4eDcNqzriZELQjGBjRQCb6hTI1vd-8Mxc52JHqysOQ6-a04okV_3_icncn2OhDzyzt6o8-MhFQog_1ijQ08LuCcvoigYuNdSXjVZ8XY6hTzqm_980UhSosrVNztooVtOjWPHPO__AAJKRJI)

:white_check_mark:
 **Mermaid실행 화면**

<img width="1368" alt="스크린샷 2025-05-24 오후 1 37 05" src="https://github.com/user-attachments/assets/5f5ef3a1-65af-4fb1-97af-acebc76295c8" />
<br>
<br>

:white_check_mark:
 **Mermaid SequenceDiagram 화면**

<img width="467" alt="스크린샷 2025-05-24 오후 1 30 14" src="https://github.com/user-attachments/assets/8e92ced7-b5c0-4fd0-a917-251f5b599f23" />

```mermaid
sequenceDiagram
    %% 사용자, 전체 상품 조회 → 검색 → 정렬/필터 → 상세 보기까지의 전체 흐름

    participant User as 사용자
    participant WebApp as 쇼핑몰 웹앱 (UI)
    participant Server as 서버
    participant ProductDB as 상품 DB

    %% 0. 전체 상품 리스트 초기 로드
    User->>WebApp: 쇼핑몰 접속
    WebApp->>Server: 전체 상품 리스트 요청
    Server->>ProductDB: 최신 상품 10개 조회
    ProductDB-->>Server: 상품 리스트 10개 반환
    Server-->>WebApp: 전체 상품 리스트 응답
    WebApp-->>User: UI에 상품 10개 표시

    %% 1. 플랫폼 선택
    User->>WebApp: 쿠팡 클릭
    WebApp->>Server: 쿠팡 홈으로 리다이렉트

    %% 2. 검색
    User->>WebApp: "무선 마우스" 검색어 입력
    WebApp->>Server: 검색 요청 (검색어 전달)
    Server->>ProductDB: 키워드 기반 상품 조회
    ProductDB-->>Server: 검색 결과 반환

    %% 3. 정렬 및 필터 적용
    User->>WebApp: "가격 낮은 순" 정렬 선택
    User->>WebApp: "브랜드 = 로지텍, 가격 < 30000원" 필터 선택
    WebApp->>Server: 정렬 및 필터 조건 전달
    Server->>ProductDB: 조건 적용 후 상품 재조회
    ProductDB-->>Server: 정렬/필터 적용된 상품 리스트
    Server-->>WebApp: 최종 상품 리스트 응답
    WebApp-->>User: UI에 결과 표시

    %% 4. 상세 보기
    User->>WebApp: 상품 상세 페이지 클릭
    WebApp->>Server: 상품 ID 전달
    Server->>ProductDB: 해당 상품 정보 조회
    ProductDB-->>Server: 상품 상세 정보
    Server-->>WebApp: 상세 정보 응답
    WebApp-->>User: 상세 페이지 표시
```

---

## 3. 구현을 위한 파이썬 코드
```
# shopping_flow.py

from typing import List, Optional  # 타입 힌트를 위한 모듈

# ✅ 상품 클래스: 개별 상품의 정보를 저장하는 객체
class Product:
    def __init__(self, product_id: int, name: str, brand: str, price: int):
        self.product_id = product_id  # 상품 고유 ID
        self.name = name              # 상품 이름
        self.brand = brand            # 브랜드명
        self.price = price            # 가격

    def __repr__(self):
        # 상품 정보를 문자열로 표현할 때 사용
        return f"{self.name} ({self.brand}) - {self.price}원"

# ✅ 상품 저장소 클래스: 상품 목록을 보관하고 검색/필터/조회 기능 제공
class ProductRepository:
    def __init__(self):
        # 초기 상품 10개를 리스트에 저장
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

    # 전체 또는 최신 상품 일부 반환
    def get_latest_products(self, count: int = 10) -> List[Product]:
        return self.products[:count]

    # 키워드가 포함된 상품 검색
    def search(self, keyword: str) -> List[Product]:
        return [p for p in self.products if keyword in p.name]

    # 브랜드 및 가격 필터링
    def filter(self, products: List[Product], brand: Optional[str], max_price: Optional[int]) -> List[Product]:
        filtered = products
        if brand:
            filtered = [p for p in filtered if p.brand == brand]
        if max_price:
            filtered = [p for p in filtered if p.price <= max_price]
        return filtered

    # 상품 ID로 상세 정보 조회
    def get_detail(self, product_id: int) -> Optional[Product]:
        for p in self.products:
            if p.product_id == product_id:
                return p
        return None

# ✅ 웹 앱 클래스: 저장소를 통해 사용자 요청을 처리
class WebApp:
    def __init__(self, repository: ProductRepository):
        self.repo = repository  # 저장소 주입

    # 메인 페이지용 최신 상품 불러오기
    def load_home(self):
        return self.repo.get_latest_products()

    # 검색 + 필터 + 정렬 처리
    def search_products(self, keyword: str, brand: Optional[str], max_price: Optional[int]):
        result = self.repo.search(keyword)
        return sorted(self.repo.filter(result, brand, max_price), key=lambda x: x.price)

    # 상품 ID로 상세 정보 반환
    def show_detail(self, product_id: int):
        return self.repo.get_detail(product_id)

# ✅ 사용자 클래스: 실제 사용자가 서비스를 이용하는 흐름을 시뮬레이션
class User:
    def __init__(self, app: WebApp):
        self.app = app

    def run(self):
        print("📲 쇼핑몰 접속")

        # 홈에 접속했을 때 최신 상품 목록 출력
        latest = self.app.load_home()
        print("🛒 최신 상품 리스트:")
        for p in latest:
            print("-", p)

        # '마우스' 검색 후 필터 적용
        print("\n🔍 '마우스' 검색 + 로지텍 브랜드 + 가격 ≤ 30000원")
        filtered = self.app.search_products("마우스", "로지텍", 30000)
        for p in filtered:
            print("🎯 검색결과:", p)

        # 검색 결과 중 첫 번째 상품 상세 보기
        if filtered:
            detail = self.app.show_detail(filtered[0].product_id)
            print("\n📄 상세 페이지:")
            print("📝", detail)

# ✅ 메인 실행 로직
if __name__ == "__main__":
    repo = ProductRepository()  # 저장소 생성
    app = WebApp(repo)          # 웹앱 생성 (저장소 주입)
    user = User(app)            # 사용자 생성 (웹앱 주입)
    user.run()                  # 시뮬레이션 실행

```

🔗 [Google Colab Code Link](https://colab.research.google.com/drive/1-5BSQHrmf6QDwBGMkTixB7D0aH5T5tDb?usp=sharing)

<img width="1030" alt="스크린샷 2025-05-24 오후 2 11 01" src="https://github.com/user-attachments/assets/743d5b70-0068-4971-b131-b35e6087927d" />

:white_check_mark:
 **실행결과**

<img width="459" alt="스크린샷 2025-05-24 오후 1 31 38" src="https://github.com/user-attachments/assets/436cf4b9-8ca3-438d-99e0-a7617592a5dd" />

---

## 4. 파이썬 코드 클래스 구조

```plaintext
shopping_flow.py
|
|│-- Product: 상품의 정보 (이름, 가격, 브랜드)
|│-- ProductStore: 전체/검색/필터/상세 조회 가능
|│-- User: 가입 행동을 시루리얼로 실행
```

---

## 5. 응집도/결합도 
⸻

🧠 응집도 및 결합도 평가

✅ **응집도(Cohesion) 평가**
<br>
<img width="810" alt="스크린샷 2025-05-24 오후 2 47 55" src="https://github.com/user-attachments/assets/8dfd1e8d-cd57-4b9b-9ccc-69f4b2d70ac9" />

📌 모든 클래스가 하나의 책임에 집중하여 유지보수가 매우 쉬운 구조임.

⸻

🔗 **결합도(Coupling) 평가**
<br>
<img width="814" alt="스크린샷 2025-05-24 오후 2 49 23" src="https://github.com/user-attachments/assets/60425e3c-8258-48bd-b935-ed195d1268da" />

📌 클래스 간 의존성이 낮은 편이나, 추상화 인터페이스가 도입되면 결합도를 더 낮출 수 있음.

⸻

📊 **종합 평가 요약**
<br>
<img width="727" alt="스크린샷 2025-05-24 오후 2 50 25" src="https://github.com/user-attachments/assets/cc0f86af-edad-4561-bdc8-24fdd9397ca7" />


⸻

💡 **개선 아이디어**
- ProductRepository를 인터페이스(ProductStoreInterface)로 추상화하여 WebApp이 인터페이스에 의존하도록 개선
- User 클래스가 WebApp에만 의존하지 않도록 서비스 계층 또는 컨트롤러 분리 시 확장성 향상 가능

⸻
# 🛍 개선된 Python 쇼핑몰 검색 시스템

Python으로 구현된 본 프로젝트는 구조 개선을 통해 **응집도는 유지하면서 결합도는 낮춘 예제**

---

## 📁 프로젝트 구조

```plaintext
shopping_flow/
├── product.py             # Product 클래스 정의
├── store_interface.py     # ProductStoreInterface 정의 (추상화)
├── repository.py          # ProductRepository 구현체
├── webapp.py              # WebApp 로직 처리 (인터페이스에 의존)
├── service.py             # AppService 계층 (사용자 흐름 실행)
└── main.py                # 실행 진입점
```

---

## ⚙️ 설계 변경 요약

| 변경 항목      | 개선 전                    | 개선 후                          | 효과            |
| ---------- | ----------------------- | ----------------------------- | ------------- |
| WebApp 의존성 | ProductRepository 직접 의존 | ProductStoreInterface 추상화에 의존 | 결합도 감소        |
| 사용자 흐름     | User → WebApp           | AppService 계층 추가              | 계층 분리, 확장성 향상 |

---

## 📌 응집도 평가 (Cohesion)
<br>
<img width="1022" alt="스크린샷 2025-05-24 오후 2 51 12" src="https://github.com/user-attachments/assets/f8e8fc3c-7b8d-4c3d-924c-ef75bab8a1af" />

---

## 🔗 결합도 평가 (Coupling)
<br>
<img width="1088" alt="스크린샷 2025-05-24 오후 2 52 26" src="https://github.com/user-attachments/assets/50d57065-0b0b-48fc-8419-223e09e78638" />


📌 **총평:** 클래스 간 의존성이 낮고, 추상화 인터페이스 도입으로 테스트 용이성과 재사용성, 유지보수성이 우수함

---

## 📊 종합 평가 요약
<br>
<img width="781" alt="스크린샷 2025-05-24 오후 2 53 30" src="https://github.com/user-attachments/assets/37e5dab2-f80e-47ba-8e28-4ff623e8ff79" />


---

## ✅ 실행 예시

```bash
$ python main.py
📲 쇼핑몰 접속
🛒 최신 상품 리스트:
- 로지텍 무선 마우스 (로지텍) - 25000원
...
🔍 '마우스' 검색 + 로지텍 브랜드 + 가격 ≤ 30000원
🎯 검색결과: 로지텍 무선 마우스 (로지텍) - 25000원
📄 상세 페이지:
📝 로지텍 무선 마우스 (로지텍) - 25000원
```


---

```
from typing import List, Optional, Protocol

# 상품 클래스
class Product:
    def __init__(self, product_id: int, name: str, brand: str, price: int):
        self.product_id = product_id
        self.name = name
        self.brand = brand
        self.price = price

    def __repr__(self):
        return f"{self.name} ({self.brand}) - {self.price}원"

# 추상 인터페이스
class ProductStoreInterface(Protocol):
    def get_latest_products(self, count: int) -> List[Product]: ...
    def search(self, keyword: str) -> List[Product]: ...
    def filter(self, products: List[Product], brand: Optional[str], max_price: Optional[int]) -> List[Product]: ...
    def get_detail(self, product_id: int) -> Optional[Product]: ...

# 구현체
class ProductRepository(ProductStoreInterface):
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

# WebApp 클래스
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

# 사용자 흐름 담당 서비스 계층
class AppService:
    def __init__(self, app: WebApp):
        self.app = app

    def simulate_user_flow(self):
        print("📲 쇼핑몰 접속")
        for p in self.app.load_home():
            print("🛒", p)

        print("\n🔍 '마우스' 검색 + 로지텍 브랜드 + 가격 ≤ 30000원")
        filtered = self.app.search_products("마우스", "로지텍", 30000)
        for p in filtered:
            print("🎯", p)

        if filtered:
            print("\n📄 상세 페이지:")
            print("📝", self.app.show_detail(filtered[0].product_id))

# 실행부
if __name__ == "__main__":
    store = ProductRepository()
    web_app = WebApp(store)
    service = AppService(web_app)
    service.simulate_user_flow()

```
 
💢  ## 결합도/응집도 비교 테스트
---
```
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

```
☑️ **기존/개선된 코드의 응집도/결합도 비교**
<br>
<img width="799" alt="스크린샷 2025-05-24 오후 8 19 00" src="https://github.com/user-attachments/assets/879f9c3e-c25d-4f8d-b3fe-2907aa6da047" />
<br>

<img width="686" alt="스크린샷 2025-05-24 오후 3 12 48" src="https://github.com/user-attachments/assets/3518d851-cdf8-4a4a-86a9-bbacbdfc39ec" />

☑️ **그래프**
![Comparison of Cohesion and Coupling between Structures](https://github.com/user-attachments/assets/f92c7ee2-39c5-4db4-8e07-936102e24764)



## 6. 결론
## 🔍 개선 포인트 요약

* ✅ 의존성 주입 + 추상화(인터페이스)를 활용
* ✅ 사용자 흐름을 서비스 계층으로 분리해 테스트, 유지보수 용이
* ✅ 개선 구조는 클래스 수와 메서드 수가 증가했지만, 구조 분리가 명확하며 유지보수성이 높음
* ✅ 응집도는 개선 구조가 역할 분리를 통해 높은 수준을 유지함
* ✅ 결합도는 인터페이스 도입 덕분에 개선 구조가 더 낮음 → 유연한 구조
* ✅ 클래스 간 책임을 명확히 분리하고, 추상화를 도입하여 유지보수성과 확장성을 강화한 구조
---
