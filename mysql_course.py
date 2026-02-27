# DDL
# CREATE, ALTER, DROP

# DROP DATABASE IF EXISTS telegram;
# CREATE SCHEMA telegram;
# CREATE DATABASE telegram;
# USE telegram;

# DROP TABLE IF EXISTS users;
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

# ) COMMENT 'пользователи';

# 1 x 1

# DROP TABLE IF EXISTS user_settings;
# CREATE TABLE user_settings(
#     user_id BIGINT UNSIGNED NOT NULL,
#     is_premium_account BIT,
#     is_night_mode BIT,
#     color_scheme ENUM('classic', 'day', 'tinted', 'night'),
#     LANGUAGE ENUM('russian', 'english', 'french', 'denmark', 'croatian'),
#     status_text VARCHAR(70)
#     notifications_and_sounds JSON,
#     created_at DATETIME DEFAULT NOW()

# );
# ALTER TABLE user_settings ADD CONSTRAINT fk_user_settings_user_id
# FOREIGN KEY (user_id) REFERENCES users (id)
# ON UPDATE CASCADE
# ON DELETE RESTRICT;

# ALTER TABLE users ADD COLUMN birthday DATETIME;
# ALTER TABLE users MODIFY COLUMN birthday DATE;
# ALTER TABLE users RENAME COLUMN birthday TO date_of_birth;
# ALTER TABLE users DROP COLUMN date_of_birth;


# /* DROP TABLE IF EXISTS media_types;
# CREATE TABLE media_type(
# id SERIAL,
# name VARCHAR(50)
# ); */


# 1 x M

# DROP TABLE IF EXISTS private_messages;
# CREATE TABLE private_messages(
#     id SERIAL,
#     sender_id BIGINT UNSIGNED NOT NULL,
#     receiver_id BIGINT UNSIGNED NOT NULL,
#     media_type ENUM('text', 'video', 'audio', 'image')
#     / media_type_id BIGINT UNSIGNED NOT NULL /
#     body TEXT,
#     filename VARCHAR(200),
#     created_at DATETIME DEFAULT NOW()
#     FOREIGN KEY(sender_id) REFERENCES users(id),
#     FOREIGN KEY(receiver_id) REFERENCES users(id)

# );
