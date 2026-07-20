#!/usr/bin/env python3
"""
================================================================================
HANDOUT #16: GIT & VERSION CONTROL (CS104)
================================================================================
Student: ________________________________
Date: ___________________________________

This handout covers:
    1. git init and git clone
    2. git add, git commit, git push
    3. Branching (git branch, git checkout, git merge)
    4. Handling merge conflicts
    5. Undoing changes (git reset, git revert, git checkout)
    6. git reflog (recovery)
    7. GitHub workflow
    8. .gitignore essentials

Commands are provided as a reference. Open your terminal and follow along.
================================================================================
"""

print("\n" + "="*70)
print("CS104: GIT & VERSION CONTROL")
print("="*70)

print("""
This topic is best learned in the terminal. This script provides all commands
as a reference. Open your terminal and follow along.

================================================================================
PART 1: GETTING STARTED
================================================================================

# Check if Git is installed
git --version

# Configure your identity (do this once)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Start a new repository
mkdir my_project
cd my_project
git init

# Or clone an existing repository
git clone https://github.com/username/repo.git

================================================================================
PART 2: THE BASIC CYCLE (add, commit, push)
================================================================================

# Check status
git status

# Stage changes
git add file.py      # Stage a specific file
git add .            # Stage ALL changes

# Commit
git commit -m "feat: add search functionality"

# Connect to remote (GitHub)
git remote add origin https://github.com/yourusername/repo.git

# Push
git push -u origin main   # First push
git push                  # Subsequent pushes

================================================================================
PART 3: BRANCHING
================================================================================

# Create and switch to a new branch
git checkout -b feature/search

# Or in two steps:
git branch feature/search
git checkout feature/search

# List branches
git branch           # Local branches
git branch -r        # Remote branches

# Switch branches
git checkout main

# Merge a branch
git checkout main
git merge feature/search

# Delete a branch
git branch -d feature/search   # Local
git push origin --delete feature/search  # Remote

================================================================================
PART 4: MERGE CONFLICTS (Resolving)
================================================================================

When a conflict occurs, Git marks the file:
    <<<<<<< HEAD
    Your changes
    =======
    Their changes
    >>>>>>> other-branch

1. Edit the file to resolve the conflict.
2. Stage the resolved file: git add file.py
3. Commit: git commit -m "Resolve merge conflict"

================================================================================
PART 5: UNDOING CHANGES
================================================================================

# Discard uncommitted changes to a file
git checkout -- file.py

# Unstage a file (keep changes)
git reset HEAD file.py

# Undo the last commit (keep changes)
git reset --soft HEAD~1

# Undo the last commit (discard changes) - DANGEROUS!
git reset --hard HEAD~1

# Revert a commit (safe, adds a new commit that undoes changes)
git revert HEAD

================================================================================
PART 6: git reflog (The Ultimate Recovery Tool)
================================================================================

# Show all actions
git reflog

# Recover a lost commit
git checkout COMMIT_HASH
# Or create a branch from it:
git branch recover-branch COMMIT_HASH

================================================================================
PART 7: COMMIT MESSAGE CONVENTIONS
================================================================================

feat:     New feature
fix:      Bug fix
docs:     Documentation changes
refactor: Code cleanup (no behavior change)
test:     Adding or updating tests
chore:    Maintenance (dependencies, configs)

Example: git commit -m "feat: add book search by title"

================================================================================
PART 8: .gitignore ESSENTIALS
================================================================================

Create a .gitignore file in your project root with:

    # Python
    __pycache__/
    *.pyc
    *.pyo
    *.pyd
    
    # Virtual environments
    venv/
    .venv/
    env/
    
    # IDE
    .vscode/
    .idea/
    *.swp
    
    # Environment variables
    .env
    *.env
    
    # Data files
    data/*.json
    *.db
    
    # OS files
    .DS_Store
    Thumbs.db
    
    # Testing
    .pytest_cache/
    .coverage
    htmlcov/

================================================================================
PART 9: FULL PROFESSIONAL WORKFLOW
================================================================================

# 1. Start your day
git checkout main
git pull origin main

# 2. Create a feature branch
git checkout -b feature/my-feature

# 3. Work (make changes, test)

# 4. Stage and commit frequently
git add .
git commit -m "feat: add search function"
git commit -m "feat: handle empty search results"

# 5. Push your branch
git push -u origin feature/my-feature

# 6. Open a Pull Request on GitHub

# 7. After PR is approved and merged:
git checkout main
git pull origin main
git branch -d feature/my-feature
git push origin --delete feature/my-feature

================================================================================
COMMON MISTAKES TO AVOID
================================================================================

❌ Mistake 1: Committing directly to main
   # Fix: Always create a branch for new features.

❌ Mistake 2: Vague commit messages ("update", "fix")
   # Fix: Use conventional commits: "feat: add search"

❌ Mistake 3: Forgetting .gitignore before first commit
   # Fix: Always create .gitignore before git add .

❌ Mistake 4: git push without git pull (on shared branches)
   # Fix: Always pull before pushing: git pull origin main

❌ Mistake 5: Using git reset --hard without thinking
   # Fix: Use git stash to save changes, or use --soft.

❌ Mistake 6: Committing sensitive data (API keys, passwords)
   # Fix: NEVER commit .env files. Use .gitignore.

================================================================================
CORE EXERCISES (Mastery Check)
================================================================================

EXERCISE 1 (Setup):
1. Create a new folder called 'git-practice'.
2. Initialize it as a Git repository.
3. Create a README.md file with '# Git Practice'.
4. Stage and commit it.
5. Create a file called hello.py with 'print("Hello, Git!")'.
6. Stage and commit it.

EXERCISE 2 (Branching):
1. Create a new branch called 'feature/goodbye'.
2. In that branch, add a file goodbye.py with 'print("Goodbye, Git!")'.
3. Commit it.
4. Switch back to main.
5. Merge feature/goodbye into main.
6. Delete the branch.

EXERCISE 3 (Undoing):
1. Make a change to hello.py that you regret.
2. Discard the change using git checkout -- hello.py.
3. Make another change and commit it.
4. Undo the commit using git reset --soft HEAD~1.
5. Verify your changes are still in the working directory.

EXERCISE 4 (GitHub):
1. Create a public repository on GitHub called 'git-practice'.
2. Connect your local repository to it.
3. Push all your commits.
4. Verify the repository is visible on GitHub.
""")


