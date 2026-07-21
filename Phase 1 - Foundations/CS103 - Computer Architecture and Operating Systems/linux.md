================================================================================
CS103 PART 3: LINUX MASTERY – FULL LESSON
================================================================================

TABLE OF CONTENTS
=================
1. Why This Matters
2. Core Intuition (The Dark Workshop)
3. Core Command Categories
4. Lesson 3.1: Navigation (pwd, ls, cd)
5. Lesson 3.2: File Operations (touch, cp, mv, rm, mkdir)
6. Lesson 3.3: Viewing Files (cat, head, tail, less)
7. Lesson 3.4: Text Processing (grep, wc, sort, uniq, cut, sed)
8. Lesson 3.5: Redirection and Pipes (>, >>, |)
9. Lesson 3.6: Processes (ps, top, kill)
10. Lesson 3.7: Permissions (chmod, chown, ls -l)
11. Lesson 3.8: SSH & Remote Access (ssh, scp, rsync)
12. Lesson 3.9: Automation (cron, shell scripts)
13. Cheat Sheet (Quick Reference)
14. Core Exercises (5 exercises)
15. Code Demonstrations (Python simulations of Linux concepts)
================================================================================


================================================================================
1. WHY THIS MATTERS
================================================================================

You have been using a computer with a mouse and a GUI your whole life. That is
the "easy" way. The TERMINAL is the "powerful" way.

In the real world:
    - Servers (like the ones hosting your web apps) have NO screen. You connect
      via ssh and work exclusively in the terminal.
    - Cloud (AWS, GCP) is managed through the terminal.
    - DevOps, MLOps, and Backend Engineering require heavy terminal usage.

Without Linux terminal skills, you cannot:
    - Deploy a web app to the cloud.
    - Debug why your server is slow (top, htop, ps).
    - Automate repetitive tasks (shell scripts, cron jobs).


================================================================================
2. CORE INTUITION (THE DARK WORKSHOP)
================================================================================

Imagine the terminal is a DARK WORKSHOP. There are no buttons, no menus, no
mouse. Just a blank screen with a blinking cursor.

But in this workshop, you have SUPERPOWERS:
    - You can move mountains (files) instantly.
    - You can cut through stone (search millions of lines of text in seconds).
    - You can automate repetitive tasks (shell scripts) that would take you
      hours with a mouse.

The GUI is like a car with automatic transmission. The Terminal is like a
manual transmission race car. It takes more skill, but you have complete
control and can go much faster.


================================================================================
3. CORE COMMAND CATEGORIES
================================================================================

| Category          | Commands                                      | Purpose                                    |
|-------------------|-----------------------------------------------|--------------------------------------------|
| Navigation        | pwd, ls, cd                                   | Where am I? What's here? How do I move?    |
| File Operations   | touch, cp, mv, rm, mkdir                      | Create, copy, move, delete, make folders.  |
| Viewing Files     | cat, head, tail, less                         | Peek into files without opening an editor. |
| Text Processing   | grep, wc, sort, uniq, cut, sed                | Search, filter, sort, transform text.      |
| Process Control   | ps, top, kill                                 | See what's running, stop misbehaving ones. |
| Permissions       | chmod, chown                                  | Who can read/write/execute a file.         |
| Redirection       | >, >>, |, <                                   | Chain commands and save outputs.           |
| SSH & Remote      | ssh, scp, rsync                               | Connect to servers, transfer files.        |
| Automation        | cron, shell scripts                           | Schedule tasks, automate the boring stuff. |


================================================================================
4. LESSON 3.1: NAVIGATION (WHERE AM I?)
================================================================================

COMMANDS
--------
| Command | What It Does                                   | Example                    |
|---------|------------------------------------------------|----------------------------|
| pwd     | Print Working Directory – shows current folder | pwd  → /home/yourname      |
| ls      | LiSt files and folders in current directory    | ls  → Documents Downloads  |
| cd      | Change Directory – move to another folder      | cd Documents               |

COMMON SHORTCUTS
----------------
| Shortcut | What It Does                                     |
|----------|--------------------------------------------------|
| cd ..    | Go up one folder (parent directory)              |
| cd ~     | Go to your home folder (/home/yourname)          |
| cd /     | Go to the root of the entire filesystem          |
| cd -     | Go back to the previous folder you were in       |

PRACTICE
--------
Open your terminal and type these commands in order:
    pwd
    ls
    cd Documents
    pwd
    ls
    cd ..
    pwd
    cd ~
    pwd

