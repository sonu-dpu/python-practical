def isPrime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1, 1):
        if n%i==0:
            return False
    return True

n = int(input("Enter a number:"))
for num in range(1, n+1):
    if isPrime(num):
        print(num, end=" ")

