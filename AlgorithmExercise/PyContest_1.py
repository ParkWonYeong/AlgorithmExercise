import MyFibo
import time

def main():
    
    print("Python Contest Test_1 학번: 21811954, 성명: 박원영")
    print("start, stop, step for Fibo calculation : ", end='')
    # 피보나치 수열 계산 범위의 start, stop, step 정수 입력
    start, stop, step = map(int, input().split())

    fibo = MyFibo.dynFibo(stop)     # 피보나치 수열 모듈

    for i in range(start, stop+1, step):
        mynum = str(fibo[i]) + ', ' + 'took ' + str(time.process_time()) + ' [ms]'
        print(str(i)+'-th Fibo series = '+ mynum)

    return

if __name__ == "__main__":
    main()