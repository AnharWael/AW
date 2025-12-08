from app_framework.src.product_reviews_with_purchases.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
from app_framework.src.product_reviews_with_purchases.persistence_layer.purchases_repository import PurchasesRepository
from app_framework.src.product_reviews_with_purchases.service_layer.purchases_service import PurchasesService
from app_framework.src.product_reviews_with_purchases.presentation_layer.console_ui import show_all_purchases_menu


def main():
    # Set up database connection wrapper
    db = MySQLPersistenceWrapper()

    # Create repository and service objects
    repo = PurchasesRepository(db)
    service = PurchasesService(repo)

    # Start the console menu
    show_all_purchases_menu(service)


if __name__ == "__main__":
    main()