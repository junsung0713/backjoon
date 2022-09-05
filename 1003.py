fib_one_list = [0 for _ in range(20)];
fib_zero_list = [0 for _ in range(20)];

fib_
def fibo(n,i):
    if(n == 1):
        fib_one_list[i] += 1
        return 1;
    if(n == 0):
        fib_zero_list[i] += 1
        return 0;
    return fibo(n-1,i) + fibo(n-2,i)

number = int(input())
for i in range(number):
    fibo(int(input()),i)

for i in range(number):
    print("{} {}".format(fib_zero_list[i],fib_one_list[i]))


# fib_one_list = [0 for _ in range(20)];
# fib_zero_list = [0 for _ in range(20)];

# def fibo(n,i):
#     if(n == 1):
#         fib_one_list[i] += 1
#         return 1;
#     if(n == 0):
#         fib_zero_list[i] += 1
#         return 0;
#     return fibo(n-1,i) + fibo(n-2,i)

# number = int(input())
# for i in range(number):
#     fibo(int(input()),i)

# for i in range(number):
#     print("{} {}".format(fib_zero_list[i],fib_one_list[i]))