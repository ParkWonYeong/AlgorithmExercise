## 10773

k = int(input())
money = []*100001

for i in range(k):
    one = int(input())
    if one == 0:                    # 0인 경우
        money.pop()
    else:                           # 0이 아닌 경우
        money.append(one)

print(sum(money))

## 31620KB, 4000ms