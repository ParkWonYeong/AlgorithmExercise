## 1085

# X,Y,W,H 순으로 입력
x,y,w,h = map(int, input().split())
ans = min(x, y, abs(w-x), abs(y-h))
print(ans)

# 30840KB, 72ms