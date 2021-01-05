# N개의 정수가 주어질 때, 각 정수 M에 대하여 a+b+c=M인 직각삼각형의 각 변인 a, b, c의 곱의 최댓값을 구하여라
# Given N integers, for each integer M, find the maximum product where a+b+c=M and a, b, c are sides of a right triangle

for _ in range(int(input())):
    n = int(input())
    ans = -1
    for a in range(3, n//3+1):
        b = (n**2 - 2*n*a)/(2*(n - a))
		if b == int(b):
			c = n-b-a
			if a*b*c > ans:
				ans = a*b*c
    print(int(ans))