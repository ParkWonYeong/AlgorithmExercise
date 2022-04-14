## 2562

num = []
ans = 0
for i in range(9):
    a = int(input())
    num.append(a)               # 9개의 자연수를 한줄씩 입력받는다.
    if max(num)==num[i]:        # 받은 값 중 최댓값에 해당할 경우
        ans = i+1

num.sort(reverse=True)          # 오름차순으로 정렬.
print(num[0])
print(ans)

# 30840KB, 68ms