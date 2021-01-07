# N개의 정수가 주어질때, 각 정수 M보다 작은 소수들의 합을 출력하시오
# Given N integers, for each integer M, find the sum of all primes less than or equal to M

limit = 1000001
primes = list(range(limit))
primes[0] = primes[1] = 0
sum_of_primes = [0]*limit
for i in range(2, limit):
    if primes[i]:
		sum_of_primes[i] = sum_of_primes[i-1] + primes[i]
        for j in range(i*i, limit, i):
            primes[j] = 0
	else:
		sum_of_primes[i] = sum_of_primes[i-1]
for _ in range(int(input())):
    print(sum_of_primes[int(input())])