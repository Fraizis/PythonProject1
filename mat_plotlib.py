# import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import pyplot


def make_2d():
    # координаты
    x = range(7)
    y1 = [6, 1, 5, 4, 3, 3, 4]

    y2 = [5, 4, 5, 3, 4, 2, 5]

    # размер
    pyplot.figure(figsize=(9, 6))

    # заголовок
    pyplot.title('Заголовок', fontsize=20)

    # название осей
    pyplot.xlabel('Ось X', fontsize=15)
    pyplot.ylabel('Ось Y', fontsize=15)

    # названия деления на осях
    pyplot.xticks(range(7),
                  labels=['Раз', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь'],
                  fontsize=12,
                  rotation=45)
    pyplot.yticks(range(1, 6))

    # границы осей
    # pyplot.xlim(0, 8)
    # pyplot.ylim(0, 8)

    # сетка
    pyplot.grid()

    # создание
    pyplot.plot(x, y1, color='purple')
    pyplot.plot(x, y2, color='lightgreen')

    # легенда
    pyplot.legend(title='Графики', labels=['Первый график', 'Второй график'])

    # отображение
    pyplot.show()


def line_graph():
    x = [1, 2, 3, 4]
    y = [10, 15, 7, 12]

    pyplot.plot(x, y, color='blue', linestyle='--', label='Пример линии')
    pyplot.title('Линейный график')
    pyplot.xlabel('Ось X')
    pyplot.ylabel('Ось Y')
    pyplot.legend()
    pyplot.savefig('pics/img_line.jpg', format='jpg')
    pyplot.show()


def scatter_diagram():
    x = range(7)
    y = [3, 1, 2, 4, 5, 3, 4]

    pyplot.scatter(x, y, color='red', s=50, alpha=0.7)
    pyplot.title('Точечная диаграмма')
    pyplot.xlabel('Ось X')
    pyplot.ylabel('Ось Y')
    pyplot.savefig('pics/img_scatter.png', format='png')
    pyplot.show()


def bar_diagram():
    categories = ['A', 'B', 'C']
    values = [15, 25, 10]

    pyplot.bar(categories, values, color=['red', 'green', 'blue'])
    pyplot.title('Столбчатая диаграмма')
    pyplot.xlabel('Категории')
    pyplot.ylabel('Значения')
    pyplot.show()


def histogram():
    data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

    pyplot.hist(data, bins=5, edgecolor='black')
    pyplot.title('Гистограмма распределения')
    pyplot.xlabel('Значения')
    pyplot.ylabel('Частота')
    pyplot.show()


def pie_diagram():
    sizes = [30, 20, 50]
    labels = ['A', 'B', 'C']

    pyplot.pie(sizes, labels=labels, startangle=90)
    pyplot.title('Круговая диаграмма')
    pyplot.savefig('pics/img_pie_1.png', format='png')
    pyplot.show()


def boxplot_diagram():
    data = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]

    pyplot.boxplot(data)
    pyplot.title('Boxplot')
    pyplot.xticks([1, 2], ['Группа 1', 'Группа 2'])
    pyplot.ylabel('Значения')
    pyplot.savefig('pics/img_boxplot.png', format='png')
    pyplot.show()


def attrition_dep():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    # print(df['Department'].unique())

    df['Attrition'] = df['Attrition'] == 'Yes'
    # deps = df.groupby('Department')['Attrition'].mean() * 100
    deps = round(df.groupby('Department')['Attrition'].mean() * 100, 2)
    print(deps.index, deps)

    # categories = ['Sales', 'Research & Development', 'Human Resources']
    # values = [deps['Sales'], deps['Research & Development'], deps['Human Resources']]
    # pyplot.figure(figsize=(10, 6))

    pyplot.bar(deps.index, deps, color=['red', 'green', 'blue'], label=deps)
    pyplot.title('Процент уволенных сотрудников в разных департаментах')
    pyplot.xlabel('Департаменты')
    pyplot.ylabel('Процент уволенных')
    pyplot.legend()

    pyplot.show()


def ages_histogram_deps():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    # print(df['Department'].value_counts().index)
    # print(df['Age'].min())

    pyplot.figure(figsize=(10, 6))
    pyplot.grid(axis='y')

    for department in df['Department'].value_counts().index:
        subset = df[df['Department'] == department]
        pyplot.hist(subset['Age'], bins=11, alpha=1, label=department, edgecolor='black')

    pyplot.title('Распределение возрастов по департаментам')
    pyplot.xlabel('Возраст')
    pyplot.ylabel('Количество сотрудников')
    pyplot.legend()

    pyplot.show()
    print()


if __name__ == '__main__':
    attrition_dep()
    print()
