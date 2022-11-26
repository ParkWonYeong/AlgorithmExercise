import fileinput
import math

def fGetFloatData(file_name):
    # dir1 = 'Exam2_21811954_박원영\float_data.txt'
    # dir = 'C:/Users/IT/Desktop/21811954_박원영\Exam2_21811954_박원영\float_data.txt'
    # open(dir1)
    float_num = []
    float_n = []
    for i in range(4):
        float_n = map(float, input().split())
        for j in float_n:
            float_num.append(j)
    return float_num

def printFloatList(L, per_line):
    print('    '.join(''))
    for i in range(per_line//len(L)):
        for j in range(per_line):
            print(str(L[i]).join(' '))
        print()

# 리스트의 최소값, 최대값, 평균값, 분산, 표준편차
def getStatistics(L):

    L_sum = 0
    for s in L:
        L_sum += s
    L_avg = L_sum/len(L)

    L_dev = 0
    for i in L:
        L_dev += i**2
    L_dev = L_dev/len(L)

    L_std = math.sqrt(L_dev)

    mylist = [min(L), max(L), L_avg, L_dev, L_std]

    return mylist


# 오름차순 또는 내림차순으로 정렬, (리스트, 정렬 방향(increasing or decreasing))
def sortList(L, sort_parameter):
    
    if sort_parameter == "increasing":
        L.sort()
    elif sort_parameter == "decreasing":
        L.sort(reverse = True)
    
    return L

def main():
    print("2022 Python Contest 2 - 학번: 21811954, 성명: 박원영")
    L_float = fGetFloatData("float_data.txt")
    
    L_info = getStatistics(L_float)
    L_min, L_max, L_avg, L_dev, L_std = L_info[0],L_info[1],L_info[2],L_info[3], L_info[4]
    print("L_min({:.2f}), L_max({:.2f}), L_avg({:.2f}), L_dev({:.2f}), L_std({:.2f})"\
        .format(L_min, L_max, L_avg, L_dev, L_std))

    sortList(L_float, "increasing")
    print("L_float after sorting in increasing order : ")
    printFloatList(L_float, 10)

    sortList(L_float, "decreasing")
    print("L_float after sorting in decreasing order : ")
    printFloatList(L_float, 10)

main()