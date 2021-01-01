# N개의 수가 주어질때 세자리 수 두개를 곱하여 만들 수 있는 대칭수 중 각 수보다 작은 것들 중 가장 큰 것을 고르시오
# Given N integers, find the largest palindrome made from the product of two 3-digit numbers which is less than each integer

palindrome = set()
for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		if (i*j) % 11 == 0:
			s = str(i*j)
			if s == s[::-1]:
				palindrome.add(i*j)
palindrome = sorted(palindrome)
for _ in range(int(input())):
    n = int(input())
    begin, end = 0, len(palindrome)-1
    while begin <= end:
        mid = (begin+end)//2
        if palindrome[mid] >= n:
            end = mid - 1
        else:
            begin = mid + 1
    print(palindrome[(begin+end)//2])