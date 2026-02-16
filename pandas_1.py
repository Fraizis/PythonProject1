import pandas as pd
import seaborn


def create_df():
    s = pd.Series([10, 20, 30, 40])
    print(s)

    s = pd.Series(data=[100, 200, 300], index=['A', 'B', 'C'], name='Letters with numbers', dtype=float)
    print(s)

    s = pd.Series(data=[1, 2, 3], index=['x', 'y', 'z'])
    print(s)

    s = pd.Series({'A': 100, 'B': 200, 'C': 300}, dtype=int)
    print(s)

    df = pd.DataFrame(data={"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]}, index=['abc', 'def', 'ghi'])
    print(df)

    df = pd.DataFrame(data=[[4, 7, 10], [5, 8, 11], [6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c'])
    print(df)
    print(df.index, df.columns)

    df = pd.DataFrame(
        data={"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]},
        index=pd.MultiIndex.from_tuples([('d', 1), ('d', 2), ('e', 2)], names=['n', 'v'])
    )
    print(df)


def read_file():
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
