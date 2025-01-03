str = input("Enter a string : ")
cntV = 0
cntC = 0
vowel = "aeiou"
str = str.lower()
for char in str :
    if char in vowel :
       cntV+=1
    else:
        cntC+=1
print(f"count of vowel = {cntV} \ncount of consonant = {cntC}")


