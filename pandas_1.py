import numpy as np
import pandas as pd
import seaborn


def attrition_dep():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    df['Attrition'] = df['Attrition'] == 'Yes'

    print('Процент уволенных в каждом департаменте:')
    print(df.groupby('Department')['Attrition'].mean() * 100)


def attrition_marriage():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    print(df['MaritalStatus'].unique())

    df['Married'] = df['MaritalStatus'] == 'Married'
    df['Attrition'] = df['Attrition'] == 'Yes'

    print('Вероятности увольнения сотрудников в браке и не в браке:')
    print(df.groupby('Married')['Attrition'].mean() * 100)


def not_attrition_edu():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    # print(df['EducationField'].unique())
    df['Attrition'] = df['Attrition'] == 'No'
    edu_field = df.groupby('EducationField')['Attrition'].mean() * 100

    print(f'Процент не уволенных среди сотрудников, '
          f'у которых указана сфера образования Other: {edu_field['Other']:0.2f}%\n')
    print('Влияет ли сфера образования на увольнение:')
    print(edu_field)


def education_age():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    # print(df['Age'].unique())

    df['Attrition'] = df['Attrition'] == 'Yes'
    edu_age = df.groupby('Education')['Age'].mean()
    print(edu_age)

    df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 21, 40, 65], labels=['Teenager', 'Adult', 'Senior Adult'])

    print('\nВероятности увольнения для сотрудников разных возрастных групп')
    print(df.groupby('AgeGroup')['Attrition'].mean() * 100)


def data_frame_seaborn():
    # print(seaborn.get_dataset_names())
    exc = seaborn.load_dataset('exercise')
    print(exc.columns)
    # print(exc['diet'].unique())
    # 1
    runn = exc[exc['kind'] == 'running']
    res = runn['pulse'].agg(['mean'])
    print(res)
    # 2
    walk = exc[(exc['kind'] == 'walking') & (exc['time'] == '30 min')]
    res = walk['pulse'].agg(['mean'])
    print(round(res['mean']))
    # 3
    df = exc.groupby(['diet', 'time'])['pulse'].mean()
    print(round(df, 1))

    # 4
    print(exc[exc['pulse'] == exc['pulse'].max()])

    # 5
    answer = exc[(exc['kind'] == 'rest') & (exc['pulse'] < 100)]['id']
    print(len(answer.unique()))
    # 6
    pulse = exc['pulse'].mean()
    answer = exc[
        (exc['diet'] == 'no fat') &
        (exc['kind'] == 'rest') &
        (exc['pulse'] > exc['pulse'].mean())
        ]['id']
    print(len(answer.unique()))


def create_series_df():
    # Создание Series из списка
    s1 = pd.Series([1, 2, 3, 4, 5])
    print(s1)

    # Создание Series с определенным индексом
    s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print(s2)

    print(s1[0])  # Выводит первый элемент
    print(s2['b'])  # Выводит элемент с индексом 'b'

    s3 = s1 + 10
    print(s3)  # К каждому элементу добавляется 10

    # Создание DataFrame из словаря
    data = {
        'Имя': ['Никита', 'Лиза', 'Степа', 'Егор'],
        'Возраст': [25, 27, 22, 33],
        'Город': ['Мадрид', 'Мадрид', 'Москва', 'Петербург']
    }
    df = pd.DataFrame(data)
    print(df)

    # Создание DataFrame из списка списков
    data_list = [['Никита', 25, 'Москва'], ['Лиза', 27, 'Москва'], ['Степа', 22, 'Казань'], ['Егор', 33, 'Петербург']]
    df2 = pd.DataFrame(data_list, columns=['Имя', 'Возраст', 'Город'])
    print(df2)

    print(df['Имя'])  # Получает столбец 'Имя'
    print(df.iloc[0])  # Получает первую строку

    young_people = df[df['Возраст'] < 30]  # Фильтрует людей младше 30
    print(young_people)

    df['Занятие'] = ['Инженер', 'Менеджер', 'Студент', 'Экономист']
    print(df)

    df = df.drop('Занятие', axis=1)  # Удаляет столбец 'Занятие'
    print(df)

    average_age = df['Возраст'].mean()
    print(f"Средний возраст: {average_age}")
    print(df)


