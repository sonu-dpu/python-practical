num = input("Enter a number : ")
rev = num[::-1]
print("Reversed : ", int(rev))
if rev == num :
    print(num+" is a palindrome nuimber")
else:
    print(num+" is not a palindrome")
