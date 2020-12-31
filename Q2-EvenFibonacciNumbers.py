# N개의 수가 주어질 때 각 수보다 작은 짝수 피보나치 항의 합을 출력하라
# Given N integers, print the sum of all even Fibonacci numbers less than the given integers

even_fibonacci = [2]
max_limit = 4*1e16
evFi1, evFi2 = 0, 2
while True:
	next_evFi = 4*evFi2 + evFi1
	if next_evFi >= max_limit:
		break
	evFi1, evFi2 = evFi2, next_evFi
	even_fibonacci.append(evFi2)
for _ in range(int(input())):
	n = int(input())
	S = filter(lambda x: x<n, even_fibonacci)
	print(sum(S))