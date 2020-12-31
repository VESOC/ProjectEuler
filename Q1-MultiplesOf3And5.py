# N개의 수가 주어질 때 각 수보다 작은 자연수 중 3 또는 5의 배수의 합을 출력하라
# Given N amount of integers, return the sum of all the mutiples of 3 or 5 below M
# https://coder38611.tistory.com/95

def get_sum_of_mutiples(num, target):
	amt = num//target
	return target*amt*(amt+1)//2
for _ in range(int(input())):
	m = int(input())
	total = get_sum_of_mutiples(m-1, 3) + get_sum_of_mutiples(m-1, 5) - get_sum_of_mutiples(m-1, 15)
	print(total)
'''Line 5~7&10 == Line 13~14'''
# amt_threes, amt_fives, amt_fifteens = (m-1)//3, (m-1)//5, (m-1)//15
# total = (3*amt_threes*(amt_threes+1) + 5*amt_fives*(amt_fives+1) - 15*amt_fifteens*(amt_fifteens+1))//2