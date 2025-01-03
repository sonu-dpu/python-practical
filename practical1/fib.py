def fib(n):
    print(f'{n} fibonacci number :')
    a=0
    b=1
    for _ in range(n):
        print(a,end=" ")
        c = a+b
        a = b
        b = c
n = int(input("Enter a number : "))
fib(n)
