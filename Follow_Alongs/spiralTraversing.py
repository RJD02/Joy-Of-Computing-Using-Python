import turtle


turtle.bgcolor("black")
leo = turtle.Turtle() #  As in Teenage Mutant Ninja Turtles
width = 5
height = 7
dist = 25
leo.setpos(-250, 250)


def spiral(row, col): #  mat = Matrix(list of list), row = number of rows, col = number of columns
    r, c = 0, 0
    flag = 0
    leo.color("white")
    while r < row and c < col:
        #  leo.color("red")
        if flag == 1:
            leo.right(90) #  Rotating leo by 90 degrees
        for i in range(c, col): #  Printing the first row from remaining rows
            leo.color("red")
            leo.forward(dist)
            #  print(mat[r][i], end = " ")
        r += 1
        flag = 1
        leo.right(90)
        for i in range(r, row): #  Printing the last column from remaining cloumn
            leo.color("green")
            leo.forward(dist)
            #  print(mat[i][col - 1], end = " ")
        col -= 1
        leo.right(90)
        if r < row:
            for i in range(col - 1, c - 1, -1):
                leo.color("orange")
                leo.forward(dist)
                #  print(mat[row - 1][i], end = " ")
            row -= 1
        leo.right(90)
        if c < col:
            for i in range(row - 1, r - 1, -1):
                leo.color("pink")
                leo.forward(dist)
                #  print(mat[i][c], end = " ")
            c += 1
    return

def main():
    #  n = int(input())
    spiral(20, 20)
    return
main()
