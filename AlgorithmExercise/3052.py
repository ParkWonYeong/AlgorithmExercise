## 나머지

# 수 10개를 입력받은 뒤 각각을 42로 나눈 나머지를 구하고,
#  서로 다른 값이 몇개인지 출력

num = []

for i in range(10):
    n = int(input())
    x = n%42
    if x not in num:
        num.append(x)

print(len(num))