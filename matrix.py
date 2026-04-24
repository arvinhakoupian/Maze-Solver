class Matrix:
    def __init__(self, rows, cols, default_value=None):
        self.rows = rows
        self.cols = cols
        self._data = [default_value] * (rows * cols)

    def _idx(self, row, col):
        return row * self.cols + col

    def get(self, row, col):
        return self._data[self._idx(row, col)]

    def set(self, row, col, value):
        self._data[self._idx(row, col)] = value
