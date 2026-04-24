from queue import Queue
from matrix import Matrix
from maze_data import MazeData
from vector import Vector


class MazeSolver:
    def __init__(self):
        self._maze = None
        self._path = None

    def clear(self):
        self._maze = None
        self._path = None

    def _is_walkable(self, row, col):
        if self._maze is None:
            return False
        if row < 0 or row >= self._maze.rows or col < 0 or col >= self._maze.cols:
            return False
        ch = self._maze.grid.get(row, col)
        return ch == '.' or ch == 'S' or ch == 'G'

    def load_maze(self, path):
        self._path = None
        try:
            with open(path, "r", encoding="utf-8") as f:
                first = f.readline()
                if not first:
                    raise ValueError("missing dimensions")
                parts = first.strip().split()
                if len(parts) != 2:
                    raise ValueError("invalid dimensions")

                rows = int(parts[0])
                cols = int(parts[1])
                if rows <= 0 or cols <= 0:
                    raise ValueError("invalid dimensions")

                grid = Matrix(rows, cols)
                start = None
                goal = None

                row = 0
                while row < rows:
                    line = f.readline()
                    if line == "":
                        raise ValueError("missing row")
                    line = line.rstrip("\n").rstrip("\r")
                    if len(line) != cols:
                        raise ValueError("invalid row length")

                    col = 0
                    while col < cols:
                        ch = line[col]
                        if ch != '#' and ch != '.' and ch != 'S' and ch != 'G':
                            raise ValueError("invalid cell")
                        grid.set(row, col, ch)
                        if ch == 'S':
                            if start is not None:
                                raise ValueError("multiple starts")
                            start = (row, col)
                        if ch == 'G':
                            if goal is not None:
                                raise ValueError("multiple goals")
                            goal = (row, col)
                        col += 1
                    row += 1

                if start is None or goal is None:
                    raise ValueError("missing start or goal")

                self._maze = MazeData(rows, cols, grid, start, goal)
                print(f"MAZE_LOADED rows={rows} cols={cols}")
        except Exception:
            self._maze = None
            self._path = None
            print("ERROR: INVALID_MAZE")

    def print_maze(self):
        if self._maze is None:
            print("ERROR: NO_MAZE")
            return

        print("MAZE")
        row = 0
        while row < self._maze.rows:
            chars = [' '] * self._maze.cols
            col = 0
            while col < self._maze.cols:
                chars[col] = self._maze.grid.get(row, col)
                col += 1
            print("".join(chars))
            row += 1

    def solve(self):
        if self._maze is None:
            print("ERROR: NO_MAZE")
            return

        rows = self._maze.rows
        cols = self._maze.cols
        start_r, start_c = self._maze.start
        goal_r, goal_c = self._maze.goal

        visited = Matrix(rows, cols, False)
        parent = Matrix(rows, cols, -1)

        q = Queue(rows * cols if rows * cols > 0 else 1)
        start_idx = start_r * cols + start_c
        goal_idx = goal_r * cols + goal_c

        q.enqueue(start_idx)
        visited.set(start_r, start_c, True)

        found = False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while not q.is_empty():
            curr_idx = q.dequeue()
            curr_r = curr_idx // cols
            curr_c = curr_idx % cols

            if curr_idx == goal_idx:
                found = True
                break

            d = 0
            while d < 4:
                nr = curr_r + directions[d][0]
                nc = curr_c + directions[d][1]
                if self._is_walkable(nr, nc) and not visited.get(nr, nc):
                    next_idx = nr * cols + nc
                    visited.set(nr, nc, True)
                    parent.set(nr, nc, curr_idx)
                    q.enqueue(next_idx)
                d += 1

        if not found:
            self._path = None
            print("UNSOLVABLE")
            return

        reverse_path = Vector(8)
        curr = goal_idx
        while curr != -1:
            rr = curr // cols
            cc = curr % cols
            reverse_path.append((rr, cc))
            if curr == start_idx:
                break
            curr = parent.get(rr, cc)

        path = Vector(reverse_path.size())
        i = reverse_path.size() - 1
        while i >= 0:
            path.append(reverse_path.get(i))
            i -= 1

        self._path = path
        print("SOLVED")
        print(f"-> length={path.size() - 1}")

    def print_path(self):
        if self._maze is None:
            print("ERROR: NO_MAZE")
            return

        print("PATH")
        if self._path is None or self._path.size() == 0:
            print("NO_PATH")
            return

        i = 0
        while i < self._path.size():
            row, col = self._path.get(i)
            print(f"-> ({row},{col})")
            i += 1

    def process_command(self, tokens):
        if tokens.size() == 0:
            return False

        command = tokens.get(0).upper()

        if command == "LOAD_MAZE":
            if tokens.size() != 2:
                print("ERROR: INVALID_MAZE")
            else:
                self.load_maze(tokens.get(1))
            return False

        if command == "PRINT_MAZE":
            self.print_maze()
            return False

        if command == "SOLVE":
            self.solve()
            return False

        if command == "PRINT_PATH":
            self.print_path()
            return False

        if command == "CLEAR":
            self.clear()
            print("CLEARED")
            return False

        if command == "QUIT":
            return True

        print("ERROR: INVALID_COMMAND")
        return False
