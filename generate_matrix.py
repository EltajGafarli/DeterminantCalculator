from random import randint


def generate_matrix() -> list[list[int]]:
    dimension: int = randint(0, 10)
    matrix = []
    for i in range(dimension):
        row = []
        for j in range(dimension):
            element = randint(0, 10)
            row.append(element)
        matrix.append(row)

    return matrix


def convert_matrix_to_string(matrix: list[list[int]]) -> str:
    result = ""
    for row in matrix:
        row = list(map(str, row))
        result += " ".join(row) + "\n"

    return result
