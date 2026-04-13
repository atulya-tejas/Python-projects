import random
print("\n--------Number guessing game--------")
aim = random.randint(0,100)
toFind = True
while toFind:
    num = int(input("Enter a number between 0 - 100 :"))
    if num == aim:
        print("--------Congratulations, you won!!!!!--------")
        toFind = False
    elif num > aim :
        if num - aim < 10  :
            print("Try Again! You guessed slightly high")
        else:
            print("Try Again! You guessed too high")
    elif num < aim :
        if aim - num < 10 :
            print("Try Again! You guessed slightly low")
        else:
            print("Try Again! You guessed too low")



    


    



