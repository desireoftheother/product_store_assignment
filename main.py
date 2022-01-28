from src.app.app import MainApplication
from src.product.available_assortment import AvailableAssortment, AVAILABLE_OFFERS

if __name__ == "__main__":
    MainApplication(
        available_assortment=AvailableAssortment(), available_offers=AVAILABLE_OFFERS
    ).execute_application()
