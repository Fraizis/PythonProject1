# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",  # Localhost for local connection
    user="root",
    passwd="09021991qqQ",
    database="gfg"
)

# preparing a cursor object

cursorObject = dataBase.cursor()



# creating database
# cursorObject.execute("CREATE DATABASE gfg")

# create user

# query = "CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonpwd123'"
# cursorObject.execute(query)

# creating table
# cursorObject.execute("USE gfg")

studentRecord = """
CREATE TABLE STUDENT (
    NAME  VARCHAR(20) NOT NULL,
    BRANCH VARCHAR(50),
    ROLL INT NOT NULL,
    SECTION VARCHAR(5),
    AGE INT
)"""

# table created
# cursorObject.execute(studentRecord)


# sql =
# """
# INSERT INTO STUDENT (
#     NAME,
#     BRANCH,
#     ROLL,
#     SECTION,
#     AGE
#     )
# VALUES (%s, %s, %s, %s, %s)
# """
# val = ("Ram", "CSE", "85", "B", "19")

# cursorObject.execute(sql, val)

# dataBase.commit()


sql = """
INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)
VALUES (%s, %s, %s, %s, %s)
"""
val = [("Nikhil", "CSE", "98", "A", "18"),
       ("Nisha", "CSE", "99", "A", "18"),
       ("Rohan", "MAE", "43", "B", "20"),
       ("Amit", "ECE", "24", "A", "21"),
       ("Anil", "MAE", "45", "B", "20"),
       ("Megha", "ECE", "55", "A", "22"),
       ("Sita", "CSE", "95", "A", "19")]

# cursorObject.executemany(sql, val)
# dataBase.commit()

# print(dataBase.get_rows())


query = "SELECT NAME, ROLL FROM STUDENT"
cursorObject.execute(query)


myresult = cursorObject.fetchall()
print(myresult)

for x in myresult:
    print(x)

# Disconnecting from the server
dataBase.close()



#
# Задачи
#
#     Описать таблицу фильм: id, название, длительность, режиссер, жанр фильма.
#     Обратите внимание на то, что у фильма может быть более одного жанра, а к одному
#     жанру может относится более, чем один фильм.

#     Описать таблицу песня: id, название, длительность, певец. При этом у песни может быть
#     более одного певца, а певец мог записать более одной песни.

#     Реализовать таблицу машина: модель, производитель, цвет, цена
#         Описать отдельную таблицу производитель: id, название, рейтинг.
#         Описать отдельную таблицу цвета: id, название.
#
#     У одной машины может быть только один производитель, а у производителя — много машин.
#     У одной машины может быть много цветов, а у одного цвета может быть много машин.
#     Добавить в БД из пункта 6.2. таблицу военно-обязанных по типу того,
#     как мы описали отдельную таблицу DisabledEmployee.
#
