import random

randomnum=random.randint(1,10)

print("You have three chances to guess my secret number!")

number = 0

while number < 3:
    print("Guess my number between 1 and 10")
    guess=int(input())
    if guess == randomnum:
        print("You guessed it!")
        number=3
    else:
        print("Try, again...")
        number+=1
print("Thanks for playing... The number was actually ", randomnum)