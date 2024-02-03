#key:values pair
#pop()
#.get()
#.popitems()
#update() 
#.items()   to get both values

# student={"name":"reshidev","age":23,"course":"python full stack"}
# print(list(student.keys()))
# print(student.get("name"))
# print(student.items())
# student["place"]="kochi"
# print(student)

# food={}
# l=["food1","food2","food3"]
# for i in l:
#     name=input("enter the food")
#     food[i]=name
# print(food)
# remove=input("which one to remove")
# print(food.pop(remove))
# print(food)

# dict1={1:"hello",2:"world",3:"hai",4:"abc"}
# n=int(input("enter"))
# a=list(dict1.items())
# print(dict(a[0:n]))

# result={"jithin":60,"fayas":70,"aswin":75,"brightlee":60}
# print(sum(result.values())/len(result))

# result={"a":60,"b":70,"c":75,"d":40,"e":90,"f":30,"g":85}
# if result.values()<50:
#     print(result.pop())       ????

# l=["a","b","c","a"]
# s={}
# for i in l:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(s)

# name="hello,world"
# a=name.split(',')
# print(a)
# b=','.join(a)
# print(b)

# a={"name":"reshi"}
# b={"age":23}
# c=list(b.items())
# print(c)
# for i,j in c:
#     a[i]=j
# print(a)
                        #same prg
# a={"name":"reshi"}
# b={"age":23}
# a.update(b)
# print(a)

# text="hello hai hello hai hello"
# d={}
# a=text.split(' ')
# print(a)
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# d={}
# m="ABCABBDE"
# for i in m:
#     if i in d:
#         d[i]+=1
#         print(i)
#         break
#     else:
#         d[i]=1

# d={}
# text="ABBCD"
# for i in text:
#      if i in d:
#         d[i]+=1
#      else:
#          d[i]=1
# print(d)
# c=list(d.items())
# for i,j in c:
#     if j==1:
#         print(i)




     










