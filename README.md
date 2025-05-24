# 🌟 소프트웨어 공학 - 개인과제

- '일상속 상품 검색 기능'을 구현한 프로젝트


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
    User->>WebApp: "브랜드=로지텍, 가격 < 30000원" 필터 선택
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



---

## 6. 결론

---
