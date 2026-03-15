# DML

# INSERT, SELECT, UPDATE, DELETE


# Порядок ключевых слов в нем строго определен:
#     SELECT [ DISTINCT ] <список_столбцов> [ AS <псевдонимы> ]
#     FROM <имя_таблицы>
#     [ JOIN <другая_таблица> ON <условие_связи> ] (это мы изучим в следующем модуле)
#     WHERE <условие_фильтрации_строк>
#     GROUP BY <столбцы_группировки>
#     HAVING <условие_фильтрации_групп>
#     ORDER BY <столбцы_сортировки>
#     LIMIT <ограничение_вывода>


# -- ОЧЕНЬ ОПАСНО! WHERE отсутствует!
# DELETE FROM Products;

# UPDATE Products
# SET Price = 1000;


# UPDATE

# Безопасный рабочий процесс перед UPDATE:
#   WHERE
#     Проверка:
#       SELECT *
#       FROM Products
#       WHERE ProductID = 3;
#       (убедились, что нашли нужную строку).

#     Выполнение:
#       UPDATE Products
#       SET Price = 1000
#       WHERE ProductID = 3;
#       (теперь мы уверены в условии).

# UPDATE channels
# SET title = 'Все про SQL'
# WHERE owner_user_id = 15 AND id = 35;


# UPDATE Ordersnew
# SET order_date = CASE order_num
#   WHEN 20010 THEN '2025-08-02'
#   WHEN 20011 THEN '2025-08-03'
#   WHEN 20012 THEN '2025-08-04'
#   ELSE order_date
# END
# WHERE order_num IN (20010, 20011, 20012);


# SELECT MIN(YEAR(birthday))
# FROM users;


# SELECT IF (1 = 2, 'TRUE', 'FALSE');


# -- использование условий IF в SELECT запросе
# -- выводит тип канала в зависимости от значения поля is_private
# SELECT
#     is_private ,
#     IF (is_private = 1, 'private', 'public') AS publicity,
#     title
# FROM channels;


# -- оператор ветвления CASE
# -- выполняет то же, что и в предыдущих 2 запросах
# SELECT
#     is_private ,
#     CASE(is_private)
#         WHEN 0 THEN 'public'
#         WHEN 1 THEN 'private'
#         ELSE 'not set'
#     END AS publicity,
#     title
# FROM channels;


# GROUP BY

# OFFSET - количество строк, которые нужно пропустить перед началом возврата строк из результата запроса
# -- первая страница (пользователи с 1 по 5)
# SELECT *
# FROM users
# ORDER BY id
# LIMIT 5 OFFSET 0;


# -- самый популярный канал по кол-ву пользователей
# SELECT
#     count(*) AS cnt,
#     channel_id
# FROM channel_subscribers
# GROUP BY channel_id
# ORDER BY cnt DESC
# LIMIT 1;


# -- то же, но с учетом статуса подписки
# SELECT
#     count(*) AS cnt,
#     channel_id
# FROM channel_subscribers
# WHERE status = 'joined'
# GROUP BY channel_id
# ORDER BY cnt DESC
# LIMIT 1;


# SELECT
# 	COUNT(*) as cnt,
# 	group_id
# FROM
#   group_messages
# GROUP BY
#   group_id
# HAVING
#   cnt > 50
# ORDER BY
#   cnt DESC;


# SELECT
# COUNT(*) as count,
#      CASE(views_count >= 1000)
# 	     WHEN 1 THEN 'popular'
# 	     WHEN 0 THEN 'not popular'
#      END AS is_popular
# FROM stories
# GROUP BY is_popular;


# -- количество пользователей в каждом году
# SELECT
#     COUNT(*),
#     YEAR(birthday) AS birth_year
# FROM users
# GROUP BY birth_year;


# Посчитать общую сумму продаж для категорий Hardware и Software и
# вывести их в отдельных столбцах в одной строке.
#
# Запрос с условной агрегацией:
#
# SELECT
#     SUM(CASE WHEN product_category = 'Hardware' THEN sale_amount ELSE 0 END) AS hardware_sales,
#     SUM(CASE WHEN product_category = 'Software' THEN sale_amount ELSE 0 END) AS software_sales
# FROM
#     sales;


