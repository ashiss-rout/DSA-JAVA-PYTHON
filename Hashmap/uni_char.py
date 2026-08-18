#first unique char in a string 

def first_unique(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch

    return None


s = "leetcode"
print("The first unique character is:", first_unique(s))
