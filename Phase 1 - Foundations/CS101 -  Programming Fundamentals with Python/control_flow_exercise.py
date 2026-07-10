"""
Exercise 1 (if/elif/else):
Write a program that asks the user for a number. 
If the number is positive, print "Positive". 
If negative, print "Negative". If zero, print "Zero".
"""
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

"""
Exercise 2 (while loop):
Write a program that keeps asking 
the user to type "yes" until they actually type "yes". 
When they do, print "Finally!".
"""
while True:
    agree = input("Type \"yes\": ")

    if agree == "yes":
        print("Finally!")
        break

"""
Exercise 3 (for loop with range):
Calculate the sum of all numbers from 1 to 100 (inclusive).
Print the total.
"""
sum = 0
for num in range(1, 101):
    sum = sum + num
print(sum)
"""
Exercise 4 (break and continue):
Write a program that prints numbers from 1 to 20. 
If the number is divisible by 3, skip it (continue). 
If the number is greater than 15, stop the loop (break).
"""
for num in range(1, 21):
    if num % 3 == 0:
        continue
    if num > 15:
        break

    print(num)