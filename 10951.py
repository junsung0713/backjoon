while True:
    try:
        a,b = list(map(int, input().split(" ")))
    except:
        break;
    print(a+b)