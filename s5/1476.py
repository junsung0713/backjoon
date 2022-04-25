E, S, M = [1,1,1];
e, s, m = list(map(int, input().split(" ")))
for i in range(1,10000+1):
    if E == 16 :
        E = 1;
    if S == 29 :
        S = 1;
    if M == 20 :
        M = 1;
    if E==e and S==s and M==m:
        # print("i = {} E = {} S = {} M = {}".format(i,E,S,M))
        print(i)
        break
    E+=1
    S+=1
    M+=1