# Другой пример с COUNT:
# Можно посчитать количество товаров в каждой категории.
#
# SELECT
#     COUNT(CASE WHEN product_category = 'Hardware' THEN 1 END) AS hardware_items,
#     COUNT(CASE WHEN product_category = 'Software' THEN 1 END) AS software_items
# FROM
#     sales;


# Отсортировать задачи в особом порядке

# SELECT *
# FROM tasks
# ORDER BY
#     CASE
#         WHEN status = 'In Progress' THEN 1
#         WHEN status = 'New' THEN 2
#         WHEN status = 'Done' THEN 3
#     END;


# -- подсчет количества пользователей в каждом поколении
# SELECT
#     COUNT(*) AS cnt,
#     CASE
#         WHEN year(birthday) >= 1945 AND year(birthday) <= 1965 THEN 'baby boomer'
#         WHEN year(birthday) >= 1966 AND year(birthday) <= 1980 THEN 'generation X'
#         WHEN year(birthday) >= 1981 AND year(birthday) <= 1995 THEN 'millenial'
#         WHEN year(birthday) >= 1996 AND year(birthday) <= 2011 THEN 'generation Z'
#         WHEN year(birthday) >= 2012 THEN 'alpha'
#     END AS generation
# FROM users
# GROUP BY generation
# ORDER BY min(YEAR(birthday))
# # ORDER BY cnt DESC ;


# -- то же, но с использованием функции BETWEEN
# SELECT
#     count(*) AS cnt,
#     CASE
#         WHEN year(birthday) BETWEEN 1945 AND 1965 THEN 'baby boomer'
#         WHEN year(birthday) BETWEEN 1966 AND 1980 THEN 'generation X'
#         WHEN year(birthday) BETWEEN 1981 AND 1995 THEN 'millenial'
#         WHEN year(birthday) BETWEEN 1996 AND 2011 THEN 'generation Z'
#         WHEN year(birthday) > 2011 THEN 'alpha'
#     END AS generation
# FROM users
# GROUP BY generation
# ORDER BY min(YEAR(birthday))


# SELECT *
# FROM saved_messages
# WHERE user_id = 5 and body LIKE '%список покупок%'


# SELECT COUNT(*)
# FROM channels
# WHERE LENGTH(title) < 3;


# SELECT *
# FROM stories
# WHERE user_id IN (22, 33, 44, 55, 66)
# ORDER BY created_at;

# Функция CONCAT()
# функция, которая принимает на вход два или более аргумента и возвращает их, объединенными в одну строку.
#
# SELECT
#     CONCAT(last_name, ', ', first_name) AS full_name
# FROM
#     users;


# TRIM() — удаление пробелов с обеих сторон
# LTRIM() и RTRIM() — удаление пробелов с одной стороны
# Очистить имя пользователя от случайных пробелов по краям
#
# SELECT TRIM('  Иван Петров  ') AS cleaned_name;


# SUBSTRING() — извлечение подстроки по позиции
# LEFT() и RIGHT() — удобные функции для извлечения с начала или конца

# SELECT LEFT('CAT-12345-PROD', 3);

# SELECT id, SUBSTRING(title, 1, 30), is_private
# FROM `groups`
# WHERE is_private = 1
# ORDER BY title;


# LOCATE() — это функция в SQL, которая находит позицию первого вхождения одной строки внутри другой строки.
# Она возвращает число, которое является индексом (номером символа), с которого начинается искомая подстрока.

# SUBSTRING(
#   filename,                               -- Где вырезаем
#   LOCATE('_', filename) + 1,              -- Начало (позиция после '_')
#   LOCATE('.', filename) - LOCATE('_', filename) - 1  -- Длина (расстояние между '.' и '_')
# )


# NOW() — получение текущей даты и времени

# -- При создании нового заказа мы фиксируем точное время его создания
# INSERT INTO orders (customer_id, order_time) VALUES (123, NOW());


# CURRENT_DATE — получение только текущей даты
# -- Найти все задачи, которые должны быть выполнены сегодня
# SELECT * FROM tasks WHERE due_date = CURRENT_DATE;


