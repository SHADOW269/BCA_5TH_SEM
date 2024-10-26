def strassen_matrix(a, b):
    m1 = (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
    m2 = (a[1][0] + a[1][1]) * b[0][0]
    m3 = a[0][0] * (b[0][1] - b[1][1])
    m4 = a[1][1] * (b[1][0] - b[0][0])
    m5 = (a[0][0] + a[0][1]) * b[1][1]
    m6 = (a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
    m7 = (a[0][1] - a[1][1]) * (b[1][0] + b[1][1])

    c = [[0, 0], [0, 0]]
    c[0][0] = m1 + m4 - m5 + m7
    c[0][1] = m3 + m5
    c[1][0] = m2 + m4
    c[1][1] = m1 + m3 - m2 + m6

    return c
def input_matrix():
    matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            element = int(input(f"Enter element at posiƟon ({i},{j}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)
print("Enter the first 2x2 matrix:")
matrix1 = input_matrix()
print("\n First Matrix is:")
print_matrix(matrix1)
print("Enter the second 2x2 matrix:")
matrix2 = input_matrix()
print("\n Second Matrix is:")
print_matrix(matrix2)
result = strassen_matrix(matrix1, matrix2)
print("\nResulƟng Matrix:")
print_matrix(result)