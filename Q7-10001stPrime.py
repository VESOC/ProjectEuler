# N개의 자연수가 주어질 때, 각 수 M에 대하여 M번째 소수를 구하시오
# Given N integers, for each integer M, find the Mth prime

limit = 200000
primes = list(range(limit))
primes[0], primes[1] = 0, 0
for i in range(2, limit):
    if primes[i]:
        for j in range(i+i, limit, i):
            primes[j] = 0
primes = tuple(prime for prime in primes if prime)
for _ in range(int(input())):
    print(primes[int(input())-1])