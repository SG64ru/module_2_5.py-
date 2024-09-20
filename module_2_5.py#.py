def get_matrix(n = 1, m = 1, value = 0):
    matrix = []
    for i in range(n):
        matrix.append(([]))
        for j in range(m):
            matrix[i].append(value)
    return matrix
result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
print("Матрица 1: ", result_1)
print("Матрица 2: ", result_2)
print("Матрица 3: ", result_3)
get_matrix()











