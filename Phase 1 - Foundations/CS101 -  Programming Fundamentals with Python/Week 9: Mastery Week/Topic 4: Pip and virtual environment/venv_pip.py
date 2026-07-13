#!/usr/bin/env python3
"""
================================================================================
HANDOUT #13: VIRTUAL ENVIRONMENTS (venv) & pip (Mastery Week – Topic 4)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. What is a virtual environment?
    2. Creating a virtual environment (python -m venv)
    3. Activating and deactivating
    4. Installing packages with pip
    5. Creating requirements.txt
    6. Installing from requirements.txt

This is a terminal-heavy topic. The commands are provided here for reference.
Run this script to print out the instructions.
================================================================================
"""

print("\n" + "="*70)
print("MASTERY WEEK – TOPIC 4: VIRTUAL ENVIRONMENTS (venv) & pip")
print("="*70)

print("""
This topic is best learned in the terminal. This script provides all commands
as a reference. Open your terminal and follow along.

================================================================================
PART 1: What is a Virtual Environment?
================================================================================

A virtual environment is an isolated Python installation for a specific project.
It has its own:
    - Python interpreter
    - pip
    - site-packages folder (where installed packages live)

Why use it?
    - Avoid conflicts between projects.
    - Reproducible environments (with requirements.txt).
    - No need for admin permissions to install packages.
    - Keeps your system Python clean.

================================================================================
PART 2: Creating a Virtual Environment
================================================================================

Step 1: Navigate to your project folder.
    cd my_project

Step 2: Create the virtual environment.
    python -m venv venv

    This creates a folder named 'venv' containing the isolated environment.

Step 3: Activate the virtual environment.

    On Windows (Command Prompt):
        venv\\Scripts\\activate.bat

    On Windows (PowerShell):
        venv\\Scripts\\Activate.ps1

    On macOS / Linux:
        source venv/bin/activate

    You will see (venv) in your terminal prompt when active.

Step 4: Deactivate when done.
    deactivate

================================================================================
PART 3: Installing Packages with pip
================================================================================

While the virtual environment is ACTIVE, use pip to install packages.

    pip install package_name          # Install latest version
    pip install package_name==1.2.3   # Install specific version
    pip install package_name>=1.2.0   # Install minimum version

    # Install multiple packages at once
    pip install requests pytest numpy

    # List installed packages
    pip list

    # Show package details
    pip show package_name

================================================================================
PART 4: requirements.txt
================================================================================

requirements.txt is a file that lists all packages needed for a project.

    # Generate requirements.txt from current environment
    pip freeze > requirements.txt

    # Install all packages from requirements.txt
    pip install -r requirements.txt

Example requirements.txt:
    requests==2.31.0
    pytest==7.4.0
    numpy==1.24.3

================================================================================
PART 5: Best Practices
================================================================================

    ✅ ALWAYS use a virtual environment for every project.
    ✅ Name the virtual environment folder 'venv' or '.venv'.
    ✅ Add 'venv/' to .gitignore (never commit it to Git).
    ✅ Always commit requirements.txt.
    ✅ Activate the venv before running your code or installing packages.
    ✅ Deactivate when you switch projects.

================================================================================
PART 6: Common Workflow (Full Example)
================================================================================

    # Create a new project
    mkdir my_project
    cd my_project

    # Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate  # (or Windows equivalent)

    # Install packages
    pip install requests pytest

    # Write your code (in main.py, etc.)
    # ...

    # Freeze dependencies
    pip freeze > requirements.txt

    # Deactivate
    deactivate

    # Later, on another machine:
    git clone my_project
    cd my_project
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    # Run your code!

================================================================================
COMMON MISTAKES TO AVOID
================================================================================

❌ Mistake 1: Forgetting to activate the venv
   # Installing packages without activating installs them globally!
   # Fix: Always see (venv) in your prompt before installing.

❌ Mistake 2: Committing venv/ to Git
   # Adds hundreds of MB to your repo, causes conflicts.
   # Fix: Add venv/ to .gitignore.

❌ Mistake 3: Not creating requirements.txt
   # Others cannot recreate your environment.
   # Fix: Always run 'pip freeze > requirements.txt'.

❌ Mistake 4: Installing packages globally for a project
   # Causes conflicts over time.
   # Fix: Create a venv for every project.

❌ Mistake 5: Forgetting to activate before running the project
   # Code might run with the wrong package versions.
   # Fix: Always activate first.

================================================================================
CORE EXERCISES (Mastery Check)
================================================================================

EXERCISE 1 (Setup):
1. Create a new folder called 'my_project'.
2. Inside it, create a virtual environment named 'venv'.
3. Activate the virtual environment.
4. Install the package 'requests' using pip.
5. Generate a requirements.txt file.
6. Deactivate the virtual environment.

EXERCISE 2 (Recreation):
1. Delete the 'venv' folder.
2. Recreate the virtual environment.
3. Activate it.
4. Install all dependencies from requirements.txt.
5. Verify that requests is installed correctly.

EXERCISE 3 (Project Structure):
Create a project folder with the following structure:
    my_library/
    ├── venv/               # Virtual environment (not committed)
    ├── requirements.txt    # Dependencies
    ├── .gitignore          # Ignore venv/, __pycache__, etc.
    └── main.py             # Your code
""")


# =============================================================================
# HELPER FUNCTIONS (Optional - For curiosity)
# =============================================================================

def print_commands():
    """Print all commands in a table format for quick reference."""
    print("\n" + "="*70)
    print("QUICK REFERENCE TABLE")
    print("="*70)

    commands = [
        ("Create venv", "python -m venv venv"),
        ("Activate (Windows CMD)", "venv\\Scripts\\activate.bat"),
        ("Activate (Windows PowerShell)", "venv\\Scripts\\Activate.ps1"),
        ("Activate (macOS/Linux)", "source venv/bin/activate"),
        ("Deactivate", "deactivate"),
        ("Install package", "pip install package_name"),
        ("Install specific version", "pip install package_name==1.2.3"),
        ("Generate requirements", "pip freeze > requirements.txt"),
        ("Install from requirements", "pip install -r requirements.txt"),
        ("List installed packages", "pip list"),
        ("Show package info", "pip show package_name"),
        ("Uninstall package", "pip uninstall package_name"),
    ]

    print("\n{:<35} -> {}".format("Task", "Command"))
    print("-" * 70)
    for task, cmd in commands:
        print("{:<35} -> {}".format(task, cmd))

    print("\n" + "-"*50)
    print("EXERCISE SUMMARY")
    print("-"*50)

    print("""
Follow the exercises in the main handout above. They require you to
open a terminal and practice creating, activating, and managing virtual
environments. This is a practical skill—you must do it, not just read it.
    """)


if __name__ == "__main__":
    print_commands()

    print("\n" + "="*70)
    print("END OF HANDOUT #13")
    print("="*70)