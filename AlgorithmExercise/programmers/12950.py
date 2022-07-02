## 12950

def solution(arr1, arr2):

    answer = [[0 for _ in range(len(arr1[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

### 별해: numpy를 이용한 방법 ###
import numpy as np

def solution(A,B):
    A,B=np.array(A), np.array(B)
    answer=A+B
    return answer.tolist()