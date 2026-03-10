# базовый вариант команды INSERT

# INSERT INTO missions (id, name, planet, captain)
# VALUES (1, 'Mars Search', 'Mars', 'John');


# пакетная вставка данных - работает быстро

# INSERT INTO users (firstname, lastname, email, phone) VALUES
# ('Ozella', 'Hauck', 'idickens@example.com', '9773438197'),
# ('Emmet', 'Hammes', 'qcremin@example.org', '9694110645'),
# ('Lori', 'Koch', 'damaris34@example.net', '9192291407'),
# ('Sam', 'Kuphal', 'telly.miller@example.net', '9917826315');


# Проигнорировать повторяющиеся значения

# INSERT IGNORE INTO missions (id, name, planet, captain)
# VALUES (1, 'Mars Search', 'Mars', 'John');


# Скопировать данные из одной таблицы в другую

# INSERT INTO users(firstname,lastname,email)
# SELECT firstname, lastname, email
# FROM sakila.staff;



# Обновить данные при совпадении первичного ключа

# INSERT INTO users (id, firstname, lastname, email, phone)
# VALUES (2, 'Luci', 'Rolfson', 'John@exm.ru', 123456789)
# ON DUPLICATE KEY UPDATE
#   firstname = 'Luci',
#   lastname = 'Rolfson',
#   email = 'John@exm.ru',
#   phone = 123456789;


# скопировать в таблицу Ordersnew все заказы, которые были созданы после 08.02.2013 из таблицы Orders

# insert into Ordersnew(order_num, order_date, cust_id)
# select order_num, order_date, cust_id
# from Orders
# where order_date > '2013-02-08';


# Вставка данных с преобразованием или вычислениями

# расчитаем в новой таблице OrderItemsnew итоговую стоимость товаров за партию,
# но только для тех, где количество = 100

# INSERT INTO OrderItemsnew(order_date, total_amount)
# SELECT CURRENT_DATE, item_price * quantity
# FROM OrderItems
# WHERE OrderItems.quantity = 100;
