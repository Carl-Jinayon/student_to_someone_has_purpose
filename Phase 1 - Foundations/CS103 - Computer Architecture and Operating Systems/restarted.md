# CS103 – Architecture & Operating Systems (Restarted) – STUDY PHASE

## 🧭 How to Use This File (READ THIS FIRST)

This is your **Study Phase** material.

- Read this file carefully.
- Copy the code snippets into your terminal/Python.
- Experiment with the concepts.
- **Do not report back to me yet.**
- **Do not attempt any formal exercises.**

When you have completed all the Practical Labs and feel comfortable with the concepts, type **"Ready"** in the chat. Then, and only then, will I give you the Application Phase (Cold Start scenarios).

---

# 📖 PART 1: STUDY PHASE

## Why This Matters

You have written Python code. You have used Git. You have managed virtual environments. But **do you know what is actually happening under the hood?**

- Why does `while True: x = x + 1` eventually slow down?
- Why does your ML model crash with `MemoryError` when loading a 10GB dataset?
- Why does `0.1 + 0.2 != 0.3`?
- What actually happens when you type `python script.py`?

Without understanding the machine, you are programming by **superstition**. You guess what is fast or slow. You don't know why things break. This subject gives you the **mental model** of the machine your code runs on.

**In your career:**
- Understanding CPU caches explains why certain Python data structures are faster.
- Understanding binary explains why `0.1 + 0.2 != 0.3`.
- Understanding memory explains why loading a 10GB CSV file crashes your laptop.
- Understanding processes and threads is essential for building web servers, ML pipelines, and concurrent systems.

---

## Core Intuition (The Factory Model)

Imagine a computer is a **factory**:

- The **CPU** is the **factory floor**. It has workers (cores) that do the actual work. They are incredibly fast but can only do one thing at a time.
- The **RAM** is the **workbench** next to the floor. It holds materials (data) and instructions (code) that the workers are currently using. Fast, but limited in size.
- The **Hard Drive (SSD/HDD)** is the **warehouse** in the back. It holds everything—materials, old projects, finished goods. Huge, but slow to access.
- The **Memory Hierarchy** is the **logistics chain**. The worker looks at their hands first (registers), then the workbench (RAM), then the warehouse (disk). The closer it is to the worker, the faster it is.

---

## Lesson 1: Binary – The Language of Computers

Computers don't understand `"hello"` or `5`. They understand **only two states**: ON (1) and OFF (0). Everything—numbers, text, images, videos—is stored as sequences of these 1s and 0s.

### Counting in Binary

| Decimal | Binary (8 bits) |
| :--- | :--- |
| 0 | 00000000 |
| 1 | 00000001 |
| 2 | 00000010 |
| 3 | 00000011 |
| 4 | 00000100 |
| 5 | 00000101 |
| 6 | 00000110 |
| 7 | 00000111 |
| 8 | 00001000 |
| 9 | 00001001 |
| 10 | 00001010 |

**Bit** = One digit (0 or 1).  
**Byte** = 8 bits. This is the fundamental unit of memory.

### The Commands (Type these in Python)

```python
# Convert decimal to binary
print(bin(5))     # 0b101
print(bin(42))    # 0b101010

# Convert binary to decimal
print(int('101', 2))    # 5
print(int('101010', 2)) # 42

# Bitwise operations
print(5 & 3)    # 1 (AND)
print(5 | 3)    # 7 (OR)
print(5 ^ 3)    # 6 (XOR)
print(~5)       # -6 (NOT)
print(5 << 1)   # 10 (Left shift)
print(5 >> 1)   # 2 (Right shift)
```

> **🛠️ PRACTICAL LAB:** Open Python and play with `bin()`, `int()`, and bitwise operators. Convert decimal 255 to binary. What is `0b1111` in decimal?

---

## Lesson 2: Hexadecimal – Human-Readable Binary

Binary is hard to read. `1010111011001101` is ugly. So we group bits into **nibbles (4 bits)** and map each to a hex digit (0-9, A-F).

| Hex | Binary | Decimal |
| :--- | :--- | :--- |
| 0 | 0000 | 0 |
| 1 | 0001 | 1 |
| 2 | 0010 | 2 |
| 3 | 0011 | 3 |
| 4 | 0100 | 4 |
| 5 | 0101 | 5 |
| 6 | 0110 | 6 |
| 7 | 0111 | 7 |
| 8 | 1000 | 8 |
| 9 | 1001 | 9 |
| A | 1010 | 10 |
| B | 1011 | 11 |
| C | 1100 | 12 |
| D | 1101 | 13 |
| E | 1110 | 14 |
| F | 1111 | 15 |

