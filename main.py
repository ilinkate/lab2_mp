import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from collections import defaultdict

from Sport import OBJ
from hashtable import HashTable
from Binary import BinarySearchTree
from RBT import RedBlackTree

df = pd.read_csv('/Users/ekaterina/Documents/учёба/методы программирования/lab2_mp/dataset_olympics2.csv')
df = df.drop(["ID", "Sex", "Team", "NOC", "Year", "Season", "City", "Event", "Medal", "Games"], axis=1)

df_1 = df[:1000]
df_1.to_csv("d_1.csv")

df_2 = df[1000:3100]
df_2.to_csv("d_2.csv")

df_3 = df[3100:6300]
df_3.to_csv("d_3.csv")

df_4 = df[6300:10600]
df_4.to_csv("d_4.csv")

df_5 = df[10600:16000]
df_5.to_csv("d_5.csv")

df_6 = df[16000:22500]
df_6.to_csv("d_6.csv")

df_7 = df[22500:30100]
df_7.to_csv("d_7.csv")




# @brief функции сортировок написаны для массивов, => формирую из датасетов правильный формат
df_1 = pd.read_csv('d_1.csv')
fin_1 = []
l1 = len(df_1)
for i in range(l1):
    fin_1.append(OBJ(df_1['Name'][i], df_1['Sport'][i], df_1['Age'][i], df_1['Height'][i], df_1['Weight'][i]))

df_2 = pd.read_csv('d_2.csv')
fin_2 = []
l2 = len(df_2)
for i in range(l2):
    fin_2.append(OBJ(df_2['Name'][i], df_2['Sport'][i], df_2['Age'][i], df_2['Height'][i], df_2['Weight'][i]))

df_3 = pd.read_csv('d_3.csv')
fin_3 = []
l3 = len(df_3)
for i in range(l3):
    fin_3.append(OBJ(df_3['Name'][i], df_3['Sport'][i], df_3['Age'][i], df_3['Height'][i], df_3['Weight'][i]))

df_4 = pd.read_csv('d_4.csv')
fin_4 = []
l4 = len(df_4)
for i in range(l4):
    fin_4.append(OBJ(df_4['Name'][i], df_4['Sport'][i], df_4['Age'][i], df_4['Height'][i], df_4['Weight'][i]))

df_5 = pd.read_csv('d_5.csv')
fin_5 = []
l5 = len(df_5)
for i in range(l5):
    fin_5.append(OBJ(df_5['Name'][i], df_5['Sport'][i], df_5['Age'][i], df_5['Height'][i], df_5['Weight'][i]))

df_6 = pd.read_csv('d_6.csv')
fin_6 = []
l6 = len(df_6)
for i in range(l6):
    fin_6.append(OBJ(df_6['Name'][i], df_6['Sport'][i], df_6['Age'][i], df_6['Height'][i], df_6['Weight'][i]))

df_7 = pd.read_csv('d_7.csv')
fin_7 = []
l7 = len(df_7)
for i in range(l7):
    fin_7.append(OBJ(df_7['Name'][i], df_7['Sport'][i], df_7['Age'][i], df_7['Height'][i], df_7['Weight'][i]))

final = [fin_1, fin_2, fin_3, fin_4, fin_5, fin_6, fin_7]

x = []
for i in final:
    x.append(len(i))
# print(x)

# Размеры массивов для тестирования
array_sizes = [len(fin_1), len(fin_2), len(fin_3), len(fin_4), len(fin_5), len(fin_6), len(fin_7)]

# Количество повторений для каждой размерности
num_repeats = 10

# Словарь для сохранения времени поиска для каждого метода
search_times = {'Binary Search': [], 'Hash Table Search': [], 'Multimap Search': [], 'RBT Search': []}

# Проход по всем размерностям массивов
for size in array_sizes:
    print(f"Testing for size: {size}")

    # Создание массива для тестирования
    test_array = fin_1[:size]  # Просто берем первый массив в mass

    # Используем время для измерения производительности

    # 1. Бинарное дерево поиска
    bst = BinarySearchTree()
    for obj in test_array:
        bst.insert(obj)

    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].name
        result = bst.search(key)
    search_time = np.log((time.time() - start_time) / num_repeats)
    search_times['Binary Search'].append(search_time)

    # 2. Хэш-таблица
    hashtable = HashTable(size)
    for obj in test_array:
        hashtable.insert(obj)

    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].name
        result = hashtable.search(key)
    search_time = np.log((time.time() - start_time) / num_repeats)
    search_times['Hash Table Search'].append(search_time)

    # 3. Multimap
    multimap = defaultdict(list)
    for obj in test_array:
        multimap[obj.name].append(obj)

    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].name
        result = multimap[key]
    search_time = np.log((time.time() - start_time) / num_repeats)
    search_times['Multimap Search'].append(search_time)

    # 4. RBT
    rbt = RedBlackTree(size)
    for obj in test_array:
        rbt.insert(obj)

    start_time = time.time()
    for _ in range(num_repeats):
        key = test_array[0].name
        result = rbt.search(key)
    search_time = np.log((time.time() - start_time) / num_repeats)
    search_times['RBT Search'].append(search_time)


# Построение графика
plt.plot(array_sizes, search_times['Binary Search'], label='Binary Search')
plt.plot(array_sizes, search_times['Hash Table Search'], label='Hash Table Search')
plt.plot(array_sizes, search_times['Multimap Search'], label='Multimap Search')
plt.plot(array_sizes, search_times['RBT Search'], label='RBT Search')

plt.title('Search Time and Array Size')
plt.xlabel('Array Size')
plt.ylabel('Search Time (seconds)')
plt.legend()
plt.show()

