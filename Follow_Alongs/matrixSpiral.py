def spiral(mat, row, col): #  mat = Matrix(list of list), row = number of rows, col = number of columns
    r, c = 0, 0
    while r < row and c < col:
        for i in range(c, col): #  Printing the first row from remaining rows
            print(mat[r][i], end = " ")
        r += 1
        for i in range(r, row): #  Printing the last column from remaining cloumn
            print(mat[i][col - 1], end = " ")
        col -= 1
        if r < row:
            for i in range(col - 1, c - 1, -1):
                print(mat[row - 1][i], end = " ")
            row -= 1
        if c < col:
            for i in range(row - 1, r - 1, -1):
                print(mat[i][c], end = " ")
            c += 1


count = 1
#  mat = [[i for i in range(4)] for j in range(4)]
mat = []
for i in range(4):
    mat.append([])
    for ii in range(4):
        mat[i].append(count)
        count += 1
print(mat)
spiral(mat, 4, 4)
