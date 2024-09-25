# using if elif and else condition
a=int(input("eneter  age"))
if a<=5:
    print("small babay")
elif a<=10:
    print("is a child")
elif a>=18:
    print(" eligible for vote")
else:
    print("enter correct age ")


#transfer statement
# in python break statement is used to stop the current iteration
for i in range(1,20):
    if i==3:
        break
    print(i)
print("_____________")
# continue
# in python continue is used to skip the current iteration 
for i in  range(1,10):
    if i==5:
        continue
    print(i)


# Guess by number using while loop and if:
guess_number=int(input("enter a guess number"))
guesses=-1
while guesses !=guess_number:
    guesses=int(input("guess the number"))
    if guesses<guess_number:
        print("too low! try again")
    elif guesses>guess_number:
        print("too high! try again")
    else:
        print("congratulations you guessed the number")
        

# Guess by number using for loop and if:
number=int(input("enter a number"))
attempts=int(input("enter number of attempts"))  
for i in range(1,attempts+1):
    guess_number=int(input("enter a guess number"))
    if guess_number<number:
        print("two low")
    elif guess_number>number:
        print("two high")
    else:
        print("congratulations you guessed the number")
else:
    print("sorry number of attempts are completed")