**Example:** `1010111011001101` (16 bits)  
Group: `1010 1110 1100 1101`  
Hex: `A E C D` → `0xAECD`

**Why use hex?** Memory addresses, color codes (`#FF5733`), and debuggers all use hex. It's the shorthand for binary.

```python
# Convert decimal to hex
print(hex(255))   # 0xff
print(hex(42))    # 0x2a

# Convert hex to decimal
print(int('ff', 16))   # 255
print(int('2a', 16))   # 42
```

> **🛠️ PRACTICAL LAB:** Open Python. Convert decimal `1234` to hex. Convert hex `0xdead` to decimal.

---

## Lesson 3: Two's Complement – Representing Negative Numbers

How do you represent -5 in binary? You could use a sign bit (0=positive, 1=negative), but that makes math complicated. Computers use **Two's Complement**.

**Formula:** Flip all bits and add 1.

**Example: -5 in 8 bits (0000 0101 = 5)**

1. Flip bits: `1111 1010`
2. Add 1: `1111 1011` = -5

**Why?** It makes addition work naturally. `5 + (-5) = 0`:

```
 0000 0101  (+5)
+1111 1011  (-5)
=0000 0000  (0)
```

**Range of 8-bit signed integers:** -128 to 127.  
**Range of 8-bit unsigned:** 0 to 255.

```python
# Python handles two's complement for you
print(bin(-5))  # -0b101 (Python's representation)
print(-5 & 0b11111111)  # 251 (8-bit two's complement)
```

> **🛠️ PRACTICAL LAB:** Calculate the two's complement of `-12` in 8 bits. Use Python to verify your answer.

---

## Lesson 4: Boolean Logic – The Building Blocks

Everything a computer does is built from **Boolean logic gates**: AND, OR, NOT, XOR.

- **AND**: True only if BOTH inputs are True.
- **OR**: True if AT LEAST ONE input is True.
- **NOT**: Flips True to False, False to True.
- **XOR**: True if inputs are DIFFERENT.

These gates are physically built from **transistors** (tiny switches). Billions of transistors on a single CPU chip implement these gates.

### Truth Tables

| A | B | A AND B | A OR B | A XOR B |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

```python
# Boolean logic in Python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
print(True ^ False)    # True (XOR using ^)
```

> **🛠️ PRACTICAL LAB:** Write a Python function that implements a half-adder (adds two bits and returns sum and carry).

## Lesson 5: The CPU – The Brain

**CPU** = Central Processing Unit. It executes instructions (machine code). Your Python code is translated into machine code.

### The CPU has three main parts:

| Part | What It Does |
| :--- | :--- |
| **Control Unit** | Decodes instructions and coordinates what happens. |
| **ALU (Arithmetic Logic Unit)** | Does math (+, -, *, /) and logic (AND, OR, NOT). |
| **Registers** | Tiny, ultra-fast storage inside the CPU (1-2 clock cycles). Holds data currently being worked on. |

### The Instruction Cycle (Fetch-Decode-Execute):

1. **Fetch:** The CPU reads the next instruction from RAM.
2. **Decode:** The Control Unit figures out what the instruction means.
3. **Execute:** The ALU or other unit performs the operation.
4. **Store:** The result is written back to a register or RAM.

**Clock Speed:** Measured in GHz (e.g., 3.5 GHz = 3.5 billion cycles per second). Each cycle is one step in the instruction cycle.

```python
# Simulating a simple CPU instruction
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

print(cpu_simulate("ADD", 5, 3))   # 8
print(cpu_simulate("AND", 0b1010, 0b1100))  # 8 (0b1000)
```

> **🛠️ PRACTICAL LAB:** Open your system monitor (Task Manager on Windows, `htop` on Linux). Watch the CPU usage spike when you run a heavy Python script. What does "100% CPU" actually mean?

---

## Lesson 6: Memory Hierarchy – The Speed vs Cost Tradeoff

| Level | Size | Speed | Cost/GB |
| :--- | :--- | :--- | :--- |
| **Registers** | ~1 KB | 1 cycle (<1 ns) | Extremely expensive |
| **L1 Cache** | ~64 KB | 1-2 cycles | Very expensive |
| **L2 Cache** | ~512 KB | 10 cycles | Expensive |
| **L3 Cache** | ~8 MB | 40 cycles | Moderate |
| **RAM** | 8-64 GB | 100 cycles (~100 ns) | Inexpensive |
| **SSD** | 256 GB - 2 TB | ~100,000 cycles (~100 µs) | Cheap |
| **HDD** | 1 TB - 10 TB+ | ~10,000,000 cycles (~10 ms) | Very cheap |

