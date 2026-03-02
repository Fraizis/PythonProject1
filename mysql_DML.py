# DML

# -- ОЧЕНЬ ОПАСНО! WHERE отсутствует!
# DELETE FROM Products;

# UPDATE Products
# SET Price = 1000;


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


# INSERT INTO missions (
#     id,
#     name,
#     planet,
#     captain
# )
# VALUES (
#     1,
#     'Mars Search',
#     'Mars',
#     'John'
# );


# SELECT MIN(YEAR(birthday))
# FROM users;

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
# FROM group_messages
# GROUP BY group_id
# HAVING cnt > 50
# ORDER BY cnt DESC;


# SELECT IF (1 = 2, 'TRUE', 'FALSE');


# OFFSET - количество строк, которые нужно пропустить перед началом возврата строк из результата запроса
# -- первая страница (пользователи с 1 по 5)
# SELECT *
# FROM users
# ORDER BY id
# LIMIT 5 OFFSET 0;


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