def read_from_file():
    data = pd.read_csv('train.csv')
    # df_excel = pd.read_excel('data.xlsx')
    # data.to_csv('train_new.csv', index=False)
    # data.to_excel('train_new.xlsx', index=False)
    data = {
        'Имя': ['Аня', 'Борис', 'Света', 'Иван', 'Оля'],
        'Возраст': [23, 34, 29, 24, 27],
        'Город': ['Москва', 'Питер', 'Новосибирск', 'Екатеринбург', 'Уфа']
    }

    df = pd.DataFrame(data)
    print(df)

    # Установка имени в качестве индекса
    df.set_index('Имя', inplace=True)

    # Индексирование по меткам
    print(df.loc['Аня'])  # Получение данных для Ани

    # Индексирование по позиции
    print(df.iloc[0])  # Получение первой строки
    # Создаем новый DataFrame

    # Логическая индексация: выбираем строки, где возраст больше 25
    filtered_df = df[df['Возраст'] > 25]
    print(filtered_df)

    # Теперь можно получить возраст Бориса
    age_boris = df.loc['Борис', 'Возраст']  # Индексирование по меткам
    print(f'Возраст Бориса: {age_boris}')

    # Получение значения по позиции
    city_second = df.iloc[1, 1]  # Индексирование по позициям, 1 - вторая строка, 1 - второй столбец
    print(f'Город на второй позиции: {city_second}')
    # Создаем новый DataFrame

    # Выбор людей старше 25 лет, которые не живут в Москве
    filtered_df = df[(df['Возраст'] > 25) & (df['Город'] != 'Москва')]
    print(filtered_df)

    # Создаем новый DataFrame с многоуровневым индексом
    arrays = [
        ['Россия', 'Россия', 'США', 'США'],
        ['Москва', 'Питер', 'Нью-Йорк', 'Лос-Анджелес']
    ]
    index = pd.MultiIndex.from_arrays(arrays, names=('Страна', 'Город'))

    data = {
        'Население': [12.5, 5.4, 8.4, 4.0],
        'Площадь (км²)': [2511, 1439, 789, 503]
    }

    df_multi = pd.DataFrame(data, index=index)
    print(df_multi)

    # Выбор данных для конкретной страны
    print(df_multi.loc['Россия'])


def null_change():
    data = {
        'Имя': ['Аня', 'Борис', 'Света', None],
        'Возраст': [23, None, 29, 24],
        'Город': ['Москва', 'Питер', None, 'Екатеринбург']
    }

    df = pd.DataFrame(data)

    # Проверка отсутствующих данных
    print(df.isnull())

    # Заполнение отсутствующих данных в столбце 'Город'
    df['Город'] = df['Город'].fillna('Неизвестно')

    # Заполнение отсутствующих данных в столбце 'Возраст' нулём
    df['Возраст'] = df['Возраст'].fillna(0)

    print(df)

    # Заполнение отсутствующих данных средним значением в столбце 'Возраст'
    df['Возраст'] = df['Возраст'].fillna(df['Возраст'].mean())

    print(df)

    # Заполнение отсутствующих данных предыдущими значениями
    df['Возраст'] = df['Возраст'].ffill()
    print(df)

    # Удаление строк с отсутствующими значениями
    df_cleaned = df.dropna()
    print(df_cleaned)

    # Удаление столбцов с отсутствующими значениями
    df_cleaned_columns = df.dropna(axis=1)
    print(df_cleaned_columns)


def convert_type():
    # Создаем DataFrame
    data = {
        'Имя': ['Аня', 'Борис', 'Света'],
        'Возраст': ['23', '34', '29'],  # Возраст представлен строками
        'Рост': ['1.65', '1.80', '1.75']  # Рост тоже строками
    }

    df = pd.DataFrame(data)

    # Проверка типов данных
    print(df.dtypes)

    # Изменение типа данных
    df['Возраст'] = df['Возраст'].astype(int)  # Преобразование в целое число
    df['Рост'] = df['Рост'].astype(float)  # Преобразование в число с плавающей точкой

    # Проверка типов данных после преобразования
    print(df.dtypes)

    # Применим функцию, чтобы получить квадрат возраста
    df['Возраст_квадрат'] = df['Возраст'].apply(lambda x: x ** 2)
    print(df)

    # Суммируем значения в строках
    df['Сумма'] = df.apply(lambda row: row['Возраст'] + row['Рост'],
                           axis=1)  # axis=1 означает, что функция применяется к строкам
    print(df)

    # Применяем функцию для преобразования имен в верхний регистр
    df['Имя'] = df['Имя'].map(lambda x: x.upper())
    print(df)

    # Применяем функцию, чтобы округлить рост до одного знака после запятой
    df['Рост'] = df['Рост'].map(lambda x: round(x, 1))
    print(df)

    # Среднее значение
    mean_age = df['Возраст'].mean()
    print('Средний возраст:', mean_age)

    # Медиана зарплаты
    median_salary = df['Зарплата'].median()
    print('Медианная зарплата:', median_salary)

    # Стандартное отклонение по возрасту
    std_age = df['Возраст'].std()
    print('Стандартное отклонение по возрасту:', std_age)

    # Мода для города
    mode_city = df['Город'].mode()
    print('Наиболее распространённый город:', mode_city.iloc[0])


def export_to_file():
    # Создаем пример DataFrame
    data = {
        'Имя': ['Никита', 'Лиза', 'Степа', 'Егор'],
        'Возраст': [23, 22, 19, 26],
        'Город': ['Мадрид', 'Мадрид', 'Москва', 'Питер']
    }

    df = pd.DataFrame(data)

    # Экспортируем DataFrame в CSV файл
    df.to_csv('output.csv', index=False, encoding='utf-8')

    # Экспортируем DataFrame в Excel файл
    df.to_excel('output.xlsx', index=False, engine='openpyxl')

    # Экспортируем DataFrame в JSON файл
    df.to_json('output.json', orient='records', lines=True, force_ascii=False)


