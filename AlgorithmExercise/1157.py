## 1157

s = input().upper()
s1 = list(set(s))
cnt = []

ans_max = 0
ans = ''
for i in s1:
    counter = s.count(i)
    cnt.append(counter)

if cnt.count(max(cnt)) >= 2:    # 최대개수의 알파벳이 여러개인 경우
    print('?')
else:
    print(s1[(cnt.index(max(cnt)))])

# 32796KB, 108ms