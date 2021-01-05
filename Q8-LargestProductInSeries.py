# N개의 정수가 주어질 때, 각 정수 M에서 K개 이어진 수의 곱중 최댓값을 출력하시오
# Given N integers, find the maximum of products of K consecutive digits in each integer

from operator import mul
from functools import reduce
for _ in range(int(input())):
    n, k = map(int, input().split())
    num = list(map(int, input()))
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, reduce(mul, num[i:i+k]))
    print(ans)

# from math import prod
# ans = max(ans, prod(num[i:i+k]))