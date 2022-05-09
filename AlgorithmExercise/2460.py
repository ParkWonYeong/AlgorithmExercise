## 2460

a, b = map(str, input().split())

# binary화 : bin(숫자형)[2:]
print(bin(int(a,2)+int(b,2))[2:])