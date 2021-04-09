'''
Consider a directed graph. It can be represented by an adjacency matrix. The nodes are numbered 1 to n. 
If there is an edge from node i to node j, there will be a 1 in the (i-1,j-1) position in the adjacency matrix. 
There are no self loops in the graph. print yes if the given graph is a complete graph (connection from one node 
to all other node) else print no
'''

def solve():
    n = int(input())
    matrix = [[] for i in range(n)]
    l = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for j in range(n):
            matrix[i].append(l[count])
            count += 1
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif matrix[i][j] != 1:
                print('no')
                return
    print('yes')
    return

solve()
