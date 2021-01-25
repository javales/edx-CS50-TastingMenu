i = 0
sum = 0

while i < 10:
    sum=sum+(int(input("Let's add ten numbers:")))
    i=i+1

print("The sum is ", sum)

sum = 0;

print("How many numbers to add?: ")
number=int(input("Your number:"))

for i in range(number):
    sum=sum+(int(input("Let's add those numbers:")))
    i=i+1

print("The sum is ", sum)