CHECK-IN QUESTION
-----------------
What does cd .. do?
ANSWER: It goes up one folder level, to the parent directory.


================================================================================
5. LESSON 3.2: FILE OPERATIONS (CREATE, COPY, MOVE, DELETE)
================================================================================

COMMANDS
--------
| Command | What It Does                                     | Example                        |
|---------|--------------------------------------------------|--------------------------------|
| touch   | Create an empty file (or update its timestamp)   | touch notes.txt                |
| cp      | CoPy a file or folder                            | cp notes.txt backup.txt        |
| mv      | MoVe (or rename) a file or folder                | mv notes.txt old_notes.txt     |
| rm      | ReMove (delete) a file (⚠️ PERMANENT!)           | rm old_notes.txt               |
| mkdir   | MaKe DIRectory (folder)                          | mkdir my_project               |

FLAGS YOU MUST KNOW
-------------------
| Command | Flag | What It Does                                      |
|---------|------|---------------------------------------------------|
| rm      | -r   | Remove Recursively (deletes folders + contents)   |
| rm      | -f   | Force (ignore warnings, delete without asking)    |
| cp      | -r   | Copy Recursively (copy entire folders)            |
| mkdir   | -p   | Create parent directories if they don't exist     |

PRACTICE
--------
    mkdir test_folder
    cd test_folder
    touch file1.txt
    cp file1.txt file2.txt
    ls
    mv file2.txt renamed.txt
    ls
    rm renamed.txt
    ls
    cd ..

CHECK-IN QUESTION
-----------------
What is the difference between rm file.txt and rm -r folder/?
ANSWER: rm file.txt deletes a single file. rm -r folder/ deletes the entire
folder and everything inside it.


================================================================================
6. LESSON 3.3: VIEWING FILES (READ WITHOUT OPENING)
================================================================================

COMMANDS
--------
| Command | What It Does                                     | Example                  |
|---------|--------------------------------------------------|--------------------------|
| cat     | ConCATenate – prints entire file to the screen   | cat file.txt             |
| head    | Shows the first N lines (default 10)             | head -n 20 file.txt      |
| tail    | Shows the last N lines (default 10)              | tail -n 20 file.txt      |
| less    | View file page by page (press q to quit)         | less longfile.txt        |

WHY USE less INSTEAD OF cat?
----------------------------
If you cat a 10,000-line file, it floods your terminal. less lets you scroll
up and down (j/k) and search (/).

PRACTICE
--------
    echo "Line 1\nLine 2\nLine 3\nLine 4\nLine 5" > sample.txt
    cat sample.txt
    head -n 2 sample.txt
    tail -n 2 sample.txt
    less sample.txt   # (press q to quit)

CHECK-IN QUESTION
-----------------
You have a log file server.log that is 50,000 lines long. You want to see the
last 50 lines. What command do you use?
ANSWER: tail -n 50 server.log


================================================================================
7. LESSON 3.4: TEXT PROCESSING (THE POWER TOOLS)
================================================================================

COMMANDS
--------
| Command | What It Does                                      | Example                               |
|---------|---------------------------------------------------|---------------------------------------|
| grep    | Globally search for a REgex and Print             | grep "error" log.txt                  |
| grep -i | Case-insensitive search                           | grep -i "error" log.txt               |
| grep -r | Recursively search through all files in a folder  | grep -r "TODO" .                      |
| wc      | Word Count (lines, words, characters)             | wc -l file.txt  (count lines)         |
| sort    | Sort lines alphabetically                         | sort names.txt                        |
| uniq    | Remove duplicate lines (requires sorted input)    | sort names.txt | uniq                |
| cut     | Extract specific columns from a file              | cut -d',' -f1,3 data.csv              |
| sed     | Stream EDitor – find and replace                  | sed 's/old/new/g' file.txt            |

PRACTICE (Create names.txt)
----------------------------
echo -e "Alice\nBob\nCharlie\nAlice\nDiana\nBob" > names.txt

    # View the file
    cat names.txt

    # Sort it
    sort names.txt

    # Remove duplicates
    sort names.txt | uniq

    # Count unique names
    sort names.txt | uniq | wc -l

PRACTICE (Create log.txt)
-------------------------
echo -e "INFO: System started\nERROR: Network timeout\nWARNING: Low memory\nINFO: User logged in\nERROR: Disk full" > log.txt

    # Find all errors
    grep "ERROR" log.txt

    # Count errors
    grep "ERROR" log.txt | wc -l

    # Case-insensitive search for "timeout"
    grep -i "timeout" log.txt

