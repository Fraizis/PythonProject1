# TCL


# Работа с транзакциями
#    - Начало транзакции:
#      BEGIN;
#
#    - Завершение транзакции (commit):
#      COMMIT;
#
#    - Отмена транзакции (rollback):
#      ROLLBACK;


# BEGIN TRANSACTION WORK;
# INSERT INTO MyTable VALUES ('50', 'some string');
# COMMIT WORK;


# START TRANSACTION;
#
# -- Переводим 200 долларов с счета Alice на счет Bob
# UPDATE accounts SET balance = balance - 200 WHERE account_name = 'Alice';
# UPDATE accounts SET balance = balance + 200 WHERE account_name = 'Bob';
#
# COMMIT;
# Если между этими двумя операциями произойдет сбой системы или ошибка,
# транзакция будет отменена, и база данных вернется в исходное состояние.
# Это обеспечивает целостность данных.


# Проверить, какой будет результат определенных действий после нашего SQL-скрипта,
# но не хотим применять его.
#
# -- Начинаем транзакцию
# BEGIN;
#
# -- Переводим 200 долларов с счета Alice на счет Bob
# UPDATE accounts SET balance = balance - 200 WHERE account_name = 'Alice';
# UPDATE accounts SET balance = balance + 200 WHERE account_name = 'Bob';
#
# -- Смотрим, какой будет результат до завершения транзакции
# SELECT * FROM accounts;
#
# -- Откатываем транзакцию
# ROLLBACK;


# Транзакции

# начать транзакцию

# START TRANSACTION;
# 	INSERT INTO `users` (firstname, lastname, email, birthday)
# 	VALUES ('Rahsan2','Runt2','crist.donny2@example.net','2018-01-07');

# 	SET @user_id = LAST_INSERT_ID();
#
# 	INSERT INTO `user_settings` (user_id, is_premium_account, app_language, created_at)
# 	VALUES (@user_id, FALSE, 'english', NOW());

# коммит (фиксация) изменений
# COMMIT;

# ролбэк (откат) изменений
# ROLLBACK;

# проверка состояния таблиц после транзакции
# SELECT * FROM users ORDER BY id DESC;
# SELECT * FROM user_settings ORDER BY user_id DESC;


# удаляем процедуру с проверкой
# DROP PROCEDURE IF EXISTS telegram.add_user;

# устанавливаем разделитель команд
# DELIMITER $$

# создаем процедуру
# CREATE PROCEDURE telegram.add_user(
#     _firstname VARCHAR(100),
#     _lastname VARCHAR(100),
#     _email VARCHAR(100),
#     _birthday DATE,
#     _is_premium_account BIT,
#     _app_language ENUM('english','french','russian','german','belorussian','croatian','dutch'),
#
#     OUT trans_result VARCHAR(200)
# )
# BEGIN
# объявляем необходимые переменные
#     DECLARE has_error BIT DEFAULT 0;
#     DECLARE code VARCHAR(100);
#     DECLARE error_string VARCHAR(100);

# объявляем обработчик исключений
#     DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
#     BEGIN
#         SET has_error = 1;
#
#         GET stacked DIAGNOSTICS CONDITION 1
#             code = RETURNED_SQLSTATE, error_string = MESSAGE_TEXT;
#
#         SET trans_result = CONCAT('Error occured! Code: ', code, '. Text: ', error_string);
#     END;

# начинаем транзакцию
#     START TRANSACTION;
#         INSERT INTO `users` (firstname, lastname, email, birthday)
#         VALUES (_firstname, _lastname, _email, _birthday);
#
#         INSERT INTO `user_settings` (user_id, is_premium_account, app_language, created_at)
#         VALUES (LAST_INSERT_ID(), _is_premium_account, _app_language, NOW());

# проверяем ошибки
#     IF has_error THEN
        # SET trans_result = 'Error!';
        # ROLLBACK;
#     ELSE
#         SET trans_result = 'Ok.';
#         COMMIT;
#     END IF;
# END$$

# возвращаем разделитель в значение по умолчанию
# DELIMITER ;

# вызываем процедуру с параметрами

# CALL add_user('Leslie3', 'Reichel3',  'cronin.emmitt3@example.net', '1982-05-01', FALSE, 'english', @trans_result);

# читаем результат выполнения процедуры
# SELECT @trans_result;

# проверяем данные в таблицах
# SELECT * FROM users ORDER BY id DESC;
# SELECT * FROM user_settings ORDER BY user_id DESC;
