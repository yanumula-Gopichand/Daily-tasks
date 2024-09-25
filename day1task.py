# whats is integer 
# A number without decimal is called a integer
a=10
b=7
c=a+b
print("this is integer",c)
# what is float
#  A number with a decimal is called float
a=8
b=9.0
c=a+b
print("this is float",c)
#what is complex
# A number has imagine and real number is called complex number
a=7+8j
print( "this is complex",a)
# whats is list
# list means collection of elements and list is mutable means we can do the operations
a=[1,2,3,4]
print(type(a))
#  positive index of list
a=[1,3,5,8]
print("index position of list",a[1])
# negitive index of list
a=[0,6,90,67,"gopi"]
print("negitive index",a[-1])
# silicing 
a=["gopi","raja",1,2,3,0.8]
print(" positive silicing",a[2:5])
print(" negitive silicing",a[-1:])
# change items in list
a=[1,"gopi",5,7,"madhu"]
a[1]="amma"
print(a)
# add element particular index position
a=[1,4,7,"gopi","amma"]
a.insert(1, "orange")
print(a)
# add the element in list
a=[2,5,9,"gopi"]
a.append(8)
print(a)
# remove element
a = ["apple", "banana", "cherry", "banana", "kiwi"]
a.remove("banana")
print(a)
# delete element
a = ["apple", "banana", "cherry"]
a.pop(1)
print(a)
# Tuple
# index 
a = ("apple", "banana", "cherry")
print(a[-1])
# silicing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# convert tuple to list
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# set
a = {"apple", "banana", "cherry"}
print(type(a))
# add item in set
a = {"apple", "banana", "cherry"}
b = ["kiwi", "orange"]

a.update(b)

print(a)
# remove element in set
a = {"apple", "banana", "cherry"}

a.remove("banana")

print(a)
# dict
# add value
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a["year"] = 2018
print(a)
#remove element
a = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del a["model"]
print(a)
# string single line
a = "Hello"
print("single line",a)
# multipuline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("multipleline string",a)
# silicing string
b = "Hello, World!"
print("silicing",b[2:])
#the strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
# concentate 
a = "Hello"
b = "World"
c = a + b
print(c)