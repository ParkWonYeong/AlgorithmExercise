## 못생긴 수

# 못생긴 수: 2,3,5만을 소인수로 가지는 수
# 다이나믹 프로그래밍으로 접근

n = int(input())
ugly = [1]*(n+1)                # 각 인덱스 = 해당 번째수

idx_2=idx_3=idx_5 = 1
mux2, mux3, mux5 = 2,3,5        # 처음은 2,3,5로 시작

# 역으로 1로부터 거슬러 올라간다.
for i in range(2, n+1):
    # 계속 갱신되는 mux2,3,5 값 중 가장 작은 값(오름차순으로 정렬할 것이므로)
    ugly[i] = min(mux2, mux3, mux5)

    if ugly[i] == mux2:
        idx_2 += 1              # 인덱스값 증가
        mux2 = ugly[idx_2]*2    # 2를 약수로 가지는 다음 수로 갱신

    if ugly[i] == mux3:
        idx_3 += 1
        mux3 = ugly[idx_3]*3    # 3을 약수로 가지는 다음 수로 갱신

    if ugly[i] == mux5:
        idx_5 += 1
        mux5 = ugly[idx_5]*5    # 5를 약수로 가지는 다음 수로 갱신

print(ugly[n])