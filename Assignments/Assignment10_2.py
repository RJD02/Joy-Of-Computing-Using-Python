'''
Consider a directed graph. It can be represented by an adjacency matrix. The nodes are numbered 1 to n. If there is an edge from node i to node j, there will be a 1 in the (i-1,j-1) position in the adjacency matrix. There are no self loops in the graph. For a node, the number of head ends adjacent to a node is called the indegree of the node and the number of tail ends adjacent to a node is its outdegree. Print 'yes'  and the node number if  in the given graph there is a node with outdegree 2, else print 'no'. Adjacency matrix is given as a line of zeros and ones in row major order i.e, row 1 will be given as input first then row 2 so on. There will be only one edge with outdegree 2.


Input format :

Line 1 - Number of nodes

Line 2 - Adjacency matrix in row major order


Output format : if the condition is satisfied then yes node_number else no


Example 

input:

4
0 1 0 0 0 0 0 1 1 0 0 0 0 1 0 

output

yes 2
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
    d = {x:0 for x in range(n)}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                d[j] += 1
    for i in d.keys():
        if d[i] == 2:
            print('yes', i + 1)
            return
    print('no')
    return

solve()
