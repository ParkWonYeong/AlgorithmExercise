def solution(s, times):

    answer = [1, 1]
    Year, Month, Day, Hour, Minutes, Sec = map(int, s.split(':'))
    year, month, day, hour, minutes, sec = Year, Month, Day, Hour, Minutes, Sec

    for i in range(len(times)):
        dd, hh, mm, ss = map(int, times[i].split(':'))
        
        # 다음 저축까지 걸린 시간을 추가하여 시간 계산
        sec += ss
        if sec > 59:
            minutes += sec // 60
            sec %= 60

        minutes += mm
        if minutes > 59:
            hour += minutes // 60
            minutes %= 60

        hour += hh
        if hour > 23:
            day += hour // 24
            hour %= 24

        day += dd
        if day > 30:
            month += day // 30
            day %= 30
        
        if month > 12:
            year += month // 12
            month %= 12
        
        if day-Day >= 2:    # 1일 1저축에 실패했을 경우
            answer[0] = 0
        
        if day-Day < 0:     # 음수 나올 경우. 즉, 달이 바뀌어서 day가 더 작아진 경우
            answer[1] += (30+day) - Day
        elif day-Day > 0:
            answer[1] += day-Day

        # 계산 후 비교할 기준값 갱신
        Year, Month, Day, Hour, Minutes, Sec = year, month, day, hour, minutes, sec
    
    
    return answer