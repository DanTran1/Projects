/** 1 **/
SELECT category_name, product_name, list_price
FROM Categories c JOIN Products p
    ON c.category_id = p.category_id
ORDER BY category_name, product_name ASC;

/** 2 **/
SELECT first_name, last_name, line1, city, state, zip_code
FROM Customers_mgs c JOIN Addresses a
    ON c.customer_id = a.customer_id
WHERE c.email_address = 'allan.sherwood@yahoo.com';

/** 3 **/
SELECT last_name, first_name, order_date, product_name, 
       item_price, discount_amount, quantity
FROM Customers_mgs c 
    JOIN Orders_mgs om ON c.customer_id = om.customer_id
    JOIN Order_items oi ON om.order_id = oi.order_id
    JOIN Products p ON oi.product_id = p.product_id
ORDER BY last_name, order_date, product_name ASC;

/** 4 **/
SELECT p1.product_name, p1.list_price
FROM Products p1 JOIN Products p2
    ON p1.list_price = p2.list_price
WHERE p1.product_name != p2.product_name
ORDER BY p1.product_name;

/** 5 **/
SELECT category_name, product_id
FROM Categories c LEFT JOIN Products p
    ON c.category_id = p.category_id
WHERE p.product_id IS NULL;

/** 6 **/
SELECT 'Shipped' AS ship_status, order_id, order_date
FROM Orders_mgs
WHERE ship_date IS NOT NULL
UNION
SELECT 'Not Shipped' AS ship_status, order_id, order_date
FROM Orders_mgs
WHERE ship_date IS NULL
ORDER BY order_date;
