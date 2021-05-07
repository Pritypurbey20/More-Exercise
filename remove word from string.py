a="NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
s=a.split(" ")
print(s)
s.remove("higher")
print(s)
i=0
while i<len(s):
    if "higher" in s:
        s.remove("higher")
        print(s) 
    i+=1