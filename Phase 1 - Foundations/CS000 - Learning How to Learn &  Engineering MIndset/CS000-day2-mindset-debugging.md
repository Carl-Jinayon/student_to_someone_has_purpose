# CS000 Day 2: Engineering Mindset & Debugging

## Overview
An engineer thinks in systems, anticipates failure, and debugs systematically. Today we practice these skills with a hands-on Python project.

## The Engineering Mindset
- Code is not just instructions; it's a small system with inputs, outputs, and failure modes.
- For every piece of code, ask "What if?" about edge cases.
- Aim for correctness, readability, testability, and maintainability.

## The Scientific Method of Debugging
1. **Observe** the exact error and behavior.
2. **Hypothesize** the cause.
3. **Test** with a minimal example.
4. **Conclude** if hypothesis correct, else iterate.
5. **Fix** minimally.

## Common Python Error Types
| Error | Meaning |
|-------|---------|
| SyntaxError | Code doesn't parse |
| NameError | Variable undefined |
| TypeError | Incompatible types |
| IndexError | List index out of range |
| KeyError | Dict key missing |
| ValueError | Right type, wrong value |
| AttributeError | No such method/attribute |
| ZeroDivisionError | Division by zero |
| FileNotFoundError | File doesn't exist |

## Reading Tracebacks
Start at the bottom (where error occurred) and read upward to see the call path. The error message usually tells you exactly what's wrong.

## Rubber-Duck Debugging
Explain your code line-by-line out loud. Forces you to confront assumptions.

## Minimal Reproducible Example
When asking for help, isolate the smallest code that shows the bug. Often you'll find it yourself.

## Deliberate Practice Project: CLI Calculator
- Basic arithmetic with user input.
- Error handling for non-numeric, division by zero, unknown operations.
- History of last 10 calculations.
- Built step-by-step with reflection.

## Self-Code Review Questions
- Are names clear?
- How many assumptions might break?
- How easy is it to add a feature?

## Exercises
1. Write 5 "What if" questions for a divide function.
2. Debug a buggy average function.
3. Trigger and fix all 9 error types.
4. Build the CLI calculator with deliberate practice stages.
5. Reflect and self-review.

## Resources
- [Python Official Errors List](https://docs.python.org/3/library/exceptions.html)
- [How to Debug (PyCon talk)](https://www.youtube.com/watch?v=52tQzQ2eE0I) (optional, 30 min)
- [Rubber Duck Debugging (blog)](https://rubberduckdebugging.com/)