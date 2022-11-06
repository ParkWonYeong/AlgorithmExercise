
def recursion_func(n):

    for i in bom[:n+1]:
        print(n*"____", i)
    
    if n >= 4:
        return

    recursion_func(n+1)
    
    print(n*"____", '라고 hamwad가 말했다')


bom =['코딩 별로 안좋아하는데', '저런건 재밌다', '남이 해석해주는것도',
    '같이 들어서 재밌다', '얘들아 같이 풀자']

recursion_func(0)