def main():
    print("Enter how big your grid will be")
    entry=int(input())
    print_it(entry)
    print("Nice Grid!")

def print_it(x):
    for h in range(x):
        print_row(x)

def print_row(y):
    for i in range(y):
        print("#", end="")
    print()

main()