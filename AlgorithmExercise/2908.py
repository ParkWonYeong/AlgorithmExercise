s1,s2 = map(str, input().split())
print(max(int(s1[::-1]), int(s2[::-1])))
