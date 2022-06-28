## 왕실의 나이트
# 체스판은 8x8

# 1. 수평 두칸 이동, 수직 한칸 이동
# 2. 수직 두칸 이동, 수평 한칸 이동
# 1 -> 좌우 2가지 * 수직 위아래 2가지
# 2 -> 상하 2가지 * 수평 좌우 2가지

# a의 아스키 코드 값은 97
# 가로 97, 98, 99, 100, 101, 102, 103, 104
# 세로 1, 2, 3, 4, 5, 6, 7, 8

location = input()
w = ord(location[0])
h = int(location[1])
print(w,h)
cnt = 0
# 1번처럼 이동하는 경우
if (w-2 >= 97):
    cnt += 1
    if (h-1 >= 1):
        cnt += 1
    if (h+1 <= 8):
        cnt += 1
elif (w+2 <= 104):
    cnt += 1
    if (h-1 >= 1):
        cnt += 1
    if (h+1 <= 8):
        cnt += 1
# 2번처럼 이동하는 경우
if (h-2 >= 1):
    cnt += 1
    if (w-1 >= 97):
        cnt +=1
    if (w+1 <= 104):
        cnt += 1
elif (h+2 <= 8):
    cnt += 1
    if (w-1 >= 97):
        cnt +=1
    if (w+1 <= 104):
        cnt += 1
print(cnt)