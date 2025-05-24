from repository import ProductRepository
from webapp import WebApp
from service import AppService

if __name__ == "__main__":
    store = ProductRepository()
    app = WebApp(store)
    service = AppService(app)
    service.simulate_user_flow()