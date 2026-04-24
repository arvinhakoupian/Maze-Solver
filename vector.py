class Vector:
    def __init__(self, capacity=4):
        if capacity < 1:
            capacity = 1
        self._size = 0
        self._capacity = capacity
        self._data = [None] * self._capacity

    def _grow(self):
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        i = 0
        while i < self._size:
            new_data[i] = self._data[i]
            i += 1
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._grow()
        self._data[self._size] = value
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return self._data[index]

    def size(self):
        return self._size
