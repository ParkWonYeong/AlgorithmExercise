from Class_Data import *

if __name__ == "__main__":
    print("Python Contest Test_3 학번: 21811954, 성명: 박원영")
    while 1:
        print("input year month day : ", end='')
        yr, mn, dy = inputDate()
        if yr == 0:
            break
        dy0101 = getElapsedDaysFromJan01Ad01(yr, mn, dy)
        week_name = getWeekDayName(yr, mn, dy)
        print('('+str(yr)+'-'+str(mn)+'-'+str(dy)+') : '+ dy0101 + '-th days from Jan01AD01, (' + week_name + ')')
        
        # 크리스마스까지 남은 날 확인
        until_christmas = datetime.date(yr,12,25).toordinal() - datetime.date(yr,mn,dy).toordinal()
        if until_christmas == 0:
            print(" Happy Christmas !!")
        elif until_christmas < 0:       # 크리스마스를 지난 날인 경우 다음 해 크리스마스까지 남은 날 계산
            until_christmas = datetime.date(yr+1,12,25).toordinal() - datetime.date(yr,mn,dy).toordinal()
            print(' '+str(datetime.date(yr,12,25).toordinal() - datetime.date(yr,mn,dy).toordinal())+" days left to this year's Christmas !!")
        else:
            print(' '+str(datetime.date(yr,12,25).toordinal() - datetime.date(yr,mn,dy).toordinal())+" days left to this year's Christmas !!")