# Извлечение компонентов из даты
# SELECT
#     order_date,
#     EXTRACT(YEAR FROM order_date) AS sale_year,
#     EXTRACT(MONTH FROM order_date) AS sale_month,
#     EXTRACT(DAY FROM order_date) AS sale_day
# FROM
#     sales;


# SELECT
#     order_date,
#     YEAR(order_date) AS sale_year,
#     MONTH(order_date) AS sale_month,
#     DAY(order_date) AS sale_day
# FROM
#     sales;

# Найти дату, которая будет через 7 дней после заказа (срок доставки).

# SELECT '2025-10-26'::date + INTERVAL '7 day' AS delivery_date; -- `::date` - это
# приведение к типу даты в PostgreSQL

# SELECT '2025-10-26'::date - INTERVAL '1 month' AS month_before;

# DATEDIFF(day, <дата_1>, <дата_2>)


# Найти все заказы, сделанные за последние 30 дней.
#
# SELECT *
# FROM orders
# WHERE order_date >= CURRENT_DATE - INTERVAL '30 day';


# SELECT
#     COUNT(*) AS total_trips,
#     SUM(duration_minutes) AS total_duration,
#     AVG(distance_meters) AS avg_distance
# FROM
#     scooter_trips;


# Задача:
# Посчитать, сколько пользователей живет в каждом городе.

# SELECT
#     city,
#     COUNT(*) AS users_count
# FROM
#     users
# GROUP BY
#     city;


# Задача:
# Посчитать общую сумму продаж (sale_amount) для каждого менеджера в каждом месяце.

# SELECT
#     manager_id,
#     EXTRACT(MONTH FROM sale_date) AS sale_month,
#     SUM(sale_amount) AS total_sales
# FROM
#     sales
# GROUP BY
#     manager_id,
#     sale_month
# ORDER BY -- Добавим сортировку для наглядности
#     manager_id,
#     sale_month;


# HAVING

# SELECT
#   product_id,
#   COUNT(supplier_id) AS sup_count,
#   (MAX(price) - MIN(price)) AS avg_price
# FROM
#   supplier_prices
# GROUP BY
#   product_id
# HAVING
#   sup_count >= 3 AND
#   avg_price > 50;

# SELECT
#     department,
#     AVG(salary) AS average_salary
# FROM
#     employees
# GROUP BY
#     department
# HAVING
#     AVG(salary) > 100000;


# SELECT
#     student_id,
#     AVG(score) AS avg_score
# FROM
#     exam_scores
# WHERE
#     score > 70
# GROUP BY
#     student_id
# HAVING
#     avg_score > 85;


# SELECT
#     manager_id,
#     SUM(sale_amount) AS total_sales
# FROM
#     sales
# WHERE
#     product_category = 'Hardware'
#     AND EXTRACT(MONTH FROM sale_date) < 3
# GROUP BY
#     manager_id
# HAVING
#     SUM(sale_amount) > 7000
# ORDER BY
#     total_sales DESC
# LIMIT 2;


# SELECT
#     author_id,
#     COUNT(*) AS post_count
# FROM
#     posts
# WHERE
#     category = 'Technology' AND
#     publication_date > '2024-01-01'
# GROUP BY
#     author_id
# HAVING
#     post_count > 1;


# SELECT
#     product_category,
#     SUM(sale_amount) AS total_sales,
#     '2025-01' AS 'January 2025'
# FROM
#     sales
# WHERE
#     sale_date >= '2025-01-01' AND
#     sale_date <= '2025-01-31'
# GROUP BY
#     product_category
# HAVING
#     total_sales > 5000
# ORDER BY
#     total_sales DESC;


# CROSS JOIN - работает медленно

# SELECT *
# FROM users
# CROSS JOIN private_messages
# WHERE users.id = private_messages.sender_id ;

# также CROSS JOIN

# SELECT *
# FROM users
# JOIN private_messages;


# INNER JOIN - работает эффективно

# SELECT *
# FROM users
# INNER JOIN private_messages ON users.id = private_messages.sender_id ;


# SELECT
#     C.Name,
#     O.OrderID,
#     O.OrderDate
# FROM
#     Customers AS C
# INNER JOIN
#     Orders AS O ON C.CustomerID = O.CustomerID;


