# print(f"Hello {name}")
# Three ways to Format Strings
# 1. old (% formatting)
# 2. .format()
# 3. f-strings (Modern)
value = 483294.43223
print(f"{value:.2f}") # Formatting decimals points
accuracy = 0.985
print(f"{accuracy:.1%}") # Formatting percentages
population = 1234567890
print(f"{population:,}") # Formatting large numbers
name = "Carl"
print(f"|{name:<20}|") # left alignment
print(f"|{name:>20}|") # right alignment
print(f"|{name:^20}|") # center alignment
number = 42
print(f"{number:05}") # zero padding
price = 1234.5678
print(f"${price:,.2f}")

# Debugging with f-Strings (Python 3.8+)
x = 10
y = 20

print(f"{x=}, {y=}")

# Exercise:
product = "Laptop"
price = 49999.5
print(f"{product}: ${price:,.2f}")


