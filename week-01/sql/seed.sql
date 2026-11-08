-- Чистим и наполняем users (12 строк)
TRUNCATE orders, users RESTART IDENTITY CASCADE;

INSERT INTO users (name, city, age) VALUES
('Alice',   'Moscow',  28),
('Bob',     'Moscow',  35),
('Carol',   'Kazan',   22),
('Dave',    'Kazan',   41),
('Eve',     'Moscow',  19),
('Frank',   'SPb',     33),
('Grace',   'SPb',     27),
('Heidi',   'Kazan',   38),
('Ivan',    'Moscow',  45),
('Judy',    'SPb',     24),
('Karl',    'Moscow',  31),
('Laura',   'Kazan',   29);

INSERT INTO orders (user_id, amount, created_at) VALUES
(1, 100.00, CURRENT_DATE - INTERVAL '5 days'),
(1, 250.50, CURRENT_DATE - INTERVAL '20 days'),
(2,  75.00, CURRENT_DATE - INTERVAL '2 days'),
(2, 400.00, CURRENT_DATE - INTERVAL '40 days'),
(3, 120.00, CURRENT_DATE - INTERVAL '10 days'),
(4, 999.99, CURRENT_DATE - INTERVAL '1 day'),
(4,  50.00, CURRENT_DATE - INTERVAL '60 days'),
(5, 300.00, CURRENT_DATE - INTERVAL '15 days'),
(6, 180.00, CURRENT_DATE - INTERVAL '25 days'),
(7,  90.00, CURRENT_DATE - INTERVAL '7 days'),
(9, 500.00, CURRENT_DATE - INTERVAL '3 days'),
(9, 650.00, CURRENT_DATE - INTERVAL '12 days'),
(10, 210.00, CURRENT_DATE - INTERVAL '8 days'),
(11, 130.00, CURRENT_DATE - INTERVAL '45 days'),
(12, 470.00, CURRENT_DATE - INTERVAL '18 days');
-- Пользователи без заказов: id = 8 (Heidi)