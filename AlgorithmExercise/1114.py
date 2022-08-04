## 1114
## 통나무 자르기

import sys
input = sys.stdin.readline


# L: 통나무의 길이
# K: 통나무를 자를 수 있는 위치 개수
# C: 통나무를 자를 수 있는 횟수
l,k,c = map(int, input().split())

# K개의 통나무 자를 수 있는 위치 번호
location = list(map(int, input().split()))
location.sort()




## 출력 ##
# print((가장 긴 조각의 길이), (그 때 처음 자르는 위치))


# 9 2 1
# 4 5
# ㅁㅁㅁㅁ ㅁㅁㅁㅁㅁ
# => 5 4

# 5 1 2
# 3
# ㅁㅁㅁ ㅁㅁ
# => 3 3

# 5 5 3
# 4 2 5 3 1
# sort -> 1 2 3 4 5
# ㅁ ㅁ ㅁ ㅁㅁ
# => 2 1

# 5 10 10
# 4 3 2 1 4 3 2 1 4 3
# sort -> 1 1 2 2 3 3 3 4 4 4
# ㅁ ㅁ ㅁ ㅁ ㅁ
# => 1 1