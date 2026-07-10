#!/usr/bin/env python3
"""
================================================================================
HANDOUT #5: CONTROL FLOW (Step 5)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. if / elif / else (Decision Making)
    2. while loops (Repeat while True)
    3. for loops with range() (Repeat fixed times)
    4. break (Exit loop)
    5. continue (Skip iteration)
    6. pass (Placeholder)

Prerequisites used: int, float, str, bool, print(), input(), operators.
No functions (except print/input), no lists, no dictionaries.
================================================================================
"""

print("\n" + "="*70)
print("STEP 5: CONTROL FLOW")
print("="*70)

# =============================================================================
# PART 1: if / elif / else
# =============================================================================

print("\n" + "-"*50)
print("PART 1: if / elif / else")
print("-"*50)

# Example 1: Basic if
print("\n--- Basic if ---")
age = 20
if age >= 18:
    print("You are an adult.")

# Example 2: if / else
print("\n--- if / else ---")
temperature = 30
if temperature > 25:
    print("It's hot outside.")
else:
    print("It's cool outside.")

# Example 3: if / elif / else (Grade System)
print("\n--- if / elif / else (Grades) ---")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# Example 4: Nested if
print("\n--- Nested if (Member Discount) ---")
is_member = True
purchase_total = 250
if is_member:
    if purchase_total > 200:
        discount = 0.20
    else:
        discount = 0.10
else:
    discount = 0.00
print(f"Discount: {discount * 100}%")


# =============================================================================
# PART 2: while Loop
# =============================================================================

print("\n" + "-"*50)
print("PART 2: while Loop")
print("-"*50)

# Example 1: Basic while
print("\n--- Basic while (count to 5) ---")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count = count + 1  # CRITICAL: Without this, infinite loop!
print("Loop finished.\n")

# Example 2: Input validation with while
print("--- Input validation (password) ---")
print("(Uncomment the code below to test with user input)")
# password = ""
# while password != "secret":
#     password = input("Enter the password: ")
#     if password != "secret":
#         print("Wrong, try again.")
# print("Access granted!")


# =============================================================================
# PART 3: for Loop and range()
# =============================================================================

print("\n" + "-"*50)
print("PART 3: for Loop and range()")
print("-"*50)

# Example 1: range(stop)
print("\n--- range(5) -> 0 to 4 ---")
for i in range(5):
    print(i, end=" ")  # end=" " prints on the same line
print()  # New line

# Example 2: range(start, stop)
print("\n--- range(2, 8) -> 2 to 7 ---")
for i in range(2, 8):
    print(i, end=" ")
print()

# Example 3: range(start, stop, step)
print("\n--- range(0, 10, 2) -> 0,2,4,6,8 ---")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Example 4: Iterating over a string
print("\n--- Iterating over 'hello' ---")
word = "hello"
for letter in word:
    print(letter)


# =============================================================================
# PART 4: break and continue
# =============================================================================

print("\n" + "-"*50)
print("PART 4: break and continue")
print("-"*50)

# Example 1: break
print("\n--- break: Find first even number from 1 to 10 ---")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"First even number is: {num}")
        break  # Stops the loop immediately

# Example 2: continue
print("\n--- continue: Print only odd numbers (1 to 10) ---")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip the rest of this iteration
    print(num, end=" ")
print()


# =============================================================================
# PART 5: pass - Placeholder
# =============================================================================

print("\n" + "-"*50)
print("PART 5: pass - Placeholder")
print("-"*50)

print("\n--- pass as placeholder ---")
user_logged_in = False
if user_logged_in:
    pass  # TODO: Add dashboard logic later
else:
    print("Please log in.")

# pass is also useful in loops when you need a loop that does nothing yet.
for i in range(5):
    pass  # Planning to fill this later


# =============================================================================
# COMMON MISTAKES (Demonstrated)
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("\n❌ Mistake 1: Forgetting the colon")
print("   # if age > 18   # SyntaxError: missing ':'")
print("   #     print('Adult')")

print("\n❌ Mistake 2: Wrong indentation")
print("   # if age > 18:")
print("   # print('Adult')  # IndentationError")

print("\n❌ Mistake 3: Infinite loop (commented out to prevent crash)")
print("   # count = 0")
print("   # while count < 5:")
print("   #     print('Infinite!')  # Forgot count = count + 1")

print("\n❌ Mistake 4: Using = instead of ==")
print("   # x = 5")
print("   # if x = 5:   # SyntaxError! Use == to compare.")
print("   #     print('x is 5')")


# =============================================================================
# CORE EXERCISES (To be done in a separate file)
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES (Step 5 Mastery Check)")
print("="*70)

print("""
EXERCISE 1 (if/elif/else):
Write a program that asks the user for a number.
If the number is positive, print "Positive".
If negative, print "Negative".
If zero, print "Zero".

EXERCISE 2 (while):
Write a program that keeps asking the user to type "yes"
until they actually type "yes".
Print "Finally!" when they do.

EXERCISE 3 (for/range):
Calculate the sum of all numbers from 1 to 100.
Print the total.

EXERCISE 4 (break/continue):
Write a program that prints numbers from 1 to 20.
If the number is divisible by 3, skip it (continue).
If the number is greater than 15, stop the loop (break).
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (Optional - For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
The following concepts are EXTRA. They are NOT required for Step 5 mastery.
Read them if you are curious. They may use tools we haven't officially learned yet.
""")

# 1. else on loops
print("\n--- 1. else on loops (runs if no break) ---")
for i in range(3):
    print(i)
else:
    print("Loop finished without break.")

print("\nWith break:")
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This won't run because we broke out.")

# 2. Ternary operator
print("\n--- 2. Ternary Operator (shorthand if/else) ---")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# 3. Short-circuit evaluation
print("\n--- 3. Short-circuit evaluation ---")
def check_a():
    print("Checking A")
    return False

def check_b():
    print("Checking B")
    return True

# Python doesn't even call check_b() because check_a() is False.
if check_a() and check_b():
    print("Both true")
else:
    print("At least one is false")

# 4. Nested loops
print("\n--- 4. Nested loops (clock simulation) ---")
for hour in range(1, 3):    # 1 to 2
    for minute in range(1, 3):  # 1 to 2
        print(f"{hour}:{minute:02d}")

print("\n" + "="*70)
print("END OF HANDOUT #5")
print("="*70)