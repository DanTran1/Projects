/* 1 */
INSERT INTO categories
    (category_id, category_name)
VALUES
    (5, 'Woodwinds');

/* 2 */  
UPDATE categories
SET category_name = 'Brass'
WHERE category_id = 5;

/* 3 */
INSERT INTO products
    (product_id, category_id, product_code,
     product_name, description, list_price,
     discount_percent, date_added)
VALUES
    (11, 5, 'yas_480', 
     'Yamaha YAS-480 Saxophone', 'Long description to come.', 799.99,
     0, SYSDATE);

/* 4 */     
UPDATE products
SET discount_percent = 35
WHERE product_id = 11;

/* 5 */
DELETE FROM products
WHERE category_id = 5;

DELETE FROM categories
WHERE category_id = 5;

COMMIT;
