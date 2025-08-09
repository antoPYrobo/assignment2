number = int(input("Enter a number: "))

if number % 2 == 0:
    print(str(number) + " is an even number.\n")
else:
    print(str(number) + " is an odd number.\n")


s = 0
for i in range(51):
    s += i

print("The sum of numbers from 1 to 50 is: " + str(s))
