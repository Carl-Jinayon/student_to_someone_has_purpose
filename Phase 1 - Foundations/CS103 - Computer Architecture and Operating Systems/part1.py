#!/usr/bin/env python3
"""
================================================================================
HANDOUT #17: CS103 – HOW COMPUTERS WORK (Part 1)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. Binary numbers
    2. Hexadecimal numbers
    3. Two's complement (negative numbers)
    4. Boolean logic (AND, OR, NOT, XOR)
    5. CPU (Control Unit, ALU, Registers)
    6. Memory hierarchy (Registers, Cache, RAM, SSD, HDD)
    7. Von Neumann architecture

Run this file to see examples and demonstrations.
================================================================================
"""

print("\n" + "="*70)
print("CS103 PART 1: HOW COMPUTERS WORK")
print("="*70)

# =============================================================================
# PART 1: Binary Representation
# =============================================================================

print("\n" + "-"*50)
print("PART 1: Binary Numbers")
print("-"*50)

def to_binary(n, bits=8):
    """Convert integer to binary string with specified bits."""
    if n < 0:
        # Two's complement (simplified for fixed bits)
        return format(n & ((1 << bits) - 1), f'0{bits}b')
    return format(n, f'0{bits}b')

print("Binary representations:")
print(f"  5  -> {to_binary(5)}")
print(f"  42 -> {to_binary(42)}")
print(f"  255 -> {to_binary(255)}")
print(f"  -5 -> {to_binary(-5)}")
print(f"  -128 -> {to_binary(-128)}")

print("\n--- Counting in binary (0-15) ---")
for i in range(16):
    print(f"  {i:2d} -> {to_binary(i)}")


# =============================================================================
# PART 2: Hexadecimal
# =============================================================================

print("\n" + "-"*50)
print("PART 2: Hexadecimal")
print("-"*50)

print("Hex mapping (4 bits):")
print("  0:0000, 1:0001, 2:0010, 3:0011")
print("  4:0100, 5:0101, 6:0110, 7:0111")
print("  8:1000, 9:1001, A:1010, B:1011")
print("  C:1100, D:1101, E:1110, F:1111")

def bin_to_hex(binary_str):
    """Convert binary string to hex string."""
    # Pad to multiple of 4
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str
    hex_map = {
        '0000':'0', '0001':'1', '0010':'2', '0011':'3',
        '0100':'4', '0101':'5', '0110':'6', '0111':'7',
        '1000':'8', '1001':'9', '1010':'A', '1011':'B',
        '1100':'C', '1101':'D', '1110':'E', '1111':'F'
    }
    hex_str = ''
    for i in range(0, len(binary_str), 4):
        hex_str += hex_map[binary_str[i:i+4]]
    return '0x' + hex_str

print("\nExamples:")
print(f"  binary 1010 -> hex {bin_to_hex('1010')}")
print(f"  binary 1010111011001101 -> hex {bin_to_hex('1010111011001101')}")


# =============================================================================
# PART 3: Boolean Logic
# =============================================================================

print("\n" + "-"*50)
print("PART 3: Boolean Logic")
print("-"*50)

print("Truth Table:")
print("  A B | A&B | A|B | A^B")
print("  ----|-----|-----|-----")
for a in [0, 1]:
    for b in [0, 1]:
        print(f"  {a} {b} |  {a & b}  |  {a | b}  |  {a ^ b}")

print("\n--- Bitwise operations in Python ---")
a = 0b1010  # 10
b = 0b1100  # 12
print(f"a = {to_binary(a)} (10)")
print(f"b = {to_binary(b)} (12)")
print(f"a & b = {to_binary(a & b)} ({a & b})")
print(f"a | b = {to_binary(a | b)} ({a | b})")
print(f"a ^ b = {to_binary(a ^ b)} ({a ^ b})")
print(f"~a    = {to_binary(~a & 0b1111)} (in 4 bits)")

print("\n--- Using bitwise for even/odd check ---")
def is_even(n):
    return (n & 1) == 0

for n in [1, 2, 3, 4, 5]:
    print(f"  {n} is even? {is_even(n)}")


# =============================================================================
# PART 4: Two's Complement
# =============================================================================

print("\n" + "-"*50)
print("PART 4: Two's Complement")
print("-"*50)

print("Two's complement formula: Flip bits and add 1")
print("\nExample: -5 in 8 bits")
print("  Step 1: 5 -> 00000101")
print("  Step 2: Flip -> 11111010")
print("  Step 3: Add 1 -> 11111011")
print(f"  Python: {to_binary(-5)}")

print("\nVerification: 5 + (-5) = 0")
print(f"  {to_binary(5)} + {to_binary(-5)} = {to_binary(5 + (-5))}")


# =============================================================================
# PART 5: Memory Hierarchy
# =============================================================================

print("\n" + "-"*50)
print("PART 5: Memory Hierarchy")
print("-"*50)

print("The Speed vs Cost Tradeoff:")
print("  ┌─────────────────┬─────────────┬─────────────┬─────────────────┐")
print("  │ Level            │ Size        │ Speed       │ Cost/GB         │")
print("  │──────────────────│─────────────│─────────────│─────────────────│")
print("  │ Registers        │ ~1 KB       │ 1 cycle     │ Extremely high  │")
print("  │ L1 Cache         │ ~64 KB      │ 1-2 cycles  │ Very high       │")
print("  │ L2 Cache         │ ~512 KB     │ ~10 cycles  │ High            │")
print("  │ L3 Cache         │ ~8 MB       │ ~40 cycles  │ Moderate        │")
print("  │ RAM              │ 8-64 GB     │ ~100 ns     │ Low             │")
print("  │ SSD              │ 256 GB-2 TB │ ~100 µs     │ Very low        │")
print("  │ HDD              │ 1-10 TB+    │ ~10 ms      │ Extremely low   │")
print("  └─────────────────┴─────────────┴─────────────┴─────────────────┘")

