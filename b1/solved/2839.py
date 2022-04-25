result = 0
n = int(input())
if(n%5==0):
    result = n/5
else:
    while n > 0:
        if n % 5 == 0:
            result += n/5
            break
        n -= 3
        result += 1
if n < 0:
    print(-1)
else : 
    print(int(result))
# n과 가장가까운작은 근삿값 18 -> 15
# 근삿값이 3으로 나눌수있는지 체크하고 나눌수있으면 /3 result