str = input("Enter a string : ")
cnt = 0
for char in str :
    if char.isalpha() :
       cnt+=1
print(f"count of letters in {str} = {cnt}")

