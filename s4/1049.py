import math

[buy,brand] = list(map(int, input().split()))
sixMin = 1000
oneMin = 1000

for i in range(brand): # 출력받아 최소 최대 구하기
    [six, one] = list(map(int, input().split()))
    if(six < sixMin): 
        sixMin = six
    if(one < oneMin):
        oneMin = one
if(oneMin * 6 < sixMin):
    print(buy*oneMin)
else: #수정
    if(oneMin*(buy%6)> sixMin):
        print((sixMin * math.ceil(buy / 6)))
    else:
        print((sixMin * (buy // 6))+(oneMin * (buy % 6)))