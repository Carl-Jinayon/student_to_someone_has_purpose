# PYTHON CODE (The executable part)
# =============================================================================

import os
import time
import subprocess
from datetime import datetime

print("\n" + "="*70)
print("CS103 PART 3: LINUX MASTERY (CODE DEMONSTRATIONS)")
print("="*70)

# -----------------------------------------------------------------------------
# DEMO 1: Running Shell Commands from Python
# -----------------------------------------------------------------------------

print("\n" + "-"*50)
print("DEMO 1: Running Shell Commands from Python")
print("-"*50)

print("\n--- os.system example ---")
os.system("echo 'Hello from Python!'")
os.system("ls -la | head -n 5")

print("\n--- subprocess example (captures output) ---")
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(f"Output (first 200 chars):\n{result.stdout[:200]}...")


# -----------------------------------------------------------------------------
# DEMO 2: Simulating a grep Search
# -----------------------------------------------------------------------------

print("\n" + "-"*50)
print("DEMO 2: Simulating grep (Searching Text)")
print("-"*50)

def grep_simulate(lines, pattern, case_sensitive=True):
    """Simulate grep: return lines containing the pattern."""
    results = []
    for line in lines:
        if case_sensitive:
            if pattern in line:
                results.append(line)
        else:
            if pattern.lower() in line.lower():
                results.append(line)
    return results

log_lines = [
    "INFO: System started",
    "ERROR: Network timeout",
    "WARNING: Low memory",
    "INFO: User logged in",
    "ERROR: Disk full",
]

print("Log file contents:")
for line in log_lines:
    print(f"  {line}")

print("\n--- grep 'ERROR' (case-sensitive) ---")
errors = grep_simulate(log_lines, "ERROR")
for line in errors:
    print(f"  {line}")

print(f"\nTotal errors: {len(errors)}")

print("\n--- grep -i 'timeout' (case-insensitive) ---")
matches = grep_simulate(log_lines, "timeout", case_sensitive=False)
for line in matches:
    print(f"  {line}")


# -----------------------------------------------------------------------------
# DEMO 3: Simulating a Cron Job Schedule
# -----------------------------------------------------------------------------

print("\n" + "-"*50)
print("DEMO 3: Simulating cron (Scheduled Tasks)")
print("-"*50)

def parse_cron(cron_line):
    """Parse a cron line and return if it should run at the given time."""
    minute, hour, day, month, day_of_week, command = cron_line.split(maxsplit=5)
    now = datetime.now()
    
    if minute != "*" and int(minute) != now.minute:
        return False
    if hour != "*" and int(hour) != now.hour:
        return False
    if day != "*" and int(day) != now.day:
        return False
    if month != "*" and int(month) != now.month:
        return False
    if day_of_week != "*" and int(day_of_week) != now.weekday():
        return False
    
    return True

cron_jobs = [
    "* * * * * /home/user/backup.sh",
    "0 2 * * * /home/user/daily_backup.sh",
    "0 3 * * 1 /home/user/weekly_backup.sh",
]

print("Cron jobs scheduled:")
for job in cron_jobs:
    print(f"  {job}")

print("\nChecking if any job should run right now...")
now = datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M')}")

for job in cron_jobs:
    if parse_cron(job):
        print(f"  ✅ Should run NOW: {job}")
    else:
        print(f"  ❌ Should NOT run now: {job}")


# -----------------------------------------------------------------------------
# DEMO 4: Simulating Process Management (ps / top)
# -----------------------------------------------------------------------------

print("\n" + "-"*50)
print("DEMO 4: Simulating Process Management (ps/top)")
print("-"*50)

processes = [
    {"pid": 1, "name": "systemd", "cpu": 0.1, "memory": 0.5},
    {"pid": 1234, "name": "python", "cpu": 45.2, "memory": 12.3},
    {"pid": 5678, "name": "chrome", "cpu": 12.1, "memory": 8.7},
    {"pid": 9012, "name": "docker", "cpu": 3.4, "memory": 2.1},
]

print("Running processes (simulated):")
print(f"{'PID':>6} {'Name':<15} {'CPU%':>8} {'Memory%':>10}")
print("-" * 45)
for p in processes:
    print(f"{p['pid']:>6} {p['name']:<15} {p['cpu']:>8.1f} {p['memory']:>10.1f}")

print("\n--- Finding process with highest CPU ---")
highest_cpu = max(processes, key=lambda p: p["cpu"])
print(f"Highest CPU process: {highest_cpu['name']} (PID: {highest_cpu['pid']}) at {highest_cpu['cpu']}%")

print("\n--- Simulating 'kill' to stop a process ---")
pid_to_kill = 1234
for p in processes:
    if p["pid"] == pid_to_kill:
        print(f"  🔪 Killing process {p['name']} (PID: {p['pid']})")
        processes.remove(p)
        break

print(f"Remaining processes: {len(processes)}")


# -----------------------------------------------------------------------------
# DEMO 5: Simulating chmod (Permissions)
# -----------------------------------------------------------------------------

print("\n" + "-"*50)
print("DEMO 5: Simulating chmod (Permissions)")
print("-"*50)

print("File permissions are represented by 9 bits:")
print("  r w x  |  r w x  |  r w x")
print("  Owner  |  Group  |  Other")

def parse_permissions(perm_str):
    if len(perm_str) != 9:
        return "Invalid"
    mapping = {
        "---": 0, "--x": 1, "-w-": 2, "-wx": 3,
        "r--": 4, "r-x": 5, "rw-": 6, "rwx": 7
    }
    owner = mapping[perm_str[0:3]]
    group = mapping[perm_str[3:6]]
    other = mapping[perm_str[6:9]]
    return int(f"{owner}{group}{other}")

perm_str = "rwxr-xr--"
print(f"\nPermission string: {perm_str}")
print(f"Octal representation: {parse_permissions(perm_str)}")

print("\n--- chmod examples ---")
print("  chmod +x script.sh  -> Adds execute permission")
print("  chmod 755 file.txt  -> rwxr-xr-x")
print("  chmod 600 secret.txt -> rw-------")


# -----------------------------------------------------------------------------
# DEMO 6: Simulating a Shell Script
# -----------------------------------------------------------------------------

print("\n" + "-"*50)
print("DEMO 6: Simulating a Shell Script")
print("-"*50)

print("""
A shell script is a file containing commands:

#!/bin/bash
# This is a comment
echo "Starting backup..."
mkdir -p backup
cp *.txt backup/
echo "Backup completed!"

To run it:
    chmod +x backup.sh
    ./backup.sh
""")

def simulate_backup_script():
    print("  [Running backup.sh]")
    print("  Starting backup...")
    print("  Creating backup folder...")
    print("  Copying .txt files...")
    print("  Backup completed!")

print("\n--- Simulating backup.sh execution ---")
simulate_backup_script()

print("\n" + "="*70)
print("END OF CS103 PART 3 DEMONSTRATIONS")
print("="*70)