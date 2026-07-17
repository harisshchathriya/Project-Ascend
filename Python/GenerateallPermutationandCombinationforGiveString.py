def permute(s, i):
    if i == len(s):
        print(''.join(s))
        return
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        permute(s, i + 1)
        s[i], s[j] = s[j], s[i]