def students_80_more_points():
    data = {
        'Имя': ['Аня', 'Борис', 'Света', 'Иван'],
        'Возраст': [23, 34, 29, 24],
        'Город': ['Москва', 'Питер', 'Новосибирск', 'Екатеринбург'],
        'Оценка по математике': [75, 85, 90, 60],
        'Оценка по науке': [81, 78, 88, 70]
    }

    df = pd.DataFrame(data)
    df.set_index('Имя', inplace=True)
    answer = df[df['Оценка по науке'] > 80]
    print(answer)


def add_new_column_delete_old():
    data = {
        'Имя': ['Аня', 'Борис', 'Света', 'Иван'],
        'Возраст': [23, 34, 29, 24],
        'Город': ['Москва', 'Питер', 'Новосибирск', 'Екатеринбург'],
        'Оценка по математике': [75, 85, 90, 60],
        'Оценка по науке': [80, 78, 88, 70]
    }

    df = pd.DataFrame(data)
    df.set_index('Имя', inplace=True)

    df['Средняя оценка'] = df.apply(lambda row: (row['Оценка по математике'] + row['Оценка по науке']) / 2, axis=1)
    df = df.drop(['Оценка по математике', 'Оценка по науке'], axis=1)
    print(df)


def change_data():
    data = {
        'Название продукта': ['Яблоки', 'Бананы', 'Груши', 'Апельсины'],
        'Цена': [100, 50, np.nan, 80],
        'Количество на складе': [30, np.nan, 20, 25],
        'Рейтинг': [4.5, np.nan, 3.8, 4.2]
    }

    df = pd.DataFrame(data)

    df['Количество на складе'] = df['Количество на складе'].fillna(0)
    df['Рейтинг'] = df['Рейтинг'].fillna(df['Рейтинг'].mean())

    df['Количество на складе'] = df['Количество на складе'].astype(int)

    df['Общая стоимость'] = df.apply(lambda row: (row['Количество на складе'] * row['Цена']), axis=1)

    # Проверка типов данных после преобразования
    print(df.dtypes)
    print(df)


def aggregate_data():
    data = {
        'Город': ['Москва', 'Питер', 'Москва', 'Питер', 'Екатеринбург'],
        'Продажи': [100, 150, 200, 130, 170]
    }

    df = pd.DataFrame(data)

    grouped = df.groupby('Город').sum()
    print(grouped)

    result = df.groupby('Город').aggregate({'Продажи': ['sum', 'mean', 'count']})
    print(result)

    pivot = pd.pivot_table(df, values='Продажи', index='Город', aggfunc='sum')
    print(pivot)

    data = {
        'Город': ['Москва', 'Питер', 'Москва', 'Питер'],
        'Товар': ['А', 'А', 'Б', 'Б'],
        'Продажи': [100, 150, 200, 130]
    }

    df = pd.DataFrame(data)
    pivot = df.pivot(index='Город', columns='Товар', values='Продажи')
    print(pivot)

    data = {
        'Возраст': [25, 30, 35, 40, None],
        'Зарплата': [50000, 60000, 70000, 80000, 90000],
        'Город': ['Москва', 'Питер', 'Москва', 'Питер', 'Екатеринбург']
    }

    df = pd.DataFrame(data)

    # Описание числовых данных
    print(df.describe())


def total_sale_sum_category():
    data = {
        'Дата': [
            '2024-01-01', '2024-01-02', '2024-01-03',
            '2024-01-04', '2024-01-05', '2024-01-06',
            '2024-01-07', '2024-01-08'
        ],
        'Категория': [
            'Электроника', 'Одежда', 'Электроника',
            'Одежда', 'Спорт', 'Электроника',
            'Спорт', 'Одежда'
        ],
        'Продажи': [
            20000, 15000, 22000,
            18000, 30000, 25000,
            27000, 20000
        ],
        'Регион': [
            'Москва', 'Питер', 'Москва',
            'Екатеринбург', 'Питер', 'Москва',
            'Екатеринбург', 'Питер'
        ]
    }

    df = pd.DataFrame(data)

    result = df.groupby('Категория', as_index=False).aggregate({'Продажи': 'sum'})
    # print(result)

    res = df.groupby(['Регион', 'Категория'], as_index=False)['Продажи'].mean()
    # print(res)

    group = df.groupby(["Регион", "Категория"], as_index=False).aggregate({'Продажи': 'mean'})
    # print(group)

    pivot = pd.pivot_table(df, values='Продажи', index=['Регион', 'Категория'], aggfunc='mean').reset_index()
    print(pivot)


def avg_sale_region():
    ...


if __name__ == '__main__':
    print()
    total_sale_sum_category()
