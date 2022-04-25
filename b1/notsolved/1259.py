result = []

while True:
    flag = 'yes'
    a = input()

    if a == '0' :
        for i in range(len(result)):
            print(result[i])
        break

    for i in range(int(len(a)/2)):
        if(a[i] != a[-i -1]):
            flag = 'no'

    result.append(flag)