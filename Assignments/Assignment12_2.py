'''
Ramesh and Suresh have written GATE this year. They were not prepared for the exam. 
There were only multiple choice questions. There were 5 options for each question listed 1,2,3,4,5. 
There was only one valid answer. Each question carries 1 mark and no negative mark. 
Ramesh and Suresh are so sure that there is no question that both of them have answered correctly, i.e, 
one of them has given invalid answer. 

 

Now Ramesh wants to know how well he has done the GATE. Given the answers of both Ramesh and Suresh, 
You should tell me what the maximum marks that Ramesh can get.

 

Input Format:

Line1 - Number of Questions in the GATE Exam

Line2 - List of Answers given by Ramesh(Answer no given then its represented by ‘.’)

Line3 - List of Answers given by Suresh (Answer no given then its represented by ‘.’)

 

Output Format:

Maximum score for Ramesh

 

Input:

6

1 2 3 4 5 1

1 2 2 2 5 1

 

Output

2
'''

def solve():
    n = int(input())
    ramesh = input().split()
    suresh = input().split()
    count = 0
    for i in range(n):
        if ramesh[i] != suresh[i] and ramesh[i] != '.':
            count += 1
    print(count)
    return

solve()
