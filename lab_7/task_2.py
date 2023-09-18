import numpy as np
import csv
import matplotlib.pyplot as plt

time = np.array([])
t4 = np.array([])
t5 = np.array([])
with open('data1.csv', encoding="ISO-8859-1") as table:
    f_reader = csv.reader(table, delimiter=';')
    next(f_reader)
    for rows in f_reader:
        time = np.append(time, float(rows[0]))
        t4 = np.append(t4, int(rows[3]))
        t5 = np.append(t5, int(rows[4]))

    figure = plt.figure()  # окно
    figure.suptitle('Графики зависимостей положения дроссельной заслонки \n '
                    'и количества оборотов двигателей от времени \n '
                    'и график корреляции параметров:')

    graph1 = plt.subplot(1, 2, 1)  # 1 строка, 2 столбца, 1 график
    graph1.plot(time, t4, time, t5)  # строим два графика
    graph1.grid()
    graph1.set_xlabel('Время')
    graph1.set_ylabel('Значение положения дроссельной заслонки (синий) / \n оборотов двигателя (оранжевый)')

    graph2 = plt.subplot(1, 2, 2)  # 1 строка, 2 столбца, 2 график
    graph2.scatter(t4, t5, color='red')
    graph2.grid()
    graph2.set_xlabel('Положение дроссельной заслонки')
    graph2.set_ylabel('Количество оборотов двигателя')




plt.show()