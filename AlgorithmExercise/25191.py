## 25191 ## 곰곰컵

# 시켜먹을수있는 치킨 수 N
# 집에 있는 콜라 개수 A(얘는 2개씩), 맥주 개수 B(1개씩)

n = int(input())                    # 치킨 개수
a,b = map(int, input().split())     # 콜라, 맥주

ans = a//2 + b

if ans <= n:
    print(ans)
else:
    print(n)

# 30840KB, 80ms