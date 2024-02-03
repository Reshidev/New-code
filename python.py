# # # bank="sbi"
# # # user="reshi"
# # # print(user,"has a fixed in",bank)

# # # num1=10
# # # num2=50
# # # print(num1+num2)
# # # print(num2-num1)
# # # print(num1/num2)
# # # print(num1*num2)

# # # a=2
# # # b=3
# # # c=a
# # # a=b
# # # b=c
# # # print(a,b)

# # # institute="luminar"
# # # course="PY-Django fullstack"
# # # place="ekm"
# # # time=3
# # # # i am doing PY-Djnago fullstack in luminar at ekm at 3

# # # # print("i am doing",course,"in",institute,"at",place,"at",time)

# # # # name=input("enter u r name")
# # # # place=input("where r u from",)
# # # # print=input("i am",name,"from",place)

# # # #num1=int(input("enter your number"))
# # # #num2=int(input("enter the number"))
# # # #num3=int(input("enter the number"))
# # # #a=num1+num2
# # # #print("the answer is = ",a*num3)

# # # #name=input("enter u r name")
# # # #age=int(input("enter u r age"))
# # # #print("hey",name,"u r age will be",age+1,"next year")

# # # #bill=int(input("enter the total amount"))
# # # #chunks=int(input("enter the number"))
# # # #total=bill//chunks
# # # # division /
# # # #floor division //  used to remove decimal value and make it round figure
# # # #print(total)

# # # #days=int(input("number of days"))
# # # #hours=days*24
# # # #minutes=hours*60
# # # #print("In ",days,"days there are ",hours,"hours and",minutes,"minutes")

# # # #----------------------------------------------------conditional statements-------------------------------------------------------

# # # #n=int(input("enter the number"))
# # # #if n>10:
# # #  #   print("greater than 10")
# # # #else:
# # #  #   print("less than 10")

 
# # # #name=input("enter your name")
# # # #age=int(input("enter your age"))
# # # #if age>18:
# # #  #print("hey",name,"u can get the license")
# # # #else:
# # #  #print("hey",name,"u cant get he license")

# # # #n=int(input("enter the number"))
# # # #if n<10:
# # #  #   print("less than 10")
# # # #elif n==10:
# # #  #   print("equals 10")
# # # #else:
# # #  #   print("greater")

# # # #n1=int(input("enter the number"))
# # # #n2=int(input("enter the number"))
# # # #if n1>n2:
# # #  #   print(n2,n1)
# # # #elif n2>n1:
# # #  #   print(n1,n2)

# # # #n=int(input("enter the number"))
# # # #if n>=10 and n<=20:
# # #    # print("thank u")

# # # #n=int(input("enter the number"))
# # # #if n<10:
# # #  #   print("too low")
# # # #elif n<=10 and n>=20:
# # #  #   print("correct")
# # # #else:
# # #  #   print("too high")

# # # n=int(input("enter the number"))
# # # if n==1:
# # #     print("okay")
# # # elif n==2:
# # #     print("good")
# # # elif n==3:
# # #     print("well done")
# # # else:
# # #     print("bloody sweet")

# # color=input("enter u r color")
# # if color=="red" or color=="RED" or color=="Red":
# #     print("i like red too")
# # else:
# #     print("i prefer only red")
      
    
#         #modulo
# #n=int(input("enter the number"))
# #if n%2==0:
#     #print("even")
# #elif n%2!=0:
#  #   print("odd")
# #else:
#  #   print("out")


# #n=int(input("enter the number"))
# #if n%3==0 and n%5==0:
#   #  print("divible by both 3and 5")
# #elif n%3==0:
#  #   print("divisible by 3")
# #elif n%5==0:
#   #  print("divisible by 5")

# #nested if
# #n=input("is it rainy")
# #if n=="yes":
#     #m=input("is it windy")
#     #if m=="yes":
#      #   p=input("is it too windy")
#       #  if p=="yes":
#        #        print("take care")
#         #else:
#          #    print("okey")               
#     #else:
#      #    print("enjoy")
# #else:
#  #    print("wwoww")


# n=int(input("enter the number"))
# if n>=0 and n<=100:
#     if n>=90 and n<=100:
#         print("A")
#     elif n>=80 and n<90:
#         print("B")
#     elif n>=70 and n<80:
#         print("C")
#     elif n>=60 and n<70:
#         print ("D")
#     elif n<60:
#         print("failed")
# else:
#     print("invalid number")
          
               
#######################################string#########################



#ask user to enter firstname.if len of name under 5 ask them to enter theri second name and join them and display
#in upper case if len of firstname morethan or equal to 5 show thwn in lowercase

