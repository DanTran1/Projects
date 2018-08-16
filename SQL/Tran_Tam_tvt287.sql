/* 1 */
SELECT product_code, product_name, list_price, discount_percent
FROM products
ORDER BY list_price DESC;

/* 2 */
SELECT last_name || ', ' || first_name as full_name
FROM customers_mgs
WHERE last_name LIKE 'E%' OR last_name LIKE 'G%' OR last_name LIKE 'H%'
ORDER BY last_name ASC;

/* 3 */
SELECT product_name, list_price, date_added 
FROM products
WHERE list_price BETWEEN 500 AND 2000
ORDER BY date_added DESC;

/* 4 */
SELECT product_name, 
       list_price, 
       discount_percent, 
       list_price * (discount_percent/100) AS discount_amount,
       list_price - (list_price * (discount_percent/100)) AS discount_price
FROM products
WHERE ROWNUM <= 5
ORDER BY discount_price DESC;

/* 5 */
SELECT item_id,
       item_price,
       discount_amount,
       quantity,
       item_price * quantity AS price_total,
       discount_amount * quantity AS discount_total,
       (item_price - discount_amount) * quantity AS item_total
FROM order_items
ORDER BY item_total DESC
FETCH FIRST 6 ROWS ONLY;

SELECT item_id,
       item_price,
       discount_amount,
       quantity,
       item_price * quantity AS price_total,
       discount_amount * quantity AS discount_total,
       (item_price - discount_amount) * quantity AS item_total
FROM (SELECT *
      FROM order_items
      ORDER by (item_price - discount_amount) * quantity DESC)
WHERE ROWNUM <= 6;
    
/* 6 */   
SELECT order_id,
       order_date,
       ship_date
FROM orders_mgs
WHERE ship_date IS NULL;

/* 7 */
SELECT SYSDATE AS today_unformatted,
       TO_CHAR(SYSDATE, 'MM-DD-YYYY') AS today_formatted
FROM Dual;

/* 8 */    
SELECT 100 AS price,
       .07 AS tax_rate,
       100 * .07 AS tax_amount,
       (100 * .07) + 100 AS total
FROM Dual;
      



       
       



