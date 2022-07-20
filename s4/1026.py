amount = int(input())
array1 = list(reversed(sorted(list(map(int, input().split())))))
array2 = sorted(list(map(int, input().split())))
cnt = 0
for i in range(amount):
    cnt += array1[i] * array2[i]
print(cnt)