# m=input("enter the firstname")
# if len(m)<=5:
#     n=input("enter the second name")
#     print((m+n).upper())
# elif len(m)>5:
#     print(m.lower())
# else:
#     print("get out")

#square
#triangle

# print("square")
# print("triangle")
# n=int(input("enter your choice"))
# if n==1:
#     k=int(input("enter the area of square"))
#     print("area of square is",k*k)
# elif n==2:
#     h=int(input("enter the height of triangle"))
#     b=int(input("enter the base of triangle"))
#     print("area of triangle is",(b*h)/2)

#*************************************looping*******************************************


# for i in range(1,3):
#     print(i)
#     print("reshidev")


# for n in range(3,7):
#     if n%2==0:
#         print(n,"even")
#     else:
#         print(n,"odd")


# m=input("enter the name")
# n=int(input("enter the number"))
# for i in range(n):
#     print(m)


#ask user to enter the name and number if number lessthan 10 then print the same upto that number
#if the number is greater than 10 print too high, upto three times

# m=input("enter the name")
# n=int(input("enter the number"))
# if n<10:
#     for i in range(n):
#         print(m)
# elif n>=10:
#     for i in range(3):
#         print("too high")

# n=int(input("how many people u want to invite"))
# if n<10:
#     for i in range(n):
#          m=input("enter the name")
#          print(m,"has been invited")
# elif n>=10:
#      print("too many people")


# n=1
# while n<10:
#     print("hello")

# n=0
# while n<50:
#     num=int(input("enter the number"))
#     n=n+num
#     print(n)

# n=0
# for i in range(1,50):
#     if n<50:
#         n=int(input("enter the value"))
# print(n)
    
        
    

# n=0
# m=int(input("enter the value"))
# while m!=0:
#     total=m+n
#     print(total)


# n=int(input("enter the number"))
# if n<5:
#     for i in range(1,11):
#         total=n*i
#         print(total)
    


# weight=int(input("enter the weight"))
# height=int(input("enter the height"))
# bmi=(weight/height**2)
# print(bmi)
# if bmi<19:
#     print("below normal")
# elif bmi>=19 and bmi<25:
#     print("normal")
# elif bmi>=25 and bmi<30:
#     print("over weight")

# n  integer
# n positive- print even numbers from 2 ton n
# n zero-print n is zero
# n n negative-print n is negative

# n=int(input("enter the number"))
# if n>0:
#     for i in range(2,n+1,2):
#         print(i)
# elif n==0:
#     print("number is zero")
# elif n>0:
#     print("number is negative")



# a=int(input("enter first number"))
# b=int(input("enter the second number"))
# c=int(input("enter the third number"))
# if a>b and a>c:
#     print(a,"a is greater")
# elif b>a and b>c:
#     print(b,"is greater")
# else:
#     print(c,"is greater")

# n=1
# m=int(input("enter the number"))
# while(n<=m):
#     print(n)
#     n+=1


# n=1
# m=int(input("enter the number"))
# while(n<=m):
#     if n%2==0:
#         print(n)
#     n+=1

#to find leap year or not
# year=int(input("enter the year"))
# if year%4==0 and year%100==0 and year%400==0:
#     print("its leap year")
# else:
#     print("its not leap year")

# n=int(input("enter the starting year"))
# m=int(input("enter the current year"))
# for i in range(n,n+1):


# a=int(input("countup or countdown"))
# if a=="U":
#     b=int(input("enter the number"))
#     for i in range(1,b+1):
#         print(i)
# elif a=="d":
#     c=int(input("enter a nuber less than 20 : "))
#     for i in range(20,c-1,-1):
#         print(i)

# else:
#     print("get out")


# n=int(input("enter the number between 10 and 20"))
# while n<10 or n>20:
#     if n<10:
#         print("too low please try again")
#     elif n>20:
#         print("too high please try again")
#     n=int(input("try again"))
# print("thanku")

# total=0
# for i in range(5):
#     num=int(input("enter the number"))
#     m=(input("do u want to add this number"))
#     if m=='y':
#         total=total+num
#     elif m=='n':
#         print("leave it")
# print(total) 


# n=int(input("how many people"))
# if n<10:
#     for i in range(n):
#         name=(input("enter the name"))
#         print("welcome",name)
# else:
#     print("too many peoples")

#-------break statement-------

# for i in range(1, 10):
#     print(i)
#     if i==5:
#         break

#-------continue statement-----------

# for i in range(1, 10):
#     if i==5:
#          continue
#     print(i)
   
    




    
    


    




    




    
