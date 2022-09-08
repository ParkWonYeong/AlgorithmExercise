## 만들 수 없는 금액

# 동전 N개
n = int(input())

coin = list(map(int, input().split()))
coin.sort()

check = 1
# n개의 동전을 이용해서 만들 수 없는 양의 정수 금액 중 최솟값
for x in coin:
    if check < x:   # 동전의 단위가 check할 값보다 크면 만들 수 없는 값이다.
        print(check)
        break
    else:
        check += x
        print(check)