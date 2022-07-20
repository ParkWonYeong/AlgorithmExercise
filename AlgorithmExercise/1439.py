# 둘중 작은 값# 1과 0으로 뒤집는 경우로 나누기
# 둘중 작은 값을 선택

s = input()

cnt0,cnt1 = 0,0
if s[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1
ans = min(cnt0, cnt1)
print(ans)
