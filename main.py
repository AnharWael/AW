import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Anhar123$',
    database='product_reviews'
)

cursor = connection.cursor()
cursor.execute("""
    SELECT u.name, p.name AS product_name, x.purchase_date
    FROM user u
    JOIN purchase_xref x ON u.user_id = x.user_id
    JOIN product p ON x.product_id = p.product_id;
""")

for row in cursor.fetchall():
    print(row)

connection.close()
    