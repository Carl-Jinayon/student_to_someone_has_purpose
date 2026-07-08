"""
Arithmetic operators:
// - Integer division (will output an integer)
** - Exponent
%  - Modulus
/  - Division
*  - Multiplication
+  - Addition
-  - Subtraction
Precedence of Arithmetic Operators (Highest to lowest):
**
%, //, /, *
+, - 

Assignment Operators:
+=
-=
*=
/=
//=
%=
**= 

Comparison Operators:
> - greater than
< - less than
== - equal to
<= - less than or equal to 
>= - greater than or equal to 
!= - not equal to

Logical Operators:
and 
or
not

Bitwise Operators:
AND
OR
NOT
XOR

(TO UNDERSTAND THIS OPERATORS, YOU HAVE TO UNDERSTAND FIRST COLLECTIONS)\
which are the lists, tuples, sets, and dictionaries
Membership Operators: 
in 
not in

Identity operators:
is 
is not

Bitwise Operator:
& - AND (who is the smaller?)
| - OR (like a addition)
^ - XOR (Exclusive OR) - true of the bits are different (difference like first - second)
~ - NOT (Bitwise Complement) ~x == -(x + 1)
<< - Left shift (can't understand this fully yet) - multiplying by 2 by each shift for non negative integers
>> - right shift (can't fully understand this fully yet) - dividing by 2 by each shift for non negative integers
"""

# Exercises - Arithmetic Operators:
# balance = 10000
# print("-----------------------------")
# print("    Bank Account exercise")
# print("-----------------------------")
# deposit = int(input("Enter deposit amount: "))
# balance += deposit
# print(f"Current Balance: {balance}")
# withdraw = int(input("Enter withdraw amount: "))
# balance -= withdraw
# print(f"Current Balance: {balance}")
# balance *= 2
# print(f"Double balance: {balance}")
# balance //= 3
# print(f"Balance divided to three people: {balance}")

# print("-----------------------------")
# print("     Game Score exercise")
# print("-----------------------------")
# score = 0
# score += 50
# score += 75
# score -= 20
# score *= 2
# print(f"Final score: {score}")

#Exercises Logical Operators:
# password = "python123"
# passw = input("Enter password: ")
# if passw == password:
#     print("Access Granted.")
# else:
#     print("Access Denied.")

# age = int(input("Enter age: "))
# if age > 18:
#     print("You are over 18.")
# elif age == 18:
#     print("You are exactly 18.")
# else:
#     print("You are under 18.")

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
# largest = first_number
# if first_number > second_number:
#     largest = first_number
# else:
#     largest = second_number
# print(f"Largest number: {largest}")

# Exercise for Logical Operators:
# print("Exercise: Movie Ticket")
# age = int(input("Enter age: "))
# ticket = input("Do you have a ticket? Yes/No: ")

# has_ticket = False

# if ticket == 'Yes':
#     has_ticket = True

# if age >= 13 and has_ticket:
#     print("Entry successful.")
# else:
#     print("Entry unsuccessful.")

# print("Exercise: Schrolarship Eligibility")
# grade = int(input("Enter grade: "))
# national_competition = input("Have you even won a national competition? Yes/No: ")

# has_national_competition = False
# if national_competition == 'Yes':
#     has_national_competition = True

# if grade >= 90 or has_national_competition:
#     print("Eligible for scholarship.")
# else:
#     print("Uneligible for scholarship.")

# print("Exercise: Website login")
# username = 'carl'
# password = 'carlpogi'
# user_name = input("Enter username: ")
# pass_word = input("Enter password: ")

# if username == user_name and password == pass_word:
#     print("Logged In successful.")
# else:
#     print("Logged In unsuccessful.")

#Exercise in Membership operators:
#Username check, create a list of usernames: Carl, Alice, Bob ask the username and report whether it already exists.
# names = ['Carl', 'Alice', 'Bob']
# username = input("Enter useranme: ")

# if username in names:
#     print("Username already exist.")
# else:
#     print("Username doesn't exist.")

# # Email Validator, ask the user for an email address, use membership opeators to check whether it contains '@'
# email = input("Enter your email address: ")
# if '@' in email:
#     print("Email address is valid.")
# else:
#     print("Email address is not valid.")

# # Favorite fruits, create a list of fruits, ask the user for a fruit name, tell them whether it's in the list
# fruits = ['Apple', 'Banana', 'Mango']
# fruit = input("Enter fruit name: ")

# if fruit in fruits:
#     print(f"{fruit} is in the list.")
# else:
#     print(f"{fruit} is not in the list.")

# Exercise in identity operators:
# Create two separate lists with the same values. Compare them using both == and is.
list1 = [1,2,3,4]
list2 = [1,2,3,4]
print(list1 == list2)
print(list1 is list2)
# Create one list, assign it to another variable, modify the second variable, and observe how the first changes.
one_list = [1,2,3,4,5]
second_list = one_list
print(one_list == second_list)
second_list.append(6)
x = None
print(x is None)
print(one_list)
# Use id() to inspect the identities of three variables:
# Two variables referring to the same list.
first = [1,3,4,5]
second = first
# One variable referring to a copied list.
third = first.copy()

print(id(first))
print(id(second))
print(id(third))