# LEFT JOIN

# SELECT
#   d.dept_name
# FROM
#   departments AS d
# LEFT JOIN
#   employees AS e
#   ON d.dept_id = e.dept_id
# WHERE
#   e.emp_name IS NULL;


# LEFT JOIN = INNER JOIN

# SELECT *
# FROM users
# LEFT OUTER JOIN private_messages ON users.id = private_messages.sender_id
# WHERE private_messages.id IS NOT NULL
# ORDER BY private_messages.id;


# SELECT
#     d.dept_name,
#     COUNT(e.emp_name)
# FROM
#     departments AS d
# LEFT JOIN
#     employees AS e
#     ON e.dept_id = d.dept_id
# GROUP BY
#     d.dept_name;


# RIGHT JOIN

# SELECT e.emp_name, o.city
# FROM employees AS e
# RIGHT JOIN offices AS o ON e.office_id = o.office_id;


# SELECT o.city
# FROM employees AS e
# RIGHT JOIN offices AS o ON e.office_id = o.office_id
# WHERE e.emp_name IS NULL;


# SELECT
#     o.city,
#     COUNT(e.emp_name) AS employee_count
# FROM
#     employees AS e
# RIGHT JOIN
#     offices AS o
#     ON e.office_id = o.office_id
# GROUP BY
#     o.city;


# SELECT
#     e.emp_name, o.city
# FROM
#     offices AS o
# LEFT JOIN
#     employees AS e
#     ON e.office_id = o.office_id;
#
# SELECT
#     e.emp_name, o.city
# FROM
#     employees AS e
# RIGHT JOIN
#     offices AS o
#     ON e.office_id = o.office_id;


# CROSS JOIN

# SELECT *
# FROM users, private_messages;


# Эмуляция FULL OUTER JOIN с помощью UNION

# UNION - без повторений, только уникальные значения
# UNION ALL - все значения

# SELECT
#     e.emp_name,
#     o.city
# FROM
#     employees AS e
# LEFT JOIN
#     offices AS o
#     ON e.office_id = o.office_id
# UNION
# SELECT
#     e.emp_name,
#     o.city
# FROM
#     employees AS e
# RIGHT JOIN
#     offices AS o
#     ON e.office_id = o.office_id;


# Использование UNION ALL - самые активные в сообщениях пользователи

# SELECT
# 	count(*) AS cnt,
# 	sender_id
# FROM (
# 	SELECT sender_id
# 	FROM channel_messages
# 	UNION ALL
# 	SELECT sender_id
# 	FROM group_messages
# ) AS s
# GROUP BY sender_id
# ORDER BY cnt DESC


# JOIN 3 таблиц

# select
#     product_name
# from order_items as OI
# join
#     products as P on OI.product_id = P.product_id
# where OI.order_id = 1001;


# SELECT customer_name, order_date, product_name
# FROM customers
# JOIN orders using(customer_id)
# JOIN order_items using(order_id)
# JOIN products using(product_id);


# Самый дорогой товар купленный клиентом

# SELECT
#     p.product_name
# FROM
#     products AS p
# JOIN
#     order_items AS oi
#     ON p.product_id = oi.product_id
# JOIN
#     orders AS o
#     ON oi.order_id = o.order_id
# JOIN
#     customers AS c
#     ON o.customer_id = c.customer_id
# WHERE
#     c.customer_name = 'Иван Петров'
# ORDER BY
#     p.price DESC
# LIMIT 1;


# SELECT
#   c.customer_name,
#   SUM(oi.quantity * p.price) AS total_spent
# FROM
#   customers c
# JOIN
#   orders o USING(customer_id)
# JOIN
#   order_items oi USING(order_id)
# JOIN
#   products p USING(product_id)
# GROUP BY
#   c.customer_name;


# Подзапросы

# SELECT Name
# FROM Customers
# WHERE CustomerID IN ( -- Шаг 4: Находим имена клиентов по их ID
#     SELECT CustomerID
#     FROM Orders
#     WHERE OrderID IN ( -- Шаг 3: Находим ID заказов, в которых были нужные товары
#         SELECT OrderID
#         FROM OrderItems
#         WHERE ProductID IN ( -- Шаг 2: Находим ID товаров из нужной категории
#             SELECT ProductID
#             FROM Products
#             WHERE Category = 'Electronics' -- Шаг 1: Находим ID товаров
#         )
#     )
# );


