# import random
# num=random.randint(1,9)
# print(num)

# import random
# num=random.randint(1,9)
# for i in range(3):
#     n=int(input("enter the number"))
#     if n==num:
#         print("correct")
#         break
#     else:
#         print("try again")
# print ("thank you")

#using random
#num=(0,21)
#num=odd-print (odd from1,num)
#num=even-print(multiplication table 1 to 12)
#num=0-print (sum of number from 1 to 10)

# import random
# num=random.randint(0,21)
# if num%2!=0:
#     for i in range(1,num,2):
#         print(i)
# elif num==0:
#     sum=0
#     for i in range(1,10):
#         sum=sum+1
#         print(sum)
# elif num%2==0:
#     for i in range(1,10):
#         print(num,"=",num*i)

# import random
# score=0
# for i in range(5):
#     num1=random.randint(1,50)
#     num2=random.randint(1,50)
#     n=num1+num2
#     print(num1,"+",num2,"=")
#     result=int(input("enter the answer"))
#     if result==n:
#         score+=1
#         print("correct")
#     else:
#         print("wrong,try next one")
# print("your score is",score)   

# import random
# num=random.randint(1,5)
# ask=int(input("guess the number"))
# if num==ask:
#     print("welldone")
# elif num<ask:
#     print("too high")
#     secondchance=int(input("guess once more"))
# elif num>ask:
#     print("too low")
#     secondchance=int(input("guess once more"))
#     if secondchance==num:
#         print("well done")
#     else:
#         print("you lose") 
# print(num)

# import random
# count=0
# balance=random.randint(100,6000)
# password=random.randint(1000,9999)
# print(balance)
# print(password)
# choice=int(input("1.withdrawal\n2.Balance\n3.exit\n"))
# if choice==1:
#     for i in range(3):
#         pin=int(input("enter the PIN: "))
#         if pin==password:
#             amount=int(input("enter the amount"))
#             if amount<=balance:
#                 print(amount,"is debitted from your acoount")
#             else:
#                 print("insuffcient balance")
#             break
#         else:
#             print("wrong password")
#     print("your account has blocked")        
# elif choice==2:
#     print("the account balance is: ",balance)
# elif choice==3:
#     print("exit")



    








