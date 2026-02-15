import pandas as pd

# s = pandas.Series([10, 20, 30, 40])
# print(s)
#
# s = pandas.Series(data=[100, 200, 300], index=['A', 'B', 'C'], name='Letters with numbers', dtype=float)
# print(s)
#
# s = pandas.Series(data=[1, 2, 3], index=['x', 'y', 'z'])
# print(s)

# s = pandas.Series({'A': 100, 'B': 200, 'C': 300}, dtype=int)
# print(s)

# df = pd.DataFrame( {"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]}, index=['abc', 'def', 'ghi'] )
# print(df)

# df = pd.DataFrame([[4, 7, 10], [5, 8, 11], [6, 9, 12]], index=[1, 2, 3], columns=['a', 'b', 'c'])
# print(df)
# print(df.index, df.columns)

# df = pd.DataFrame(
#     data={"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]},
#     index=pd.MultiIndex.from_tuples([('d', 1), ('d', 2), ('e', 2)], names=['n', 'v'])
# )
# print(df)

data = pd.read_csv('train.csv')
#
# # df_excel = pd.read_excel('data.xlsx')
# # print(data.loc[1])
# print(data['Age'])

# data.to_csv('train_new.csv', index=False)
# data.to_excel('train_new.xlsx', index=False)
#
# df = pd.DataFrame( { "a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12] }, index=["abc", "def", "ghi"] )
# print(df)
#
# df.columns = ['A', 'B', 'C']
# df.index = [1, 2, 3]
# print(df)
# data['FamilySize'] = data['SibSp'] + data['Parch']
#
# data['Alone'] = data['FamilySize'].apply(lambda x: 1 if x == 0 else 0)

# data[['FamilySize', 'Alone']].head()
# print(data[['FamilySize','SibSp', 'Parch']])
# data = data.drop(columns=['Cabin', 'Embarked'])
# data.drop(columns=['Cabin'], inplace=True)
# print(data.isnull().sum())
# print(data['Age'].info())
# data['Age'] = data['Age'].fillna(data['Age'].mean())
# print(data['Age'])
# data['Age'] = data['Age'].fillna(data['Age'].median())
#
# data['Age'] = data['Age'].fillna(data.groupby('Sex')['Age'].transform('median'))
# # print(data['Age'][:100])
# data['Embarked'].mode()
# print(data['Embarked'][:100])
print(data.groupby('Pclass')['Fare'].mean())
print(data.groupby(['Sex', 'Pclass'])['Age'].mean())

# print(data[
#           (data['Sex'] == 'female') &
#           (data['Age'] > 18) &
#           (data['Age'] < 25) &
#           (data['SibSp'] == 0) &
#           (data['Parch'] == 0) &
#           (data['Survived'] == 0)
#       ].shape
#       )
# print(data[(data['SibSp'] + data['Parch'] >= 2) & (data['Pclass'] == 3)].shape)
# print(data[data['Age'] > data['Age'].mean()]['Name'].head())
print(data.groupby('Pclass')['Fare'].agg(['min', 'max', 'mean', 'median']))