# SELECT
#     firstname,
#     lastname,
#     birthday,
#     (SELECT app_language FROM user_settings WHERE user_id = users.id)
# FROM users
# WHERE email =  'mgoyette@example.org';


# SELECT emp_name
# FROM employees
# WHERE dept_id = (
#     SELECT dept_id
#     FROM employees
#     WHERE emp_name = 'Борис'
# )
# AND emp_name != 'Борис';


# сотрудники с самой высокой зарплатой в компании

# SELECT emp_name, salary
# FROM employees
# WHERE salary IN (
#     SELECT MAX(salary)
#     FROM employees
# );


# подзапросы из FROM

# SELECT
#     filtered_users.name -- Обращаемся к столбцу через псевдоним производной таблицы
# FROM
#     (
#         SELECT id, name, city FROM users WHERE city = 'Moscow'
#     ) AS filtered_users; -- Даем имя нашей виртуальной таблице



# Найти среднюю сумму одного заказа

# SELECT
#     AVG(order_total) AS average_order_value -- ЭТАП 2: Находим среднее от сумм
# FROM
#     (
#         -- --- Начало подзапроса (ЭТАП 1) ---
#         SELECT
#             order_id,
#             SUM(quantity * price_per_item) AS order_total
#         FROM
#             order_items
#         GROUP BY
#             order_id
#         -- --- Конец подзапроса ---
#     ) AS orders_with_totals; -- Даем имя нашей виртуальной таблице


# SELECT emp_name
# FROM (
#     SELECT emp_name, salary
#     FROM employees
#     WHERE dept_id = 1
# ) AS emp_names
# WHERE salary > 145000;


# SELECT AVG(sum_price.total_value) AS avg_order_value
# FROM (
#     SELECT SUM(quantity * price) AS total_value
#     FROM order_items
#     GROUP BY order_id
# ) AS sum_price;



# SELECT d.dept_name, ds.avg_salary
# FROM departments AS d
# JOIN (
#     SELECT
#         dept_id,
#         AVG(salary) AS avg_salary
#     FROM
#         employees
#     GROUP BY
#         dept_id
# ) AS ds
# ON d.dept_id = ds.dept_id;


# SELECT s.id, COUNT(sl.id) AS likes_count
# FROM stories AS s
# JOIN stories_likes AS sl ON s.id = sl.story_id
# WHERE s.user_id = 2
# GROUP BY s.id
# ORDER BY likes_count DESC;


# Коррелированные подзапросы

# SELECT
#     id,
#     (SELECT firstname FROM users WHERE id = group_messages.sender_id) AS firstname,
#     (SELECT lastname FROM users WHERE id = group_messages.sender_id) AS lastname,
#     SUBSTRING(body, 1, 30) AS body,
#     created_at
# FROM group_messages
# WHERE group_id = 11
# ORDER BY created_at;


# SELECT
#     name,
#     department,
#     salary
# FROM
#     employees AS e1 -- Даем псевдоним внешней таблице, это обязательно!
# WHERE
#     salary > (
#         -- --- Начало коррелированного подзапроса ---
#         SELECT AVG(salary)
#         FROM employees AS e2
#         WHERE e2.department = e1.department -- Ключевая "корреляция"!
#         -- --- Конец подзапроса ---
#     );


# SELECT
# 	COUNT(*)
# FROM private_messages
# WHERE
# 	receiver_id = (SELECT id FROM users WHERE email = 'hardy42@example.com');


# EXISTS

# SELECT ...
# FROM table1 AS t1
# WHERE EXISTS (
#     SELECT 1 FROM table2 AS t2 WHERE t2.key = t1.key -- Коррелированный подзапрос
# );


# -- Это эффективная и надежная замена LEFT JOIN ... WHERE ... IS NULL

# SELECT Name
# FROM Customers AS C
# WHERE NOT EXISTS (
#     SELECT 1
#     FROM Orders AS O
#     WHERE O.CustomerID = C.CustomerID
# );