CHECK-IN QUESTION
-----------------
You have a file errors.log and you want to count how many times the word
"timeout" appears (case-insensitive). What command do you use?
ANSWER: grep -i "timeout" errors.log | wc -l


================================================================================
8. LESSON 3.5: REDIRECTION AND PIPES (THE PLUMBING)
================================================================================

SYMBOLS
-------
| Symbol | What It Does                                        | Example                          |
|--------|-----------------------------------------------------|----------------------------------|
| >      | Redirect output to a file (OVERWRITES)              | echo "hello" > file.txt          |
| >>     | Redirect output to a file (APPENDS)                 | echo "world" >> file.txt         |
| |      | Pipe: send output of left to input of right         | grep "error" log.txt | wc -l     |
| <      | Redirect input from a file                          | sort < unsorted.txt              |

THE POWER OF PIPES (Real Example)
---------------------------------
Find all .log files, search for "error", count how many lines, and save to a
report:
    grep -r "error" *.log | wc -l > error_count.txt

PRACTICE
--------
    echo "Hello" > greeting.txt
    cat greeting.txt
    echo "World" >> greeting.txt
    cat greeting.txt

    # Pipe example: find all .py files with "TODO"
    grep -r "TODO" *.py > todos.txt

CHECK-IN QUESTION
-----------------
You want to find all .py files in a folder, search them for the word "TODO",
and save the results to a file called todos.txt. How do you do it?
ANSWER: grep -r "TODO" *.py > todos.txt


================================================================================
9. LESSON 3.6: PROCESSES (WHO IS RUNNING?)
================================================================================

COMMANDS
--------
| Command | What It Does                                      | Example                  |
|---------|---------------------------------------------------|--------------------------|
| ps      | Process Status – shows running processes          | ps aux                   |
| top     | Real-time view of running processes (Task Mgr)    | top                      |
| htop    | Better version of top (install separately)        | htop                     |
| kill    | Send a signal to a process (usually to stop it)   | kill 1234                |
| kill -9 | Force stop a process (the nuclear option)         | kill -9 1234             |

PRACTICE
--------
    # Show all running processes
    ps aux

    # Show only your processes
    ps aux | grep $USER

    # Find a specific process (e.g., python)
    ps aux | grep python

CHECK-IN QUESTION
-----------------
Your Python script train_model.py is stuck and using too much CPU. You want to
stop it. How do you find its Process ID (PID)?
ANSWER: ps aux | grep train_model.py


================================================================================
10. LESSON 3.7: PERMISSIONS (WHO CAN DO WHAT?)
================================================================================

Linux is a multi-user system. Every file has permissions for:
    - Owner (the user who created it)
    - Group (a group of users)
    - Others (everyone else)

VIEWING PERMISSIONS
-------------------
    ls -l file.txt
    # Output: -rw-r--r-- 1 user group 1234 Mar 1 10:00 file.txt

    - : File type (- for file, d for directory)
    rw- : Owner permissions (r=read, w=write, x=execute)
    r-- : Group permissions
    r-- : Others permissions

CHANGING PERMISSIONS (chmod)
----------------------------
| Command             | What It Does                                      |
|---------------------|---------------------------------------------------|
| chmod +x script.sh  | Make script.sh executable                         |
| chmod 755 file.txt  | rwxr-xr-x (Owner: all, Others: read+execute)      |
| chmod 600 secret.txt| rw------- (Only owner can read/write)             |

CHANGING OWNERSHIP (chown)
--------------------------
    chown newuser file.txt

CHECK-IN QUESTION
-----------------
You write a shell script backup.sh. You get an error: Permission denied.
What do you do?
ANSWER: chmod +x backup.sh to make it executable.


================================================================================
11. LESSON 3.8: SSH & REMOTE ACCESS (CONNECT TO THE CLOUD)
================================================================================

COMMANDS
--------
| Command | What It Does                                      | Example                                      |
|---------|---------------------------------------------------|----------------------------------------------|
| ssh     | Secure Shell – connect to a remote server         | ssh user@192.168.1.100                       |
| scp     | Secure CoPy – copy files over SSH                 | scp file.txt user@server:/home/user/         |
| rsync   | Efficiently sync files/folders over SSH           | rsync -avz ./folder user@server:/backup/     |

