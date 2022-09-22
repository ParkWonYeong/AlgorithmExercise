## 인공지능 시계

now_hour, now_min, now_sec = map(int, input().split())  # 현재시각(시, 분, 초)
oven_time = int(input())    # 오븐구이가 끝나는 시간(초)

# 오븐구이 시간 시,분,초로 환산
# 1분 = 60초 / 60분(1시간) = 60*60 = 3600초
oven_hour = oven_time // 3600
oven_min = (oven_time % 3600) // 60
oven_sec = oven_time - (oven_hour*3600 + oven_min*60)
# print(oven_hour, oven_min, oven_sec)

hour = now_hour + oven_hour
minute = now_min + oven_min
sec = now_sec + oven_sec

if sec >= 60:
    minute += sec // 60
    sec %= 60

if minute >= 60:
    hour += minute // 60
    minute %= 60

if hour >= 24:
    hour %= 24

print(hour, minute, sec)