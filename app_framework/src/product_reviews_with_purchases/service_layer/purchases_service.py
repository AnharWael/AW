from app_framework.src.product_reviews_with_purchases.persistence_layer.purchases_repository import PurchasesRepository


class PurchasesService:
    def __init__(self, repo: PurchasesRepository):
        self.repo = repo

    def list_all_purchases(self):
        """
        Returns all purchases with user name, product name, and purchase date.
        """
        return self.repo.get_all_purchases()