import random
import sys

def main(n):
    print(n)
    for i in range(n):
        print(random.randint(1, n))

n = int(sys.argv[1])
main(n)