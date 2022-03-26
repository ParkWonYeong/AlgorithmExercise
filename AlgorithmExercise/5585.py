## 5585

change = 1000-int(input())          # 거스름돈
coin = [500, 100, 50, 10, 5, 1]     # 코인 단위
cnt = 0

for i in coin:
    cnt += change // i              # 0이면 0인대로. 거스름돈에 적용가능한 큰 단위의 동전부터 센다
    change %= i                     # 남은 거스름돈을 다음 반복에 적용한다
    if change==0:break              # 거스름돈 정산이 완료되면 반복문을 빠져나간다
print(cnt)



## 별해 ##

change = 1000-int(input())

cnt = 0
while change != 0:
    if (change // 500) != 0:        # 거스름돈이 500엔 이상이면 500엔 사용 
        muxnum = change//500
        change %= 500               # 혹은 change -= 500 * muxnum
        cnt += muxnum

    elif (change // 100) != 0:      # 거스름돈이 100엔 이상이면 100엔 사용 
        muxnum = change//100
        change %= 100               # 혹은 change -= 100 * muxnum
        cnt += muxnum

    elif (change // 50) != 0:       # 거스름돈이 50엔 이상이면 50엔 사용 
        muxnum = change//50
        change %= 50                # 혹은 change -= 50 * muxnum
        cnt += muxnum

    elif (change // 10) != 0:       # 거스름돈이 10엔 이상이면 10엔 사용 
        muxnum = change//10
        change %= 10                # 혹은 change -= 10 * muxnum
        cnt += muxnum

    elif (change // 5) != 0:        # 거스름돈이 5엔 이상이면 5엔 사용 
        muxnum = change//5
        change %= 5                 # 혹은 change -= 50 * muxnum
        cnt += muxnum

    elif (change // 1) != 0:        # 거스름돈이 1엔 이상이면 1엔 사용 
        muxnum = change//1
        change %= 1                 # 혹은 change -= 1 * muxnum
        cnt += muxnum

print(cnt)


# 30864KB, 64ms