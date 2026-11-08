SELECT name, city, age
FROM users
WHERE age > 25;

SELECT name, city, age
FROM users
WHERE city = 'Moscow' OR city = 'Kazan';

SELECT id, user_id, amount, created_at
FROM orders
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days';

SELECT SUM(amount) AS "Сумма всех заказа"
FROM orders;

SELECT 
 AVG(age) as "Средний возраст", 
 city as "Город"
FROM users
GROUP by city
ORDER BY city;

SELECT city as "Город",
AVG(age) as "Средний возраст"
FROM users
GROUP BY city
HAVING AVG(age) > 30
ORDER BY city;

SELECT o.id AS "Номер заказа",
u.name as "Имя пользователя",
o.amount as "Сумма",
o.created_at as "Дата"
FROM orders as o
INNER JOIN users as u
    ON o.user_id = u.id
ORDER BY o.id;

SELECT u.name AS "Имя пользователя",
u.city AS "Город",
u.age AS "Возраст",
o.id AS "Номер заказа",
o.amount AS "Сумма",
o.created_at AS "Дата заказа"
FROM users as u
LEFT JOIN orders as o
    ON u.id = o.user_id
ORDER BY o.id;


SELECT u.name AS "Имя пользователя",
COUNT(o.id) AS "Количество заказов"
FROM users as u
INNER JOIN orders as o
    ON u.id = o.user_id
GROUP BY u.name
ORDER BY COUNT(o.id) DESC;


SELECT u.name AS "Имя пользователя",
SUM(o.amount) AS "Итоговая сумма заказа"
FROM users as u
INNER JOIN orders as o
    ON u.id = o.user_id
GROUP BY u.name
ORDER BY SUM(o.amount) DESC
LIMIT 3;
