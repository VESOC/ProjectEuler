# N개의 정수가 주어질때, 각 정수 M에 대하여 1부터 M까지의 합의 제곱과 각각의 제곱의 합과의 차를 구하시오
# Given N integers, for each integer M, find the difference between the sum of squares of the first M natural numbers and the square of the sum.

for _ in range(int(input())):
    n = int(input())
    sum_of_squares = n*(n+1)*(2*n+1) // 6
    square_of_sum = (n*(n+1)//2)**2
    print(square_of_sum-sum_of_squares)