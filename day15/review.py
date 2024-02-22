def sol(n):
    if len(n) > 1:
        n.remove(min(n))
        return n
    else:
        return [-1]
a=sol([3,34,64])
print(a)
def sol1(s1,s2):
    word = ""
    for i,j in enumerate(s1):
        word += j
        word += s2[i]
    return word
print(sol1("aaaaa","bbbbb"))