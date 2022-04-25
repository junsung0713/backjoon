list1 = list(range(1,10000))
list2 = []
for number in list1:
    res = number
    for num in str(number):
        res = res + int(num)
    if res < 10000:
        list2.append(res)
for num in set(list2):
    list1.remove(num)
for num in list1:
    print(num)