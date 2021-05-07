#Q4:
s=["empathy","empathy","kindness","kindness","compassion","humble","humble"]
s=["delhi","delhi","mumbai","mumbai","chennai","chennai","mumbai"]
g=[]
i=0
while i<len(s):
    if s[i] not in g:
        g.append(s[i])
    i+=1   
print(g)  