# SELECT * FROM Orders
# WHERE EXISTS (SELECT 1 FROM Products WHERE Products.id = Orders.product_id);


# SELECT *
# FROM orders AS o1
# WHERE order_date >= (
#     SELECT MAX(order_date)
#     FROM orders AS o2
#     WHERE o2.customer_id = o1.customer_id
# );


# SELECT *
# FROM users AS u1
# WHERE EXISTS (
#     SELECT 1
#     FROM users AS u2
#     WHERE u1.email = u2.email AND u1.registration_date < u2.registration_date
# );


# SELECT dept_name
# FROM departments AS d
# WHERE EXISTS (
#     SELECT 1
#     FROM
#         employees AS e
#     WHERE
#         d.dept_id = e.dept_id AND
#         e.salary > 145000
# );


# оконные функции

# подсчет популярности яыков (с группировкой и агрегирующей функцией) с оконной функцией)

# SELECT DISTINCT
# 	COUNT(*) OVER (PARTITION BY app_language) AS cnt,
# 	app_language
# FROM user_settings;


# SELECT DISTINCT
#     s.id,
#     COUNT(sl.story_id) OVER(PARTITION BY sl.story_id) AS likes_count
# FROM stories AS s
# JOIN stories_likes AS sl ON s.id = sl.story_id
# WHERE s.user_id = 2
# ORDER BY likes_count DESC;


# WITH cte1 AS (
#     SELECT DISTINCT
#         COUNT(*) OVER(PARTITION BY reaction_id) AS `count`,
#         reaction_id
#     FROM private_message_reactions
# )
# SELECT *
# FROM cte1
# WHERE `count` > 80
# ORDER BY `count` DESC;


# оконные функции позволяют выводить любые другие поля таблицы

# SELECT DISTINCT
# 	COUNT(*) OVER (PARTITION BY app_language) AS cnt,
# 	app_language,
# 	color_scheme
# FROM user_settings;


# SELECT DISTINCT
#     user_id,
#     COUNT(channel_id) OVER(PARTITION BY user_id) AS channels_count
# FROM channel_subscribers
# WHERE status = 'joined'
# ORDER BY channels_count DESC
# LIMIT 1;


# в рамках одного запроса можно использовать несколько оконных функций

# SELECT DISTINCT
# 	ROW_NUMBER() OVER() AS rn,
# 	RANK() OVER(ORDER BY app_language) AS language_rank,
# 	DENSE_RANK() OVER(ORDER BY app_language) AS language_rank2,
# 	ROW_NUMBER() OVER(PARTITION BY app_language) AS rn2,
# 	COUNT(*) OVER (PARTITION BY app_language) AS cnt1,
# 	COUNT(*) OVER (PARTITION BY color_scheme) AS cnt2,
# 	app_language,
# 	color_scheme
# FROM user_settings
# ORDER BY app_language, rn2;


# альтернативный синтаксис (именованные оконные функции)

# SELECT DISTINCT
# 	COUNT(*) OVER win1 AS cnt,
# 	app_language
# FROM user_settings
# WINDOW win1 AS (PARTITION BY app_language);


# использование одного 'окна' вместе с разными фунциями

# SELECT
#   app_language,
#   ROW_NUMBER() OVER w AS 'row_number',
#   RANK()       OVER w AS 'rank',
#   DENSE_RANK() OVER w AS 'dense_rank'
# FROM user_settings
# WINDOW w AS (ORDER BY app_language);


# CTE

# получение данных о пользователе из разных таблиц с помощью CTE (общего табличного выражения)

# WITH cte1 AS (
# 	SELECT
# 		user_id,
# 		app_language ,
# 		is_premium_account
# 	FROM user_settings
# )
# SELECT
# 	firstname ,
# 	lastname ,
# 	app_language ,
# 	is_premium_account
# FROM cte1
# JOIN users AS u ON u.id = cte1.user_id
# WHERE id = 2
# ;


# в 1 запросе можно использовать несколько табличных выражений (у каждого из них должно быть свое уникальное имя)

# WITH cte1 AS (
# 	SELECT * FROM channel_subscribers
# ),
# cte2 AS (
# 	SELECT * FROM group_members
# )
# SELECT * FROM cte2
# ....;


