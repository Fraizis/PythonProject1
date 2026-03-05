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
