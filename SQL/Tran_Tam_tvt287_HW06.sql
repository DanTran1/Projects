/* 1 */

SELECT DISTINCT category_name
FROM categories
WHERE category_id IN 
      (SELECT category_id
       FROM products)
ORDER BY category_name;

/* 2 */
SELECT product_name, list_price
FROM products
WHERE list_price > 
     (SELECT AVG(list_price)
      FROM products)
ORDER BY list_price DESC;

/* 3 */
SELECT p1.product_name, p1.discount_percent
FROM products p1
WHERE p1.discount_percent NOT IN 
      (SELECT p2.discount_percent
       FROM products p2
       WHERE p1.product_name <> p2.product_name)
ORDER BY p1.product_name;

/* 4 */
SELECT vendor_name, vendor_city, vendor_state
FROM vendors
WHERE vendor_state || vendor_city NOT IN
     (SELECT vendor_state || vendor_city
      FROM vendors
      GROUP BY vendor_state || vendor_city
      HAVING COUNT(*) > 1);




