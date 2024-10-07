def get_matrix(n, m, value):
    matrix = []
    for i in range(int(n)):
        row = []
        for j in range(int(m)):
            row.append(int(value))
        matrix.append(row)
    return matrix
n = input('Ввести количество строк: ')
m = input('Ввести количество столбцов: ')
value = input('Введите значение: ')
result = get_matrix(n, m, value)
for row in result:
    print(row)

