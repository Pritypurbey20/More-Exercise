#Q9:
harshad number:
n=int(input("Enter a number:")) 
i=0
b=n
sum=0
while i<=n:
    sum=sum+n%10
    n=n//10
    i+=1
print("sum is",sum)
if b%sum==0:
    print(b,"is harshad number.")
else:
    print(b,"is not harshad number")