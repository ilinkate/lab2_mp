# для поиска хэш-таблицей
import matplotlib.pyplot as plt

from Sport import OBJ


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, obj):
        key = obj.name
        index = self.hash_function(key)
        if not self.table[index]:
            self.table[index] = [obj]
        else:
            self.table[index].append(obj)

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            for obj in self.table[index]:
                if obj.name == key:
                    return obj
        return None

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def linear_probing(self, index):
        return (index + 1) % self.size

    def insert(self, obj):
        key = obj.name
        index = self.hash_function(key)

        while self.table[index] is not None:
            self.collisions += 1
            index = self.linear_probing(index)

        self.table[index] = obj

    def search(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index].name == key:
                return self.table[index]
            index = self.linear_probing(index)

        return None

# Функция для тестирования


def test_hash_table(size):
    hash_table = HashTable(size)
    for i in range(size):
        obj = OBJ(sport=f"Sport{i}", age=i, weight=i, name=f"Name{i}", height=i)
        hash_table.insert(obj)

    return hash_table.collisions


sizes = list(range(100, 2001, 200))
collisions = [test_hash_table(size) for size in sizes]

plt.plot(sizes, collisions, marker='*')
plt.title('Collisions and Array Size')
plt.xlabel('Array Size')
plt.ylabel('Number of Collisions')
plt.show()


