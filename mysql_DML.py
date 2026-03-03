# DML

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


# INSERT

# INSERT INTO missions
# (
#     id,
#     name,
#     planet,
#     captain
# )
# VALUES
# (
#     1,
#     'Mars Search',
#     'Mars',
#     'John'
# );


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


# SELECT id, SUBSTRING(title, 1, 30), is_private
# FROM `groups`
# WHERE is_private = 1
# ORDER BY title;


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
