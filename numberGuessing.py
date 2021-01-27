import random

num = str(input("Enter any number from 1 to 10 :"))
randNum = str(random.randint(0, 10))

if num == randNum:
    print("you have won the random number is "+randNum)
elif num != randNum:
    print("Not the generated number the generated one was " + randNum)
else:
    print("Out of range")

