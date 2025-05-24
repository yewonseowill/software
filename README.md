# 🌟 소프트웨어 공학 - 개인과제

- '일상속 상품 검색 기능'을 구현한 프로젝트

---

## 1. 프로젝트 개요

* 사용자가 상품을 검색하고 조건만출 (브랜드 / 가격) 후 검색결과 보기
* 반환된 검색 결과에서 하나를 선택하여 상세정보 확인

---

## 2. 프로젝트 프로세스 플로우차트 (Mermaid Flowchart)

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

```


### 사용 클래스:



### 구현 목적:



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

## 5.

| 키점     | 가지가 있다         | 판단 |
| ------ | -------------- | -- |
| 개발 단순성 | 클래스 3개 이하      | 가능 |
| 유지법    | 클래스간 가능한 최소 가열 | 가능 |
| 검증효    | 다양한 검증자 만들기 여유 | 가능 |

---

## 6. 결론

---
