from app_framework.src.product_reviews_with_purchases.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper

class PurchasesRepository:
    def __init__(self, db: MySQLPersistenceWrapper):
        self.db = db
        def get_all_purchases(self):
            query = """
                SELECT
                    u.name AS user_name,
                    p.name AS product_name,
                    x.purchase_date
                FROM purchase_xref x
                JOIN users u ON x.user_id = u.id
                JOIN products p ON x.product_id = p.id
            """
            return self.db.fetch_all(query)