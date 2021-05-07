
# harshad number in function:
# def h(n):
#     i=1
#     b=n
#     sum=0
#     while i<=n:
#         sum=sum+n%10
#         n=n//10
#     if b%sum==0:
#         print(b,"is a harshad number.")
#     else:
#         print(b,"is not a harshad number.")
#     i+=1
# h(18)

#harshad number from 1 to 1000 in function:
# def h(n):
#     i=1
#     while i<=n:
#         a=i%10
#         b=(i//10)%10
#         c=(i//10)//10
#         d=a+b+c
#         if i%d==0:
#             print(i,"is a harshad number")
#         else:
#             print(i,"is not a harshad number") 
#         i+=1       
#h(1000)        



# m=[[45,21,42,63],[12,42,42,53],[42,90,78,13],[94,89,78,76],[87,55,98,99]]
# i=0
# o=[]
# while i<len(m):
#     j=0
#     n=0
#     s=len(m[i])
#     while j<s:
#         t=m[i][j]
#         if n<t:
#             n=t
#         j+=1
#     i+=1
#     o.append(n)
# print(o)

#fabonacci series in list:
# n=int(input("Enter a number:"))
# a=0
# b=1
# c=1
# sum=0
# k=[]
# while c<=n:
#     c+=1
#     a=b
#     b=sum
#     sum=a+b
#     k.append(sum)
# i=0
# while i<len(k):
#     print(k[i])
#     i+=1
# print(k)

#strong password:
# n=input("Enter your password:")
# if (len(n)>=6 or len(n)<=16) and ("#" or "$" or "@" or "&" in n) and ("2" or "8" in n) and ("A" or "Z" in n):
#     print(n,"is a strong password")
# else:
#     print(n,"is not a strong password")


#debugging:
#  Q1:
# def n(list):
#     i=0
#     h=[]
#     k=[]
#     while i<len(list):
#         item=list[i]
#         if item>20:
#             h.append(item)
#         else:
#             k.append(item)
#         i+=1
#     print("Initial list",list)
#     print("list that doesn't contain numbers greater than 20",k)
#     print("greater than 20",h)     
# n([12,312,42,123,5,12,53,75,123,62,9]

# def x(a,b):
#     i=0
#     c=0
#     d=0
#     e=0
#     while i<len(a):
#         if a[i]>b[i]:
#             c+=1
#         elif a[i]<b[i]:
#             d+=1
#         elif a[i]==b[j]:
#             e+=1
#         i+=1
#         print(c)
#         print()
# x([2,3,4],[6,8,9])   





