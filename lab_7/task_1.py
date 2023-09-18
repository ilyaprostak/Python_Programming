import numpy as np
from time import perf_counter
from random import randint

#start = perf_counter()  # определяем начальный момент времени

array_1_with_numpy = np.random.randint(1, 1000000000, 1000001)  # создаем два массива произвольных целых чисел numpy
array_2_with_numpy = np.random.randint(1, 1000000000, 1000001)

array_1_without_numpy = [randint(1, 1000000000) for i in range(1000001)]  # создаем два массива произвольных целых чисел
array_2_without_numpy = [randint(1, 1000000000) for i in range(1000001)]
result_array_without_numpy = []  # результирующий массив
#length = len(array_1)  # записываем длину массивов в переменную

start_1 = perf_counter()  # определяем момент времени перед началом перемножения с помощью numpy
result_array_with_numpy = np.multiply(array_1_with_numpy, array_2_with_numpy)  # выполняем поэлементное перемножение элементов заданных массивов

sort_whith_numpy_time = perf_counter() - start_1


start_2 = perf_counter()  # определяем момент времени перед началом перемножения без помощи numpy


# поэлементное перемножение двух массивов без использования библиотеки NumPy
for i in range(1000001):
    result_array_without_numpy.append(array_1_without_numpy[i] * array_2_without_numpy[i])  # выполняем поэлементное перемножение элементов с записью в массив

sort_whithout_numpy_time = perf_counter() - start_2



print(f"\nВремя перемножения массивов без использования библиотеки numpy: {sort_whithout_numpy_time}\n\n"
      f"Время перемножения массивов с использованием библиотеки numpy: {sort_whith_numpy_time}")  # выводим время работы программы