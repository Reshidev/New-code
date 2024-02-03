# n=input("enter the name")
# if len(n)<5:
#     m=input("enter the second name")
#     print((n+m).upper())
# elif len(n)<=5:
#     print(n.lower())

# n=int(input("enter the choice"))
# if n==1:
#     k=int(input("enter the side of the square "))
#     print("area of the square is",k*k)
# elif n==2:
#     base=int(input("enter the base of the triangle"))
#     height=int(input("enter the height of the triangle"))
#     print("area of the trianagle is ",(base*height)/2)


# n=int(input("enter the number"))
# if n<10:
#     print("too low")
# elif n>10 and n<20:
#     print("correct")
# elif n>20:
#     print("too high")
# print("thank you!")

# weight=int(input("enter the weight"))
# height=int(input("enter the height"))
# bmi=weight/height**2
# print(bmi)
# if bmi<19:
#     print("below normal")
# elif bmi>=19 and bmi<25:
#     print("normal")
# elif bmi>=25 and bmi<30:
#     print("over weight")
# else:
#     print("u r dead")

# n=int(input("enter the number"))
# if n<1:
#     print("get out")
# elif n%2==0:
#     sum=0
#     for i in range(2,n+1,2):
#        sum=sum+i
#     print(sum)
# else:
#     sum=0
#     for i in range(1,n+1,2):
#         sum=sum+i
#     print (sum)

#38     
# 


#40
# n=int(input("enter the number below 50"))
# print(n)
# for i in range(50,n-1,-1):
#     print(i)

#42
# total=0
# for i in range(5):
#     n=int(input("enter the number"))
#     m=input("u want to add the number Y/N")
#     if m=="Y":
#         total=total+n
#     else:
#         print("leave it")
# print(total)

# n=50
# m=int(input("guess the number"))
# count=1
# while m!=n:
   
#     if m<n:
#         print("too low")
#     elif m>n:
#         print("too high")
#     m=int(input("guess the number"))
#     count=count+1
# print(count)
# print("u r crct")


# count=0
# n=(input("do u want to invite the somebody Y/N"))
# while n=="y":
#     m=input("enter the name")
#     print(m,"is invited")
#     n=(input("do u want to invite the somebody Y/N"))
#     print("thank u")
#     count=count+1
# print(count)

#51
# n=int(input("enter a number of green bottles : "))
# print("\n\nthere are",n,"green bottle hanging on the wall\n",n,"green bottle hanging on the wall\n and if one green bottle should accidently fall\n")
# num=n-1
# if num==0:
#     print("there are no more green bottle hanging on the wall")

# else:
#     choice=int(input("howmany green bottles will be hanging on the wall ?  :    =  "))

#     while choice!=num:
#         print("no try again")
#         choice=int(input("howmany green bottles will be hanging on the wall ?  :    =  "))
    
#     print("\nYes there will be",num,"green bottle hanging on the wall")

#51
# num=10
# while num>0:
#     print(num,"green bottles are hanging")
#     print("what if one bottle falls")
#     num=num-1
#     m=int(input("how many it will be"))
#     if m==num:
#         print("there will be",num,"bottle are hanging")
#     else:
#         print("try again")
#         m=int(input("how many"))
# print("thank you!")


# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]



