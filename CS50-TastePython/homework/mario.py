def main():
    count=int(input("How many levels do you want in your pyramid?"))
    print("OK, here you go:")
    print_pyramid(count)
    print("Luigi is Super, too, you know.")

def print_pyramid(x):
    for i in range(x):
        i+=1
        for j in range(i):
            print("#", end="")
        print()

main() 