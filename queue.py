class Queue:
    def __init__(self, capacity=8):
        if capacity < 1:
            capacity = 1
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._head = 0
        self._tail = 0

    def _grow(self):
        new_capacity = self._capacity * 2
        new_data = [None] * new_capacity
        i = 0
        while i < self._size:
            new_data[i] = self._data[(self._head + i) % self._capacity]
            i += 1
        self._data = new_data
        self._capacity = new_capacity
        self._head = 0
        self._tail = self._size

    def enqueue(self, value):
        if self._size == self._capacity:
            self._grow()
        self._data[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError("dequeue from empty queue")
        value = self._data[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def is_empty(self):
        return self._size == 0
