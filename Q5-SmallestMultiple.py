# N개의 수가 주어질때 각 수 M별로 1부터 M까지의 자연수로 모두 나누어지는 수를 출력하시오
# Given N integers, for each integer M find the smallest integer evenly disible by numbers 1 to M

for _ in range(int(input())):
    n = int(input())
    test = 1
    while True:
        for i in range(1, n+1):
            if test%i:
                break
        else:
            print(test)
            break
        test += 1
# --- #
from math import gcd
from functools import reduce

for _ in range(int(input())):
    print(reduce(lambda x,y: x*y//gcd(x,y), range(1, int(input())+1)))