"""
Prof. SRS is on a trip with a set of students of his course. He has taken several packets of candies to be distributed
among the students. Unfortunately, the sizes of the packets are not the same and the professor would like to distribute
the candies in an unbiased way. A solution is to open all the packets and move some candies from the larger packets to
the smaller ones so that each packet contains equal number of candies. Your task is to determine the minimum number of
such moves to ensure all packets have the same number of candies.

(One move indicates picking one candy from a packet and moving it to the other)

Input Format:

The first line of the input contains space separated integers indicating the sizes of each packet.

Output Format:

Display a single integer indicating the minimum number of moves required to equalize the size of each packet.

If it is not possible to equalize, display -1 as output.

Example:

Input:

1 1 1 1 6

Output:

4

Input:

3 4

Output:

-1
"""

def solve():
    arr = list(map(int, input().split()))
    # print(arr, len(arr))
    sum = 0
    for i in arr:
        sum += i
    # print(sum)
    if sum % 2 == 1 or len(arr) == 0:
        return -1
    avg = sum / len(arr)
    count = 0
    for i in arr:
        if i < avg:
            count += avg - i
        elif i > avg:
            count += i - avg
    return int(count // 2)

print(solve())