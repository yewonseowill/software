from webapp import WebApp

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