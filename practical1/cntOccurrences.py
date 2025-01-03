str = input("Enter a string : ")
char_cnt = {}
for char in str:
    char_cnt[char] = char_cnt.get(char, 0)+1
print(char_cnt)
