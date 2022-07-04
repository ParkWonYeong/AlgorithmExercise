## 카드 정렬하기

n = int(input())

card = [0]*n
for i in range(n):
    card[i] = int(input())

ans = 0
while 1:            # break 할때까지 반복
    card.sort()
    ans += card.pop(0) + card.pop(0)
    card.append(ans)
    if len(card) <= 1:  # 모두 섞였으면 반복문 중지
        break

print(card[0])