# N개의 수가 주어질때 각 수의 가장 큰 소수인 약수를 구하시오
# Given N integers, find the largest prime factor of each input

def smallest_prime(n):
    i = 3
    while i*i <= n:
        if n%i == 0:
            return i
        i += 2
    return n
for _ in range(int(input())):
    n = int(input())
    while n % 2 == 0:
        n //= 2
    while True:
        sp = smallest_prime(n)
        if sp < n:
            n //= sp
        else:
            print(n)
            break