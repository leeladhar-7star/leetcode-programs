def firstuniqchar(s):
    d={}
    for i in range(len(s)):
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1
    for key,value in d.items():
        if value==1:
            return s.index(key)
    return-1
s=input("enter a string: ")
print(firstuniqchar(s))