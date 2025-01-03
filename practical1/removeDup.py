str = input("Enter a string : ")
non_dup = ""
for char in str :
    if char not in non_dup:
        non_dup+=char
print(f"non duplicate string : {non_dup}")



