def warshall(matrix):
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = 1
    return matrix


#adj_matrix = [[0, 0, 0, 1],
#              [1, 0, 1, 0],
#              [1, 0, 0, 1],
#              [0, 0, 1, 0]]

#transclosure = warshall(adj_matrix)

#transclosure = [[1, 0, 1, 1],
#                [1, 0, 1, 1],
#                [1, 0, 1, 1],
#                [1, 0, 1, 1]]