PRACTICE (If you have a remote server)
--------------------------------------
    # Connect to a server
    ssh admin@192.168.1.50

    # Copy a file to the server
    scp myfile.txt admin@192.168.1.50:/home/admin/

    # Sync a folder to the server
    rsync -avz ./project/ admin@192.168.1.50:/home/admin/backup/

CHECK-IN QUESTION
-----------------
You have a web server at 192.168.1.50. Your username is admin. How do you
connect to it?
ANSWER: ssh admin@192.168.1.50


================================================================================
12. LESSON 3.9: AUTOMATION (cron AND SHELL SCRIPTS)
================================================================================

SHELL SCRIPTS
-------------
A shell script is a file containing a series of Linux commands.

Create backup.sh:
    #!/bin/bash
    # This script backs up a folder
    echo "Starting backup..."
    tar -czf backup.tar.gz /home/user/documents
    echo "Backup complete!"

Make it executable:
    chmod +x backup.sh

Run it:
    ./backup.sh

cron – THE SCHEDULER
--------------------
cron runs tasks automatically at scheduled times.

Edit cron jobs:
    crontab -e

Add a line to run a script every day at 2 AM:
    0 2 * * * /home/user/backup.sh

CRON SYNTAX: minute hour day month day_of_week command

Examples:
    * * * * * command          # Every minute
    0 * * * * command          # Every hour (at minute 0)
    0 0 * * * command          # Every day at midnight
    0 0 * * 0 command          # Every Sunday at midnight
    0 0 1 * * command          # First day of every month

PRACTICE
--------
    # List your current cron jobs
    crontab -l

    # Open the cron editor
    crontab -e

CHECK-IN QUESTION
-----------------
You want to back up your database every day at 3 AM. What cron line do you add?
ANSWER: 0 3 * * * /home/user/backup_db.sh


================================================================================
13. CHEAT SHEET (QUICK REFERENCE)
================================================================================

| Category          | Command                | Purpose                                    |
|-------------------|------------------------|--------------------------------------------|
| Navigation        | pwd, ls, cd            | Move around the filesystem                 |
| File Ops          | touch, cp, mv, rm, mkdir | Manage files and folders                 |
| Viewing           | cat, head, tail, less  | Peek inside files                          |
| Search            | grep                   | Find text in files                         |
| Count             | wc                     | Count lines, words, characters             |
| Sort              | sort, uniq             | Sort and deduplicate text                  |
| Pipes             | |, >, >>               | Chain commands and save outputs            |
| Processes         | ps, top, kill          | Manage running programs                    |
| Permissions       | chmod, chown           | Control who can access files               |
| Remote            | ssh, scp, rsync        | Connect to servers, transfer files         |
| Automation        | cron, shell scripts    | Schedule and automate tasks                |


================================================================================
14. CORE EXERCISES (MASTERY CHECK)
================================================================================

EXERCISE 1 (Navigation):
Create the following folder structure using only the terminal:

    linux_practice/
    ├── data/
    │   └── sample.txt
    └── scripts/
        └── hello.sh

EXERCISE 2 (Text Processing):
Create a file names.txt with the following names:
    Alice
    Bob
    Charlie
    Alice
    Diana
    Bob

Write a command that:
    1. Sorts the names.
    2. Removes duplicates.
    3. Counts the number of unique names.
    4. Saves the output to unique_names.txt.

EXERCISE 3 (Search):
Create a file log.txt with the following content:
    INFO: System started
    ERROR: Network timeout
    WARNING: Low memory
    INFO: User logged in
    ERROR: Disk full

Write a command that:
    1. Searches for all lines containing ERROR.
    2. Extracts just the error message (e.g., "Network timeout").
    3. Counts how many errors there are.

EXERCISE 4 (Scripting):
Write a shell script called backup.sh that:
    1. Creates a backup/ folder if it doesn't exist.
    2. Copies all .txt files from the current directory to backup/.
    3. Prints "Backup completed!"

EXERCISE 5 (Automation):
Set up a cron job that runs backup.sh every day at 1:00 AM.


================================================================================
15. CODE DEMONSTRATIONS (Python Simulations)
================================================================================
Run this Python file to see Linux concepts simulated in code.
It demonstrates:
    1. Running shell commands from Python (os.system, subprocess)
    2. Simulating a grep search
    3. Simulating a cron job schedule
    4. Simulating process management (ps/top)
    5. Simulating chmod (permissions)
    6. Simulating a shell script
================================================================================
"""

# =============================================================================
