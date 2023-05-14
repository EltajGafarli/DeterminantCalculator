class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self._matrix = matrix
        print(matrix)

    def isValidMatrix(self) -> bool:

        if len(self._matrix) != len(self._matrix[0]):
            raise MatrixException("Kvadrat matris daxil edin")

        count_of_elements_each_row = set(map(len, self._matrix))
        return len(count_of_elements_each_row) == 1

    def calculate(self) -> int:
        if not self.isValidMatrix():
            raise MatrixException("Matrisi düzgün daxil edilməyib")

        return Matrix.find_determinant(self._matrix)

    @staticmethod
    def find_determinant(matrix: list[list[int]]):
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for j in range(len(matrix)):
                submatrix = []
                for i in range(1, len(matrix)):
                    subrow = []
                    for k in range(len(matrix)):
                        if k != j:
                            subrow.append(matrix[i][k])
                    submatrix.append(subrow)
                sign = (-1) ** j
                det += sign * matrix[0][j] * Matrix.find_determinant(submatrix)
            return det


class MatrixException(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
