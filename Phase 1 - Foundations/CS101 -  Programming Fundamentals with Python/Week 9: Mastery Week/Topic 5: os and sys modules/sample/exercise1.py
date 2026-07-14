"""
Exercise 1 (enumerate with start):
Given a list of tasks ["Buy groceries", "Clean room", "Study Python"], 
use enumerate to print them as a numbered to‑do list starting from 1. Output should be:

1. Buy groceries
2. Clean room
3. Study Python
"""

tasks = ["Buy groceries", "Clean room", "Study Python"]

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
