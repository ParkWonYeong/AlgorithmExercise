## 1110

# 2 + 6 = 8  -> 68
# 6 + 8 = 14 -> 84
# 8 + 4 = 12 -> 42
# 4 + 2 = 6  -> 26  <===== cycle length: 4

n = int(input())    # 숫자 n을 받는다.
num = n
cnt = 0
while 1:
    num_10 = num // 10              # 0~99까지이므로 10의 자릿수를 구한다.(한자리수면 0이 됨)
    num_1 = num % 10                # 1의 자릿수를 구한다.
    # 이때 'num_1 = num - num_10' 으로 했더니 시간초과가 떴다. 이 방법이 훨씬 빠른듯하다.
    cal = (num_10 + num_1) % 10     # 연산 결과 1의 자릿수를 구한다.
    num = num_1*10 + cal            # 이전의 1의 자릿수와 연산 결과 1의 자릿수를 더한다.
    cnt += 1

    if num == n: break

print(cnt)

# 30840KB, 76ms