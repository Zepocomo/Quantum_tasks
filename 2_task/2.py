def count_islands(M, N, matrix):
    def dfs(i, j):
        if i < 0 or i >= M or j < 0 or j >= N or matrix[i][j] != 1:
            return
        matrix[i][j] = -1
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    count = 0
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                dfs(i, j)
                count += 1
    return count

M1 = 3
N1 = 3
matrix1 = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 1]

]

M2 = 3
N2 = 4
matrix2 = [
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0]

]

M3 = 3
N3 = 4
matrix3 = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 1]

]

num_islands1 = count_islands(M1, N1, matrix1)
num_islands2 = count_islands(M2, N2, matrix2)
num_islands3 = count_islands(M3, N3, matrix3)
print("\nNumber of islands in first example:", num_islands1)
print("Number of islands in second example:", num_islands2)
print("Number of islands in third example:", num_islands3,'\n')