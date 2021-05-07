n=int(input("Enter a number:"))
j=1
while j<=n:
    a=int(input("Enter a number:"))
    i=0
    sum=0
    while i<a:
        sum=sum+a%10
        a=a//10
    print(sum)
    j+=1