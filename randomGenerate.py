import random
number=random.randint(1,9)
chances=0
print('Guess a Number between 1 and 9:')
while chances<3:
    x=int(input("Enter a number between 1 and 9:"))
    if x==number:
        print("Congrats! You won")
        break
    elif x<number:
        print("You Guessed a Smaller Number! Try Again")
    else:
        print("You've Guessed a Higher Number! Try Again")
    chances+=1
if chances==3:
    print("You Lost!")