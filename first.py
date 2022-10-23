                                                 #Starting Python


"""               #integer and float can be assigned like this
age = 134
price = 12.32

#String can be assigned like this
first_name = "Susheel"

#boolean value can be assigned like this
is_online = True

print(age+234)

#this is how to take input and store in a same data type variable
name = input("What is your name : ")

#this is how to print two string or adding two strings
print("Hlw "+name)


                                                #type conversion

birth = input("Enter your birth year: ")
#year = 2022 - birth
#error occured because we cannot subtract integer with string
#so here we have to perform type conversion

year = 2022 - int(birth)
                     #type conversion that we can use
               #    [[ int(),float(),bool(),str() ]]

#you cannot concatenate string with integer value
#print('you are '+year +' old') || 

# But you can do it like this:-
print(str(year)+' is your age.')
"""

                                             # Exercise 1. Basic calculator program 

""""first = input("First :")
second=input('Second :')
sum=first+second
print(sum)
here the result is concatenation of string first with string second i.e.(eg first =23,second =32,sum will be 2332)
"""

"""first = input("First :")
second=input('Second :')
sum=float(first)+float(second)
print("sum is: "+ str(sum))
"""
#another way to write this code is
""""
first = float(input("First :"))
second=float(input('Second :'))
sum=first+second
print("sum is: "+ str(sum))
"""

                     #Functions
"""course='python for beginners'
       #012345  
print(course.upper())
print(course)
print(course.lower())
print(course.find('y'))#(here the output will be 1 as the index of y is 1)
print(course.replace('for','4'))
print('Python' in course)#"in" is a keyword work like as it is read in python

                            #Arithematic operators

print(23+23)
print(23-23)
print(23*23)
print(24/23)
print(24//23)
print(24%23)
print(24**2)

x=10
x=x+3
#x += 3 ( += argumented assignment operator)

x= 10 + 3*2 (PEMDAS Works in python)
print(x)
"""

                                     #comparison operator

""""x=3>2

(>,<,>=,<=,==,!=,)

print(x)"""

                                    #logical operator

"""price=12
print(price>10 or price<15)

print(not price>10)"""
 
                                    #if statement

"""temperature=5

if temperature>30:
      print("it's a hot day")
      print("drink plenty of water ")
elif temperature>20:#(20,30]
      print("Its a nice day")
elif temperature>10:#(10,20]
      print("It's a bit cold today")
else:
      print("it's cold")"""

                                    #exercise 2. Weight conversion
"""
weight =float(input("weight:"))
measure=input("k for kg or l for pound")
if measure.upper()=='L':
      weight= weight *.45
elif measure.upper=='L':
      weight=weight/.45
print("your desired output is : "+str(weight))
"""

                                  #while loops
"""i=1
while i<=10:
      print(i * "*")
      i+=1
   """
                                    #list

"""names=["susheel", "johm", "ara"]
print(names[-1])   # -1 will represent the last element in the list
names[0] ='ma'
print(names[0])
print(names[0:2])
"""
                                    #objects

"""numbers=[1,3,4,2,5,6]
numbers.append(9)
numbers.insert(0,2)
numbers.remove(4)
#numbers.clear()      clears list
print(1 in numbers)
print(10 in numbers)
print(len(numbers))
print(numbers) """

                                  #for loops

"""numbers=[1,3,4,5]
for item in numbers:
      print(item)

#same thing but for loop is easy to write 

i=0
while i<len(numbers):
      print(numbers[i])
      i+=1  """        
                                                           
                                   #range() function
     
#numbers= range(5)     
#numbers= range(5,20,2) #2 k gap pr numers print hoga default one hota hai   
#print(numbers)
"""for numbers in range(5,10,2):
      print(numbers)"""

                                    #tuples

lists=(1,3,5,6)   #paranthesis denotes tuples
#lists[0]=3   #error bcz tuples are immutable           
lists.count(3)
lists.index(5)
print(lists)


"""#************************************************************************END**************************************************************"""
