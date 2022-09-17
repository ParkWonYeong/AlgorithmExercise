## 최소, 최대 - N개의 정수 중 최솟값과 최댓값을 구한다.

n = int(input())    # 정수의 개수
num = list(map(int, input().split()))
print(min(num), max(num))