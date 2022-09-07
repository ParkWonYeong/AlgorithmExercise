## 문자열 뒤집기

s = input()
cnt = 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1

print(cnt//2)



## 문자열 뒤집기(2회독)

s = input() # 문자열 받기
cnt = 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:      # 다른 숫자가 나올때마다 count
        cnt += 1

print(cnt//2)