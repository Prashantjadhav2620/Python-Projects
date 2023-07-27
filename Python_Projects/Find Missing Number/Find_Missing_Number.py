

def Find_Missing_Number(n):
    num = set(n)
    length = len(n)
    miss_num=[]
    for i in range(1, n[-1]):
        if i  not in num:
            miss_num.append(i)
    return miss_num  



list=[1,2,3,5,7,8,9,14,17,18,20] 


print(Find_Missing_Number(list))     

# Output: -

# [4, 6, 10, 11, 12, 13, 15, 16, 19]