# =============================================================================
# QUICK REFERENCE TABLE
# =============================================================================

print("\n" + "="*70)
print("QUICK REFERENCE TABLE")
print("="*70)

commands = [
    ("Initialize repo", "git init"),
    ("Clone repo", "git clone <url>"),
    ("Check status", "git status"),
    ("Stage file", "git add <file>"),
    ("Stage all", "git add ."),
    ("Commit", "git commit -m 'message'"),
    ("Push", "git push origin main"),
    ("Pull", "git pull origin main"),
    ("List branches", "git branch"),
    ("Create branch", "git branch <name>"),
    ("Switch branch", "git checkout <name>"),
    ("Create & switch", "git checkout -b <name>"),
    ("Merge branch", "git merge <name>"),
    ("Delete local branch", "git branch -d <name>"),
    ("Delete remote branch", "git push origin --delete <name>"),
    ("Discard changes", "git checkout -- <file>"),
    ("Unstage", "git reset HEAD <file>"),
    ("Undo commit (keep changes)", "git reset --soft HEAD~1"),
    ("Undo commit (discard changes)", "git reset --hard HEAD~1"),
    ("Safe revert", "git revert HEAD"),
    ("View history", "git log --oneline --graph"),
    ("View reflog", "git reflog"),
    ("Stash changes", "git stash"),
    ("Apply stash", "git stash apply"),
]

print("\n{:<35} -> {}".format("Task", "Command"))
print("-" * 70)
for task, cmd in commands:
    print("{:<35} -> {}".format(task, cmd))

print("\n" + "="*70)
print("END OF HANDOUT #16")
print("="*70)