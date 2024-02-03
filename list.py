# names=["reshi","roshan","jithin"]
# names.append("dev")
# print(names)
# names.pop()
# print(names)
# names.remove("jithin")
# print(names)
# names.clear()
# print(names)

# names=["reshi","roshan","jithin"]
# names.insert(2,"dev")
# print(names)

# names=["reshi","roshan","jithin"]
# names.extend([1,2,3])
# print(names)

# numbers=[100,200,300]
# for i in numbers:
#     print(i)
# ask=int(input("enter a three digit number"))
# if ask in numbers:
#     print(numbers.index(ask)                             del=to remove by giving index value

# expenses=[1000,2500,3500,12500,9876,6543]
# print(max(expenses))
# print(min(expenses))
# expenses.extend([1234,456,6542])
# print(expenses)
# expenses.insert(3,38767)
# print(expenses)
# expenses.remove(38767)
# print(expenses)

# new=[]
# for i in expenses:
#     if i>=3000 and i<=10000:
#         print(i)
#         new.append(i)
# print(new)

# expenses=[1000,2500,3500,12500,9876,6543]
# for i in expenses:
#     if i<=3000 and i>=10000:
#         expenses.remove(i)
# print(expenses)

# numbers=[2,3,4,5,7,8,9,10,12,11]
# odd=[]
# even=[]
# for i in numbers:
#     if i%2==0:
#        even.append(i)
#     else:
#         odd.append(i)
# print("even number",even)
# print("odd number",odd)

# numbers=[-2,3,-14,5,-7,8,-9,10,-12,11]
# countne=0
# countpo=0
# for i in numbers:
#     if i<0:
#         countne+=1
#     else:
#         if i>0:
#             countpo+=1
# print("negative numbers",countne)
# print("positive number",countpo)

# name=[]
# name.append(input("ente the name"))
# print(name)

# name=[]
# for i in range(3):
    
#     name.append(input("ente the name"))
# print(name)

# x=[2,3,4,5,6,7,-1]
# n=int(input("enter the number"))
# if n in x:
#     print("yes")
# else:
#     print("no")

# invite=[]
# for i in range(3):
#     invite.append(input("enter the name: "))
# new=input("u want to add another")
# while new=="yes":
#     invite.append(input("enter the name: "))
# if new=="no":
#     print(len(invite))
#     print(invite)
# ask=input("type any one of the names of the list")
# print(invite.index(ask))
# ask2=input("u want to add another")
# if ask2=="y":
#     print(invite)
# elif ask2=="no":
#     invite.remove(ask)
#     print(invite)


# number=[6,3,5,8,10]
# largest=number[0]
# for i in number:
#     if i>largest:
#         largest=i
# print(largest)

# letters=["a","b","c","a","b","b","c","a"]
# counta=0
# countb=0
# countc=0
# for i in letters:
#     if i=="a":
#         counta+=1
#     elif i=="b":
#         countb+=1
#     elif i=="c":
#         countc+=1
# print("count of a: ",counta)
# print("count of b: ",countb)
# print("count of c: ",countc)

# number=[1,2,3,4,5,6,6,7]
# ask=int(input("enter the number"))
# for i in number:
#     if i==ask:
#         print(ask,"in the list")
#         break
# else:
#     print(ask,"not in list")

# nums=[]
# for num in range(3):
#     num=int(input("enter the number"))
#     nums.append(num)
# ask=input("still want the last number Y/N")
# if ask=="Y":
#     print(nums)
# elif ask=="N":
#     nums.pop()
#     print(nums)


# n=[5,10,3,5,1,8,2]
# ask=int(input("enter the number"))
# for i in range(ask):
#     c=n.pop()
#     n.insert(0,c)
# print(n)

# name=["a","b","c","d","e","b","a","f"]
# list=[]
# for i in name:
#     if i not in list:
#         list.append(i)
# print(list)

# age=int(input("enter the number"))
# age1=100-age
# month=age1*12
# week=month*4
# days=week*7
# hours=days*24
# minutes=hours*60
# second=minutes*60
# print(month)
# print(week)
# print(days)
# print(hours)
# print(minutes)

# password=input("enter the number")
# if len(password)>7 and len(password)<15:
#     if "1" or "2" in password:
#         if "@" or "#" in password:
#             print("successful")
#         else:
#             print("no chars,unsuccessful")
#     else:
#         print("no digits")
# else:
#     print("not specified")








#-------------------------------------------------tuple--------------------------
#immutable
# name=("akhil","hari","ramu","abhin")
# print(len(name))
# v=(input("enter the name"))
# if v in name:
#     print(name.index(v))
#     print(name.count("hari"))
# else:
#     print("get out")

#---------------------------------set-----------------------
#there is no index value
#mutable
#add is use to add the element
#.issubset 
#.issuperset
#.intersection
#.union
#it will not duplicate values
# k={"akhil","hari","ramu","abhin","fayas"}
# m={"hari","ramu","fayas"}
# print(m.issubset(k))
# print(k.issuperset(m))
# print(m.intersection(k))
# print(m.union(k))


    
    

    




