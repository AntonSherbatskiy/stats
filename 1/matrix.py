class matrix:
    def __init__(self) -> None:
        self.rows_count = 0
        self.cols_count = 0
        self.inner_arr = []


    def at(self, row_index: int, col_index: int) -> int:
        return self.inner_arr[row_index][col_index]


    def append_row(self, row: list) -> None:
        self.inner_arr.append(row)


    def __str__(self) -> str:
        line = ''
        for i in range(len(self.inner_arr)):
            for j in range(len(self.inner_arr[i])):
                line += str(self.inner_arr[i][j]) + '\t'
            line += '\n'

        return line