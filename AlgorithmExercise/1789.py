## 1789

# 서로 다른 n개의 자연수의 합 s
s = int(input())

ans,cnt = 0,0
i = 1
while 1:
    ans += i
    cnt += 1
    if ans > s:
        cnt -= 1
        break
    elif ans == s:
        break
    i += 1

print(cnt)

# 30840KB, 104ms