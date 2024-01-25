def isAnagram(s, t):
    s = list(s)
    t = list(t)
    return ''.join(s.sort()) == ''.join(t.sort())
s = "rat"
t = "cat"
print(isAnagram(s, t))
