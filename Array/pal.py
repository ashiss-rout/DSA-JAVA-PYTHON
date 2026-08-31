s = "madam"

for i in range(len(s) // 2):
    j = len(s) - 1 - i

    if s[i] != s[j]:
        print("not palindrome")
        break
else:
    print("palindrome")
