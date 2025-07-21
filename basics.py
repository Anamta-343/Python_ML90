                                  # LOOPS
# a = int(input())
# b = int(input())
# for i in range(a,a*b+1):
#     if i%3==0 and i%5==0

# temp=0
# for i in range(10,56):
#     if i%3!=0 and i%5!=0:
#         temp+=i
# print(temp)

# n=int(input())
# ef=of=1
# for i in range(1,n+1):
#     if i%n==0:
#         if i%2==0:
#             ef*=i
#         else:
#             of*=i
# print(ef)
# print(of)


                                           #LIST
# a=[]
# print(a)
# lst_in=[1,5,8,4]
# print(lst_in)
#list=[1,3,5,2,7,9,12,88,50,11]   
#print(list[::-])

                        #methods
#extend
# list1=[2,3,[4,5,6],9]
# list2=[5,7,4,9]
# list2.extend(list1)
# print(list2)
# print(list1)

# list=[2,3,4,5,6,7,8,9]
# for i in range(len(list)):
#     print(list[i])

#wap which will print count of all the even and odd numbers in a given list
# list=[2,8,45,99,34,76,55]
# even=0
# odd=0
# for i in range(len(list)):
#     if list[i]%2==0:
#         even+=1
#     else:
#         odd+=1
#  print("ODD=",odd)
# print("EVEN=",even)
    
# list=[2,8,45,99,34,76,55]
# for i in range(len(list)):
#     if list[i]%2==0:
#         list[i]="even"
#     else:
#         list[i]=5
# print(list)
   
                                        #  TUPLES

# tp1=()
# tp2=tuple()
# tp3=(1,2,4,55,"Hello")
# print(tp1,tp2,tp3)
# tp4=(5,)           # paranthesis not important
# print(type(tp4))
# tpl=(1,2,3,4,5,6,7,6,7,5,3)
# print(tpl.index(4))
# print(tpl.count(6))
# tpl=(2,3,4,5)        
# tpl+=(7,8)
# print(tpl)                      #this tuple is created at a diff address and is a new tuple
      
# REMOVE ALL THE ODD ELEMENTS
# tup=(1,56,7,45,98,34,54,45)
# lst=[i for i in tup if i%2==0]
# tup=tuple(lst)
# print(tup)

                                             # STRING
# x="let's learn python"
# print(x[: :-3])
# print(x[7: :4])
# print(x[10:])
# print(x[: :3])
# print(x[-3:-10 :-5])
# print(x[-2: :])
                           # METHODS
# x="Hello Everyone"
# x.upper()
# x.lower()
# x.capitalize()
# lst=x.split()
# x=list(str)
# x="apple orange apple guava apple banana"
# y=x.replace("apple","kivi")
# print(x)
# print(y)

# wap which will take a string as a input from user and print longest word and their length
# x="hello everyone let's run python"
# x=x.split()
# temp=""
# for i in x:
#     if len(i)>len(temp):
#         temp=i
# print(temp,len(temp))       

# x="hello,everyone.how,are,you"
# y=x.replace(",","#")
# z=y.replace(".",",")
# r=z.replace("#",".")
# print(x)
# print(r)

# CHECK FOR A PALINDROME STRING
# x="madam"
# x=list(x)
# l1=list.copy(x)
# l1.reverse()
# if(x==l1):
#     print("I am Palindrome")
# else:
#     print("Not a Palindrome")

                        #  SETS
# st={1,3,4,12,3441}
#st.add((5,5,6))
# st.update([1,2,3,4,5])
#st.remove(4)
#st.discard(11)
#st.clear()
# del st
# print(st)

# x="today is wednesday. the weather is rainy"
# x=x.split()
# st=set(x)
# print(len(st))

# x="Hello How are you,How are they"
# lst=x.split()
# list=[]
# for i in list:
#     if i not in list:
#         list.append(i)
# x=" ".join(list)
# print(x)

# s1={1,2,3,4,5,6}
# s2={2,3,5,6,8,3,4}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1-s2)
# print(s2-s1)
# print(s1^s2)

                                                 # FROZEN SET                     (immutable set)
# s={1,2,3,4,5,6}
# s1=frozenset([1,2,3,4,5,6])
# print(s1)

                                                  # DICTIONARIES
# my_dict={}
# print(my_dict)
# my_dict1={1:"abc",2:"xyz"}
# print(my_dict1)
# d1=dict(({'hii',23},{'b',26}))                     #list of set
# d2=dict((['hii',23],['b',26]))                     #tuple of list
# d3=dict((('hii',23),('b',26)))                     #tuple of tuple
# d4=dict(({'hii',23},{'b',26}))                     #tuple of set
# d5=dict(({'hii',23},{'b',26}))
# d6=dict(({'hii',23},{'b',26}))
# d7=dict({(('hii',23),('b',26))})
# print(d1)
# print(d2)
# print(d3)
# print(d4)
# print(d5)
# print(d6)
# print(d7)

# HOW TO ACCESS
# my_dict={'name':'satish','age':27,'address':'guntur'}
# print(my_dict['age'])
# print(my_dict['degree'])
# print(my_dict.get('degree'))
# print(my_dict.get('name'))

# my_dict['name']="Anamta"
# my_dict['degree']="BTECH"
# print(my_dict)

                           #delete  in  dictionaries
# print(my_dict.pop('name'))
#print(my_dict.popitem())
# del my_dict
# my_dict.clear()
# print(my_dict)

                         #methods
# x=[3,4,5,6,7]
# y=x.copy()
# x[3]=15
# x[3]=14
# print(x)
# print(y)

# subjects={2:4,3:9,5:25}
# print(subjects.key())
# print(subjects.values())
# print(subjects.items())

# x={2:4,3:9,4:16}
# for k,v in x.items():
#     if v%2==0:
#         x[k]+=5
#     else:
#         x[k]-=5
# print(x)

# x={3:[5,3,76,44,23,0],4:[67,45,33,2,5,34],5:[56,33,45,659,345,5,13]}
# for k,v in x.items():
#     count=0
#     for i in v:
#         if i%2!=0:
#             count+=1
#         x[k]=count
# print(x)        

                              #   ITERATION IN DICTIONARY
# subjects={2:[4,2,3,4,56],3:[9,1,2,3,4],4:[16,2,3]}
# for k,v in subjects.items():
#     subjects[k]=[i+1 for i in v]
# print(subjects)
    
                     # COMPREHENSION
# d={'a':2,'b':1,'c':4,'d':5}
# new_dict={k:v for k,v in d.items() if v>2}
# print(new_dict)

# d={'a':2,'b':1,'c':4,'d':5}
# new_dict={k:v for k,v in d.items() if v>2}
# print(new_dict)



