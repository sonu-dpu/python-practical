def sum_of_digit(n):
    if n<=0:
        return 0
    else:
        return n%10 + sum_of_digit(n//10)
n = int(input("Enter a number : "))
print(f"Sum of digit {n} = {sum_of_digit(n)}")