**The Bottleneck:** The CPU can execute billions of instructions per second. RAM takes ~100 nanoseconds to respond. The CPU spends most of its time **waiting** for data from RAM.

**Why Python can be slow:** Python is interpreted. The interpreter adds overhead. But even compiled C code is memory-bound—it waits for data. Understanding this helps you optimize by accessing memory efficiently (e.g., using arrays instead of linked lists).

```python
# Simulating memory access speed differences
import time

# Fast access (in memory)
start = time.time()
data = [i for i in range(1000000)]
end = time.time()
print(f"List creation: {end - start:.4f} seconds")

# Slow access (simulating disk I/O)
start = time.time()
with open("large_file.txt", "w") as f:
    f.write("Hello" * 1000000)
end = time.time()
print(f"Disk write: {end - start:.4f} seconds")
```

> **🛠️ PRACTICAL LAB:** Run the code above. Notice the huge difference in speed between memory and disk operations.

---

## Lesson 7: Von Neumann Architecture (The Blueprint)

Almost all modern computers follow the **Von Neumann architecture**:

- **Single memory space** for both instructions (program code) and data.
- The CPU **fetches** instructions from memory, decodes them, and executes them.

**The Bottleneck:** Since instructions and data share the same bus (wire), the CPU cannot fetch both at the same time. This is the **Von Neumann bottleneck**. Modern CPUs use **caches** and **pipelines** to mitigate this.

```
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
```

> **🛠️ PRACTICAL LAB:** Open Python and check how much memory your Python process is using. Why does it take more memory than the sum of all your variables?

---

## Lesson 8: Processes vs Threads – The Core Distinction

**Process**: An executing program. Think of a **house**.
- It has its own private space (memory address space).
- It contains its own code, data, and resources.
- It is isolated from other houses (if a process crashes, other processes don't crash).
- *Example:* When you open VS Code, that is one process. Opening a new Firefox tab is another process.

**Thread**: A single flow of execution *inside* a process. Think of the **workers inside the house**.
- All workers (threads) share the same house (memory space).
- They can easily talk to each other (share variables).
- *Example:* In a web server (a process), there are often 100 threads. Thread 1 handles User A's request, while Thread 2 handles User B's request at the exact same time.

### Comparison Table

| Feature | Process | Thread |
| :--- | :--- | :--- |
| **Memory Space** | Private (has its own) | Shared with siblings |
| **Communication** | Slow (must use special OS channels) | Fast (can directly read/write shared variables) |
| **Crash impact** | One crashing doesn't affect others | One crashing often crashes the entire parent process |
| **Creation speed** | Slow (heavy to set up) | Fast (lightweight) |

```python
# Demonstrating process vs thread creation (concept only)
import threading
import multiprocessing

def worker():
    print("Working...")

# Thread (lightweight, shared memory)
thread = threading.Thread(target=worker)
thread.start()
thread.join()

# Process (heavy, isolated memory)
process = multiprocessing.Process(target=worker)
process.start()
process.join()
```

> **🛠️ PRACTICAL LAB:** Write a Python script that creates 10 threads and 10 processes. Use `time.sleep()` to keep them alive. Open `htop` or Task Manager. Notice the difference in memory usage.

---

## 🛠️ PRACTICAL LABS SUMMARY (The "Study Checklist")

| Topic | What to do |
| :--- | :--- |
| **Binary** | Use `bin()` and `int()` to convert numbers. Practice bitwise operators. |
| **Hexadecimal** | Use `hex()` and `int()` to convert numbers. |
| **Two's Complement** | Calculate the two's complement of negative numbers manually. |
| **Boolean Logic** | Use `and`, `or`, `not`, `^` in Python. |
| **CPU** | Open `htop`/Task Manager and watch CPU usage spike. |
| **Memory Hierarchy** | Run the list creation vs disk write code. Notice the speed difference. |
| **Von Neumann** | Check Python's memory usage. |
| **Processes vs Threads** | Create 10 threads and 10 processes. Compare memory usage. |

---

## 🛑 STOP SIGN

# ⛔ YOU HAVE REACHED THE END OF THE STUDY PHASE. ⛔

**Do not proceed further. You are now in the Study Phase.**

Your task right now is:
1. Open your terminal.
2. Open Python and experiment with binary, hex, and bitwise operators.
3. Run the memory hierarchy simulation.
4. Create threads and processes and observe the differences.

Come back when you have successfully executed every single command above at least once. When you are ready, type **"Ready"** in the chat.

**I will wait.**