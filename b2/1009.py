n = int(input())
for i in range(n):
    a,number = input().split();
    result = 1
    a = int(a)
    number = str(bin(int(number)))[2:]
    res = [x for x in range(len(number))]
    res[0] = a % 10
    number = reversed(number)
    for idx, i in enumerate(number):
        if(idx>0):
            res[idx] = (res[idx-1]**2)%10
        if(bool(int(i))):
            result *= res[idx]
    real_result = result%10
    print(10 if real_result== 0 else real_result)