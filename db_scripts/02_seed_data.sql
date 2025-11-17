USE product_reviews;

DELETE FROM purchase_xref;
DELETE FROM product;
DELETE FROM user;

INSERT INTO user (name, email) VALUES
('Anna W.', 'anna@example.com'),
('Yara A.', 'yara@example.com'),
('Rozy A.', 'rozy@example.com');

INSERT INTO product (name, price) VALUES
('Creatine Monohydrate 300g', 24.99),
('Collagen Peptides 500g', 32.50),
('Protein Bar - TRUBAR (Box of 12)', 21.00),
('Hair Botox Shampoo 250ml', 18.75);

INSERT INTO purchase_xref (user_id, product_id, purchase_date) VALUES
(1, 3, '2025-10-25'),
(1, 1, '2025-10-28'),
(2, 2, '2025-11-01'),
(3, 4, '2025-11-03'),
(2, 3, '2025-11-05');