print("\n--- Simulating memory access ---")
def simulate_memory_access(cycles, speed, label):
    print(f"  {label}: {speed} (read takes ~{cycles} clock cycles)")

simulate_memory_access(1, "<1ns", "Register")
simulate_memory_access(100, "~100ns", "RAM")
simulate_memory_access(100000, "~100µs", "SSD")
simulate_memory_access(10000000, "~10ms", "HDD")


# =============================================================================
# PART 6: CPU Model
# =============================================================================

print("\n" + "-"*50)
print("PART 6: CPU Model")
print("-"*50)

print("The CPU has three main parts:")
print("  1. Control Unit – Decodes instructions")
print("  2. ALU – Does math and logic")
print("  3. Registers – Ultra-fast storage")

print("\nThe Instruction Cycle (Fetch-Decode-Execute):")
print("  Step 1: Fetch – Read instruction from RAM")
print("  Step 2: Decode – Figure out what it means")
print("  Step 3: Execute – Perform the operation")
print("  Step 4: Store – Write back to register/RAM")

print("\n--- Simulating a simple CPU instruction ---")
def cpu_simulate(instruction, a, b):
    if instruction == "ADD":
        return a + b
    elif instruction == "SUB":
        return a - b
    elif instruction == "AND":
        return a & b
    elif instruction == "OR":
        return a | b
    else:
        return None

print(f"  ADD 5, 3 -> {cpu_simulate('ADD', 5, 3)}")
print(f"  AND 0b1010, 0b1100 -> {to_binary(cpu_simulate('AND', 0b1010, 0b1100))}")


# =============================================================================
# PART 7: Von Neumann Architecture
# =============================================================================

print("\n" + "-"*50)
print("PART 7: Von Neumann Architecture")
print("-"*50)

print("""
Von Neumann Architecture:
    - Single memory space for both CODE and DATA.
    - The CPU fetches instructions from memory.
    - The bottleneck: CPU and memory share the same bus.

    ┌─────────────────────────────────────────────┐
    │                   CPU                       │
    │  ┌─────────┐  ┌─────────┐  ┌────────────┐ │
    │  │ Control │  │   ALU   │  │ Registers  │ │
    │  │  Unit   │  │         │  │            │ │
    │  └────┬────┘  └────┬────┘  └────────────┘ │
    │       └────────────┼───────────────────────┘
    │                    │ (Bus)
    │  ┌─────────────────▼─────────────────────┐
    │  │               MEMORY                   │
    │  │   (Instructions & Data mixed)          │
    │  └────────────────────────────────────────┘
    └─────────────────────────────────────────────┘
""")


# =============================================================================
# COMMON MISTAKES
# =============================================================================

print("\n" + "-"*50)
print("COMMON MISTAKES TO AVOID")
print("-"*50)

print("""
❌ Mistake 1: Thinking Python stores text as human-readable characters
   # Everything is binary underneath. "hello" is bytes.

❌ Mistake 2: Assuming 0.1 + 0.2 == 0.3 works
   # Binary floating-point imprecision.
   # Use round(0.1 + 0.2, 10) == 0.3

❌ Mistake 3: Confusing bits and bytes
   # 1 byte = 8 bits.
   # 1 MB = 1,048,576 bytes, not 1,000,000.

❌ Mistake 4: Ignoring memory limits
   # Loading a 10GB CSV file into Python will crash.
   # Use streaming or chunking.
""")


# =============================================================================
# CORE EXERCISES
# =============================================================================

print("\n" + "="*70)
print("CORE EXERCISES")
print("="*70)

print("""
EXERCISE 1:
Write a Python function binary_sum(a, b) that adds two binary strings
(e.g., "1010" and "1100") and returns the result as a binary string.

EXERCISE 2:
Write a function count_bits(n) that counts the number of 1s in the binary
representation of n (e.g., count_bits(5) returns 2 because 101 has two 1s).

EXERCISE 3:
Simulate a simple memory with 16 bytes. Write a program that:
- Stores two numbers at memory[0] and memory[1].
- Adds them and stores the result at memory[2].
- Prints the memory contents.
""")


# =============================================================================
# 📌 ADVANCED EXTENSION (For Wandering)
# =============================================================================

print("\n" + "="*70)
print("ADVANCED EXTENSION (Optional - For Wandering)")
print("="*70)

print("""
1. Endianness:
   Big-endian: Most significant byte first (network byte order).
   Little-endian: Least significant byte first (x86, most modern CPUs).
   Python's sys.byteorder tells you your system's endianness.

2. Floating-point representation (IEEE 754):
   0.1 is a repeating binary fraction: 0.00011001100110011...
   This is why 0.1 + 0.2 != 0.3.

3. Pipelining:
   Modern CPUs can overlap fetch-decode-execute for multiple instructions.
   Like an assembly line: while one instruction executes, the next is decoded.

4. Hyper-threading:
   A single CPU core appears as two logical cores.
   Shares resources, but can run two threads simultaneously.

5. Memory-mapped I/O:
   Some memory addresses are actually connected to hardware devices.
   Writing to them sends signals to the device.
""")

print("\n" + "="*70)
print("END OF HANDOUT #17")
print("="*70)