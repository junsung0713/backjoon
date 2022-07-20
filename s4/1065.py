count_input = int(input())
cnt = 0
for i in range(1,count_input+1):
    number_list = list(map(int, list(str(i))))
    list_len = len(number_list)
    if list_len<3:
        cnt+=1
    else:
        if(number_list[0]+number_list[2] == number_list[1]*2):
            cnt+=1
print(cnt)
