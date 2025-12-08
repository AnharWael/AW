from app_framework.src.product_reviews_with_purchases.service_layer.purchases_service import PurchasesService

class PurchasesConsoleUI:
    def __init__(self, service: PurchasesService):
        self.service = service

    def show_all_purchases(self) -> None:
        """
        Display all purchases with user name, product name, and purchase date.
        """
        rows = self.service.list_all_purchases()

        print("\nUser Purchases")
        print("-------------------------------")
        for user_name, product_name, purchase_date in rows:
            print(f"{user_name:15} | {product_name:25} | {purchase_date}")
        print()