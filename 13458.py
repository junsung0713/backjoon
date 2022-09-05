import math
room_count = int(input())
rooms = list(map(int, input().split()))
result = 0 
general, sub = map(int, input().split())
for room in rooms:
    result += 1
    if(room - general <=0):
        continue
    else:
        room -= general

    result += math.ceil(room/sub)
print(result)