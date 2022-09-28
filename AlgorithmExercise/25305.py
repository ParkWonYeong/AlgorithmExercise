## 커트라인

import sys
input = sys.stdin.readline

n,k = map(int, input().split())     # n=응시자 수, k=수상자 수

student = list(map(int, input().split()))
student.sort(reverse=True)  # 내림차순 정렬

print(student[k-1])         # 수상자 커트라인