#!/usr/bin/env python3
"""
================================================================================
HANDOUT #18: CS103 – OPERATING SYSTEMS (Part 2) - FULL REFERENCE
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. What is an OS? (The Grand Manager)
    2. Processes vs. Threads (Departments vs. Workers)
    3. CPU Scheduling (Who gets the CEO's time?)
    4. Virtual Memory & Paging (The Great Illusion)
    5. File Systems (Inodes, Directories)

Run this file to see simulations of scheduling, race conditions, and paging.
================================================================================
"""

import time
import threading
import random

print("\n" + "="*70)
print("CS103 PART 2: OPERATING SYSTEMS FUNDAMENTALS")
print("="*70)

# =============================================================================
# PART 1: Processes vs Threads Simulation
# =============================================================================

print("\n" + "-"*50)
print("PART 1: Processes vs Threads (House vs Workers Analogy)")
print("-"*50)

print("""
A PROCESS is like a HOUSE:
    - Has its own address space (living room, kitchen).
    - Isolated. If one house catches fire (crashes), others are fine.

A THREAD is like a WORKER inside that house:
    - Workers share the same house (memory space).
    - They can talk to each other directly (share variables).
    - If one worker trips and ruins the living room, the whole house suffers.
""")


# =============================================================================
# PART 2: CPU Scheduling Simulation (Round Robin)
# =============================================================================

print("\n" + "-"*50)
print("PART 2: CPU Scheduling (Round Robin Example)")
print("-"*50)

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completed = False

    def execute(self, quantum):
        """Execute for one time quantum."""
        if self.remaining_time <= quantum:
            self.completed = True
            return self.remaining_time
        else:
            self.remaining_time -= quantum
            return quantum

def simulate_round_robin(processes, quantum):
    print(f"Time Quantum: {quantum}ms")
    print(f"Total Processes: {len(processes)}")
    print("Starting simulation...\n")
    
    queue = processes.copy()
    current_time = 0
    gantt_chart = []
    
    while queue:
        p = queue.pop(0)
        time_used = p.execute(quantum)
        current_time += time_used
        gantt_chart.append((p.pid, time_used))
        
        if p.completed:
            print(f"  Process P{p.pid} completed at time {current_time}ms")
        else:
            print(f"  Process P{p.pid} executed for {time_used}ms, {p.remaining_time}ms remaining")
            queue.append(p)
    
    print(f"\nTotal execution time: {current_time}ms")
    print("Gantt Chart (PID: Time):", gantt_chart)

sample_processes = [
    Process(1, 10),
    Process(2, 5),
    Process(3, 8),
    Process(4, 3)
]
simulate_round_robin(sample_processes, 4)


# =============================================================================
# PART 3: Race Condition Simulation (Concurrency Danger)
# =============================================================================

print("\n" + "-"*50)
print("PART 3: Race Condition (The Danger of Concurrency)")
print("-"*50)

balance = 0

def withdraw_without_lock(amount, iterations):
    global balance
    for _ in range(iterations):
        temp = balance
        time.sleep(0.000001)
        balance = temp - amount

lock = threading.Lock()
def withdraw_with_lock(amount, iterations):
    global balance
    for _ in range(iterations):
        with lock:
            temp = balance
            time.sleep(0.000001)
            balance = temp - amount

print("--- Without Lock (Race Condition) ---")
balance = 1000
threads = []
for i in range(2):
    t = threading.Thread(target=withdraw_without_lock, args=(10, 50))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Balance should be 0, but it is: {balance} (Data is corrupted!)")

print("\n--- With Lock (Safe) ---")
balance = 1000
threads = []
for i in range(2):
    t = threading.Thread(target=withdraw_with_lock, args=(10, 50))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"Balance is correctly: {balance} (Safe!)")


# =============================================================================
# PART 4: Virtual Memory & Paging
# =============================================================================

print("\n" + "-"*50)
print("PART 4: Virtual Memory & Paging")
print("-"*50)

print("""
Physical RAM:   [Page 0] [Page 1] [Page 2] [Page 3]
Virtual Memory: Process A thinks it has all this space.

Page Table (Translation):
    Process A, Virtual Page 0  -> Physical Page 2
    Process A, Virtual Page 1  -> Physical Page 0
    Process A, Virtual Page 2  -> Physical Page 3  (Loaded from Disk on Page Fault)
""")

page_table = {
    "A0": {"physical": 2, "present": True},
    "A1": {"physical": 0, "present": True},
    "A2": {"physical": 3, "present": False},
}
print("Page Table Contents:")
for virtual, entry in page_table.items():
    status = "Present in RAM" if entry["present"] else "PAGE FAULT (Loading from Disk)"
    print(f"  {virtual} -> Physical Page {entry['physical']} ({status})")


# =============================================================================
# PART 5: File Systems (Inodes)
# =============================================================================

print("\n" + "-"*50)
print("PART 5: File Systems & Inodes")
print("-"*50)

print("""
Inode (Index Node): A data structure that stores:
    - File metadata (Size, Permissions, Owner)
    - Timestamps (Created, Modified, Accessed)
    - Pointers to disk blocks where the actual data lives.

Directories: Simple files that map human-readable names to Inode numbers.

Example:
    File: /home/user/document.txt
    Directory entry: "document.txt" -> Inode #789
    Inode #789: Points to disk blocks 45, 47, 89 where the actual text is stored.
""")


print("\n" + "="*70)
print("END OF HANDOUT #18")
print("="*70)