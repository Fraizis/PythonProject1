import pandas as pd
import seaborn


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

    print(data.loc[1])
    print(data['Age'])
    print(data['Age'].info())
    print(data['Pclass'].unique())

    data['Alone'] = data['FamilySize'].apply(lambda x: 1 if x == 0 else 0)

    print(data[['FamilySize', 'Alone']].head())
    print(data[['FamilySize', 'SibSp', 'Parch']])
    data = data.drop(columns=['Cabin', 'Embarked'])
    data.drop(columns=['Cabin'], inplace=True)

    print(data.isnull().sum())
    print(data['Age'].info())

    data['Age'] = data['Age'].fillna(data['Age'].mean())
    print(data['Age'])
    data['Age'] = data['Age'].fillna(data['Age'].median())

    data['Age'] = data['Age'].fillna(data.groupby('Sex')['Age'].transform('median'))
    print(data['Age'][:100])
    data['Embarked'].mode()
    print(data.groupby('Pclass')['Fare'].mean())
    print(data.groupby(['Sex', 'Pclass'])['Age'].mean())

    print(data[
              (data['Sex'] == 'female') &
              (data['Age'] > 18) &
              (data['Age'] < 25) &
              (data['SibSp'] == 0) &
              (data['Parch'] == 0) &
              (data['Survived'] == 0)
              ].shape
          )

    print(data[(data['SibSp'] + data['Parch'] >= 2) & (data['Pclass'] == 3)].shape)
    print(data[data['Age'] > data['Age'].mean()]['Name'].head())

    print(data.groupby(['Pclass', 'Sex'])['Age'].mean())
    print(round(28.722973, 2))

    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 20]})
    df_sorted = df.sort_values(by='Age')
    print(df.sort_values(by='Age', ascending=False))

    print(df.sort_values(by=['Name', 'Age'], ascending=[True, False]))
    df = pd.DataFrame({'Value': [3, None, 2, None, 1]})
    print(df.sort_values(by='Value', na_position='first'))


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


if __name__ == '__main__':
    print()
    export_to_file()
