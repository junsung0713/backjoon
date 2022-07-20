words = input()
resultNumberArray = [];
resultArray = [];
cnt = 0

for i in words:
    if(i != "."):
        cnt+=1
    else:
        resultNumberArray.append(cnt)
        resultNumberArray.append('.')
        cnt = 0
resultNumberArray.append(cnt)

for i in resultNumberArray:
    if(i != "."):
        if(i%2 == 1):
            resultArray = [-1]
            break
        else:
            four = i//4
            two = (i-int(i/4)*4)//2
            resultArray.extend(list('AAAA'*four))
            resultArray.extend(list('BB'*two))
    else:
        resultArray.append(".")
if(resultArray == [-1]):
    print("-1")
else:
    print("".join(resultArray))
