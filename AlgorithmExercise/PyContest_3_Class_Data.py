import datetime

# 한 줄에 year, month, day 3개 정수 입력받고 튜플 (yr, mn, dy)로 반환
def inputDate():
    yr, mn, dy = map(int, input().split())
    return yr, mn, dy

# 윤년인지 확인
def isLeapYear(yr): 
    if yr % 4 == 0:     # 윤년인 경우
        return True
    else:
        return False

# 서기 1년 1월 1일부터 몇 번째 날짜인지 계산하여 반환하는 함수
def getElapsedDaysFromJan01Ad01(yr, mn, dy):
    return str(datetime.date(yr, mn, dy).toordinal())

# 무슨 요일인지 파악
def getWeekDayName(yr, mn, dy):
    w_num = datetime.date(yr, mn, dy).weekday()
    if w_num == 0:
        return 'Monday'
    elif w_num == 1:
        return 'Tuesday'
    elif w_num == 2:
        return 'Wednesday'
    elif w_num == 3:
        return 'Thursday'
    elif w_num == 4:
        return 'Friday'
    elif w_num == 5:
        return 'Saturday'
    else:
        return 'Sunday'