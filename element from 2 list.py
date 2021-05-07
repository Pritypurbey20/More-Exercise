#Q7:
a=[1,5,10,12,16,20]
b=[1,2,10,13,16]
i=0
while i<len(b):
    if b[i] not in a:
        a.append(b[i])
    i+=1
print(sorted(a))