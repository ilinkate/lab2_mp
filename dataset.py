import numpy as np
import pandas as pd
#Сгенерируем 7 наборов данных следующих размерностей: 100, 500, 1000, 5000, 10000, 50000, 100000
arr_names = []
with open("names.txt", "r") as f:
    for i in f:
        arr_names.append(i[:-1])

arr_books = []
with open("books.txt", "r") as f:
    for i in f:
        arr_books.append(i[:-1])

arr_sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]

for i in arr_sizes:
    name = np.random.choice(arr_names, size=i)
    sport = np.random.choice(arr_books, size=i)
    year = np.random.randint(low=1500, high=2024, size=i)
    pages = np.random.randint(low=100, high=5000, size=i)

    d = {
            "Name": name,
            "Sport": sport,
            "Year Published": year,
            "Pages": pages,
        }
    df = pd.DataFrame(data=d)
    df.to_csv(f"Data_{i}.csv")
    print('Saved ', i, "to csv!")

