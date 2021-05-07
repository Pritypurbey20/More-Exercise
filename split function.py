a="NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
s=""
b=[]
for i in a:
    if i==" ":
        b.append(s)
        s=""
    else:
        s+=i
if s:
    b.append(s)
print(b)