# CTE recursive

# вывод иерархии сообщений (кто-кому отвечал)
# WITH RECURSIVE message_replies(id, body, history) AS (
# 	SELECT id, body, cast(id AS CHAR(100))
# 	FROM group_messages
# 	WHERE reply_to_id IS NULL
# 		UNION ALL
# 	SELECT gm.id, gm.body, CONCAT(mr.history, ' <-- ', gm.id)
# 	FROM message_replies AS mr
# 	JOIN group_messages AS gm ON mr.id = gm.reply_to_id
# )
# SELECT * FROM message_replies ORDER BY history


# Полнотекстовый поиск

# обычный фильтр с оператором WHERE-LIKE
# SELECT *
# FROM saved_messages
# WHERE body LIKE '%ratione%' OR body LIKE '%est%';


# создание полнотекстового индекса на поле body
# CREATE FULLTEXT INDEX full_body_idx ON saved_messages(body);


# полнотекстовый поиск в режиме BOOLEAN
# + обязательное слово
# - исключаемое слово
# SELECT *
# FROM saved_messages
# WHERE match(body) AGAINST('+ratione +est -voluptatem' IN BOOLEAN MODE);


# полнотекстовый поиск в режиме BOOLEAN
# * заменитель любого окончания слова
# SELECT *
# FROM saved_messages
# WHERE MATCH(body) AGAINST('+ratione +est +vol*' IN BOOLEAN MODE);


# Представления

# создать или изменить представление

# CREATE OR REPLACE VIEW v_users_messages AS
# 	SELECT
# 		users.id AS uid, firstname, lastname,
# 		private_messages.id AS pmid, sender_id, body, created_at
# 	FROM users
# 	LEFT OUTER JOIN private_messages ON users.id = private_messages.sender_id
# 	ORDER BY private_messages.id
# 	LIMIT 12;

# вывод данных через представление

# SELECT *
# FROM v_users_messages
# WHERE uid = 29;


# Процедуры

# процедура, возвращающая указанное число случайных групп или каналов
# DROP PROCEDURE IF EXISTS telegram.random_society;
#
# DELIMITER $$
# $$
# CREATE PROCEDURE telegram.random_society(cnt int)
# BEGIN
#     SELECT id, title , invite_link , 'channel' AS community_type
#     FROM channels
#         UNION
#     SELECT id, title , invite_link , 'group' AS community_type
#     FROM `groups`
#     ORDER BY rand()
#     LIMIT cnt;
# END $$
# DELIMITER ;


# вызов процедуры
# CALL random_society(3);


# Переменные

# задаем локальную переменную

# SET @users_count = 10;
# читаем значение переменной
# SELECT @users_count;

# выводим список глобальных переменных

# SHOW GLOBAL VARIABLES;

# выводим только переменную foreign_key_checks (отвечает за проверку внешних ключей)

# SHOW VARIABLES LIKE 'foreign_key_checks';

# выводим глобальное значение системной переменной

# SHOW GLOBAL VARIABLES LIKE 'foreign_key_checks';

# выводим локальное значение системной переменной

# SHOW SESSION VARIABLES LIKE 'foreign_key_checks';

# выключаем локально проверку внешних ключей

# SET @@foreign_key_checks = 0;
# SET foreign_key_checks = 0;

# выключаем глобально проверку внешних ключей

# SET GLOBAL foreign_key_checks = 0;

# присвоение значений переменным в SELECT запросе

# SELECT
# 	@id := id,
# 	@firstname := firstname
# FROM users
# WHERE id = 1;

# чтение переменных

# SELECT @id, @firstname;

# второй вариант присвоения значений переменным в SELECT запросе

# SELECT id, firstname
# INTO @id, @firstname
# FROM users
# WHERE id = 11;


# Найти 2-ую по величине зарплату, либо NULL

# SELECT
#   MAX(salary) AS SecondHighestSalary
# FROM
#   Employee
# WHERE salary < (
#   SELECT MAX(salary)
#   FROM Employee
#   );


# SELECT (
#     SELECT DISTINCT salary
#     FROM Employee
#     ORDER BY salary DESC
#     LIMIT 1 OFFSET 1
# ) AS SecondHighestSalary;
