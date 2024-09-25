#in list to find  the  evrn numbers
l=[1,9,8,7,6,4]
for i in l:
    if i%2==0:
        print(i)


# in list to find the squares of elements
l=[2,5,7,9,2]
for i in l:
    print(i*i)
    
# if-else condition
a=int(input("enter a age"))
if a>=18:
    print("eligible for vote")
else:
    print(" not eligible for vote")


#s="learning python is very easy" print only wherever we have a in a word using join function
s="learning python is very easy"
a=[]
for i in s:
    if i=='a':
        a.append(i)
print(''.join(a))
# here to use append function for adding element
# join is used to an iterable elements
    

#s="learning python is very easy" print only wherever we have a in a word without join function
s="learning python is very easy"
for i in s:
     if i=='a':
         print(i)

# if-elif-else condition
marks=int(input("enter student marks"))
if marks>=90:
    print("o grade")
elif marks>85:
    print("A grade")
elif marks>50:
    print("c grade")
else:
    print("false")


# to print squares of a number in a list
import math
l=[4,25,49,81,36]
for i in l:
    print(math.sqrt(i))

            
