import random


def main():

    #Count down to the new year from random number
    number = random.randint(5, 15)
    countdown(number)
    print("Happy New Year!")

def countdown(n):
    for i in range(n):
        print(n - i)

main()