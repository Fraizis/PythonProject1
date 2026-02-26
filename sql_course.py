# DDL
# CREATE, ALTER, DROP

# удалить базу данных:
# DROP DATABASE IF EXISTS telegram;

# создать базу данных:
# CREATE SCHEMA telegram;
# CREATE DATABASE telegram;

# переключиться на указанную БД:
# USE telegram;

# удалить таблицу
# DROP TABLE IF EXISTS users;

# создать таблицу:
# CREATE TABLE users(
#     id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     # id SERIAL, # BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
#     firstname VARCHAR(100),
#     lastname VARCHAR(100) COMMENT 'фамилия',
#     login VARCHAR(100),
#     email VARCHAR(100) UNIQUE,
#     password_hash VARCHAR(256),
#     phone BIGINT UNSIGNED UNIQUE,

#     INDEX idx_users_username(firstname, lastname)

#) COMMENT 'пользователи';
