s = 'Brasil'

for i in range(len(s)):
    temp = s[0]
    s = s.replace(s[0], "")
    s = s + temp
    print(s)
