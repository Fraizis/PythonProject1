import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def example_lineplot():
    # Создание искусственного датасета
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(scale=0.1, size=x.shape)

    data = pd.DataFrame({'x': x, 'y': y})

    # Построение линейного графика
    sns.lineplot(data=data, x='x', y='y')
    plt.title('Линейный график: Синусоида с шумом')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def example_histplot():
    tips = sns.load_dataset("tips")

    # Построение гистограммы распределения счетов
    sns.histplot(tips['total_bill'], bins=20, kde=True)
    plt.title('Гистограмма: Распределение счетов')
    plt.xlabel('Счет (доллары)')
    plt.ylabel('Количество')
    plt.show()


def example_scatterplot():
    tips = sns.load_dataset("tips")

    # Построение диаграммы рассеяния
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='time')
    plt.title('Диаграмма рассеяния: Счет и чаевые')
    plt.xlabel('Счет (доллары)')
    plt.ylabel('Чаевые (доллары)')
    plt.show()


def hist_show():
    # Генерируем случайные данные
    data = np.random.randn(1000)

    # Строим гистограмму
    sns.histplot(data, bins=30, color='blue', kde=False)
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.title('Гистограмма распределения данных')
    plt.show()


def kde_plot_show():
    data = np.random.randn(1000)
    sns.kdeplot(data, color='green', fill=True)
    plt.xlabel('Значение')
    plt.ylabel('Плотность вероятности')
    plt.title('Оценка плотности вероятности данных')
    plt.show()


def kde_hist():
    data1 = np.random.randn(1000)
    data2 = np.random.randn(1000) + 1.5  # Смещение второго набора данных

    sns.histplot(data1, color='blue', label='Набор данных 1', kde=True)
    sns.histplot(data2, color='red', label='Набор данных 2', kde=True)
    plt.legend()
    plt.show()


def box_plot_show():
    # Генерируем случайные данные
    tips = sns.load_dataset("tips")

    # Строим коробочную диаграмму по данным о чаевых с группировкой по дням
    sns.boxplot(x='day', y='total_bill', data=tips)
    plt.xlabel('День недели')
    plt.ylabel('Общая сумма счета')
    plt.title('Коробочная диаграмма общей суммы счета по дням недели')
    plt.show()


def strip_plot_show():
    tips = sns.load_dataset("tips")

    # Строим точечную диаграмму
    sns.stripplot(x='day', y='total_bill', data=tips, color='orange', jitter=True)
    plt.xlabel('День недели')
    plt.ylabel('Общая сумма счета')
    plt.title('Точечная диаграмма общей суммы счета по дням недели')
    plt.show()


def boxplot_and_stripplot():
    tips = sns.load_dataset("tips")

    # Комбинированная коробочная и точечная диаграмма
    sns.boxplot(x='day', y='total_bill', data=tips, color='lightgrey')
    sns.stripplot(x='day', y='total_bill', data=tips, color='black', jitter=True, alpha=0.5)
    plt.xlabel('День недели')
    plt.ylabel('Общая сумма счета')
    plt.title('Коробочная и точечная диаграмма общей суммы счета по дням недели')
    plt.show()


def barplot_show():
    # Загружаем набор данных о чаевых
    tips = sns.load_dataset("tips")

    # Создаем столбчатую диаграмму средней суммы счета по дням недели
    sns.barplot(x='day', y='total_bill', data=tips, estimator=sum, ci='sd', palette='muted')
    plt.xlabel('День недели')
    plt.ylabel('Сумма счета')
    plt.title('Сравнение суммы счета по дням недели')
    plt.show()


def barplot_with_values():
    tips = sns.load_dataset("tips")

    ax = sns.barplot(x='day', y='total_bill', data=tips, estimator=np.mean, palette='Set2')
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='bottom')
    plt.xlabel('День недели')
    plt.ylabel('Средняя сумма счета')
    plt.title('Средняя сумма счета по дням недели с аннотациями')
    plt.show()

    sns.barplot(x='day', y='total_bill', hue='time', data=tips, palette='pastel')
    plt.xlabel('День недели')
    plt.ylabel('Средняя сумма счета')
    plt.title('Средняя сумма счета по дням недели и времени')
    plt.show()


def faceit_grid_show():
    # Загружаем набор данных о чаевых
    tips = sns.load_dataset("tips")

    # Создаем FacetGrid, чтобы визуализировать распределение суммы счета по полам и дням недели
    g = sns.FacetGrid(tips, col='sex', row='time', margin_titles=True)
    g.map(sns.histplot, 'total_bill', kde=True)
    g.set_axis_labels('Сумма счета', 'Частота')
    g.set_titles(col_template="{col_name}", row_template="{row_name}")
    plt.show()


def faceit_grid_other():
    tips = sns.load_dataset("tips")

    g = sns.FacetGrid(tips, col='sex', row='time', margin_titles=True)
    g.map(sns.scatterplot, 'total_bill', 'tip', alpha=0.5)
    g.map(sns.regplot, 'total_bill', 'tip', scatter=False, color='blue')
    g.set_axis_labels('Сумма счета', 'Чаевые')
    g.set_titles(col_template="{col_name}", row_template="{row_name}")
    plt.show()


def heatmap_show():
    # Генерируем случайные данные
    data = np.random.rand(10, 12)

    # Создаем тепловую карту
    sns.heatmap(data, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Тепловая карта случайных данных')
    plt.show()


def heatmap_with_popular_data():
    # Загружаем набор данных о чаевых
    tips = sns.load_dataset("tips")

    # Применяем one-hot encoding для категориальных переменных
    tips_encoded = pd.get_dummies(tips, drop_first=True)

    # Вычисляем корреляционную матрицу
    corr = tips_encoded.corr()

    # Создаем тепловую карту корреляционной матрицы
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Корреляционная матрица')
    plt.show()


if __name__ == '__main__':
    barplot_with_values()
