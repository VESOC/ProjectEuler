# 20x20의 정수로 이루어진 격자가 주어질 때 수평, 수직, 또는 대각선 방향으로 연속된 수 네 개의 곱 중 최댓값을 구하시오
# Given 20x20 grid of integers, find the greatest product of four adjacent numbers in the same direction

data = [list(map(int, input().split())) for _ in range(20)]
ans = 0
for i in range(20):
    for j in range(20):
        if j+3 < 20:
            ans = max(data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3], ans)
            if i + 3 < 20:
                ans = max(data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3], ans)
        if i + 3 < 20:
            ans = max(data[i][j]*data[i+1][j] * data[i+2][j]*data[i+3][j], ans)
            if j - 3 > -1:
                ans = max(data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3], ans)
print(ans)
