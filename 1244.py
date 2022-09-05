switch_cnt = int(input())
switchs = list(map(int, input().split(" ")))
# switchs = list(map(int, "0 1 0 1 0 0 0 1".split(" "))) 
stu_cnt = int(input())
for _ in range(stu_cnt):
    [sex, num] =  list(map(int, input().split(" "))) #성별,숫자
    if sex == 1:
        limit_num = switch_cnt // num # 배수의 마지막
        for i in range(limit_num):
            switchs[((i+1)*num)-1] = 1 if switchs[((i+1)*num)-1] == 0 else 0 # 토글 로직
    else : 
        limit_num = num if switch_cnt/2 > num else switch_cnt-num #0이랑 끝 중에 가까운 수
        start, end = 0,0
        for i in range(1,limit_num):
            if(switchs[num-i-1] == switchs[num+i-1]):
                start,end = num-i-1,num+i-1
        for i in range(start,end+1):
            switchs[i] = 1 if switchs[i] == 0 else 0 # 토글 로직
print(" ".join(map(str, switchs[0:20])))
# for i in range()

'''
3이면 세번 돌리기
3-1 = 3+1
3-2 = 3+2
3-3 = 3+3
'''