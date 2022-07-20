flow = 'UP'
is_mountain = 'YES'
input()
string1 = list(map(int,input().split(" ")))
# string1 = list(map(int,input().split(" ")))
for i in range(0,len(string1)-1):
    if flow == 'UP':
        if (string1[i]>=string1[i+1]):
            flow = 'DOWN'
    if flow == 'DOWN':
        if (string1[i]<=string1[i+1]):
            is_mountain = 'NO'

# print(flow)
print(is_mountain)