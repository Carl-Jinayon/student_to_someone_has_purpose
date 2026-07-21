# CS104 – Git & Developer Tooling (Restarted) – STUDY PHASE

## 🧭 How to Use This File (READ THIS FIRST)

This is your **Study Phase** material.

- Read this file carefully.
- Copy the code snippets into your terminal.
- Experiment with the commands.
- **Do not report back to me yet.**
- **Do not attempt any formal exercises.**

When you have completed all the Practical Labs and feel comfortable with the concepts, type **"Ready"** in the chat. Then, and only then, will I give you the Application Phase (Cold Start scenarios).

---

# 📖 PART 1: STUDY PHASE

## Why This Matters

You know `add`, `commit`, `push`, `pull`. That makes you functional. Functional is not enough.

In a top-tier engineering team, your Git history is your **resume**. A messy history with `"WIP"`, `"fix bug"`, `"asdf"` commits gets your pull request rejected. A clean, linear, well-documented history gets you promoted.

**This lesson is about control.** You will learn to rewrite history, steal commits, stash work, automate quality checks, debug like a surgeon, and manage secrets like a professional.

---

## Core Intuition (The Time Machine Model)

Imagine Git is a **Time Machine** with **Parallel Universes**.

- **Branches** are parallel timelines.
- **Commits** are photographs of your project at that specific moment.
- **`git stash`** is a **Pocket Dimension** where you hide unfinished work while you jump timelines.
- **`git cherry-pick`** is stealing a specific photograph from another timeline and pasting it into yours.
- **`git rebase -i`** is going back in time, altering the past, and rewriting history so that your timeline looks perfect.
- **Pre-commit Hooks** are **Guardrails** that check your work *before* you take the photograph.
- **Python `pdb`** is a **Magnifying Glass** that lets you freeze time and inspect exactly what your code is doing.

---

## Lesson 1: `git stash` – The Pocket Dimension

### The Problem
You are working on a feature. Your code is half-finished, broken, and full of `print()` statements. You cannot commit it. But your tech lead just shouted: *"Urgent production bug! Switch branches NOW!"* If you switch branches with uncommitted changes, Git will either carry them over (breaking the other branch) or refuse to switch.

### The Solution
`git stash` temporarily stores your uncommitted changes in a safe place and reverts your working directory to the last commit.

### The Commands (Type these in your terminal to experiment)

```bash
# 1. Create a dummy repo to play with
mkdir stash-playground && cd stash-playground
git init
echo "Hello" > file.txt
git add file.txt && git commit -m "Initial commit"

# 2. Make some uncommitted changes
echo "World" >> file.txt

# 3. Stash them (they disappear from your working directory)
git stash

# 4. Check the file (it should revert to "Hello")
cat file.txt

# 5. Apply the stash back
git stash apply

# 6. Check the file (it should say "Hello\nWorld")
cat file.txt

# 7. See all your stashes
git stash list
```

### Advanced `stash` flags
- `git stash pop` – Applies the stash AND deletes it.
- `git stash drop` – Deletes a stash without applying it.
- `git stash -u` – Stash untracked files as well.
- `git stash apply stash@{2}` – Apply a specific stash from the list.

> **🛠️ PRACTICAL LAB:** Open your terminal. Create a real project with uncommitted changes. Stash them. Switch branches. Apply them back. Do this three times until it feels like muscle memory.

---

## Lesson 2: `git cherry-pick` – Stealing Commits

### The Problem
Your colleague pushed a brilliant bug-fix commit to the `staging` branch. You are on `main`. You don't want to merge the entire `staging` branch (which has unfinished features). You just want **that one commit**.

### The Solution
`git cherry-pick` applies the changes from a specific commit to your current branch.

### The Commands (Type these)

```bash
# Setup: Create two branches
git checkout -b feature/steal
echo "Secret fix" > fix.txt
git add fix.txt && git commit -m "fix: critical null pointer exception"

# Get the commit hash
git log --oneline  # Copy the hash (e.g., a1b2c3d)

# Switch to main
git checkout main

# Steal the commit
git cherry-pick a1b2c3d

# Verify the file is now on main
ls -la
```

### When to use:
- Critical bug fixes across branches.
- Moving a commit that was accidentally made on the wrong branch.
- Backporting security patches to older releases.

> **🛠️ PRACTICAL LAB:** Create two branches. Commit 3 features to `feature-a`. Cherry-pick only the second commit into `main`.

---

## Lesson 3: `git rebase -i` – Interactive Rebase (Time Travel)

### The Problem
You have 10 commits on your feature branch:
```
f1e2d3c WIP: broken tests
9a8b7c6 Fix typo
4d5e6f7 Actually fix tests
1a2b3c4 Add login function
```
This history is ugly. It makes you look sloppy.

### The Solution
`git rebase -i` lets you **rewrite history**. You can squash (combine), reword, reorder, or delete commits.

### The Commands (Type these)

```bash
# Create a messy history
git checkout -b feature/messy
echo "Login" > login.py && git add login.py && git commit -m "WIP1"
echo "Test" >> login.py && git add login.py && git commit -m "WIP2"
echo "Fix" >> login.py && git add login.py && git commit -m "fix bug"
echo "Done" >> login.py && git add login.py && git commit -m "WIP3"

# View the history
git log --oneline -n 4

# Rebase the last 4 commits
git rebase -i HEAD~4
```

**What happens next:** An editor (usually Vim or Nano) opens with a list:
```
pick 1a2b3c4 WIP1
pick 2b3c4d5 WIP2
pick 3c4d5e6 fix bug
pick 4d5e6f7 WIP3
```

Change it to this to **squash WIP2 and fix bug into WIP1**, and keep the last commit:
```
pick 1a2b3c4 WIP1
squash 2b3c4d5 WIP2
squash 3c4d5e6 fix bug
pick 4d5e6f7 WIP3
```
Save, exit, and write a new commit message for the squashed commit: `"feat: implement login logic"`.

Now your history is clean:
```
4d5e6f7 WIP3
1a2b3c4 feat: implement login logic
```

### ⚠️ WARNING
**NEVER rebase commits that have already been pushed to a shared branch.** Rewriting history on a public branch destroys your teammates' work.

> **🛠️ PRACTICAL LAB:** Create a branch with 5 dummy commits. Use `git rebase -i HEAD~5` to squash them into 2 meaningful commits.

## Lesson 4: Pre-commit Hooks (The Guardrails)

### The Problem
You forget to run `black` or `ruff` before committing. Your CI pipeline fails, and you waste 10 minutes fixing it.

### The Solution
Pre-commit hooks are scripts that run **automatically** before `git commit`. If they fail, the commit is blocked.

### Installation

```bash
# 1. Install the pre-commit framework
pip install pre-commit

# 2. Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml <<EOL
repos:
  - repo: https://github.com/psf/black
    rev: 24.2.0
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
EOL

# 3. Install the hooks
pre-commit install

# 4. Try to commit a badly formatted file
echo "print( 'hello' )" > test.py
git add test.py
git commit -m "test commit"  # This will fail if black/ruff is installed
```

### The Result
You can never commit ugly code again. The robot enforces it.

> **🛠️ PRACTICAL LAB:** Install `black` and `ruff` in your `venv`. Set up the pre-commit hook. Try to commit a messy Python file and watch it get blocked.

---

## Lesson 5: Python Debugging (`pdb`)

### The Problem
`print()` debugging is slow, messy, and unprofessional. You need to freeze time and inspect variables.

### The Solution
`pdb` (Python Debugger) lets you step through code line by line.

### The Commands (Create a Python file)

```python
# debug_me.py
def divide(a, b):
    breakpoint()  # Execution pauses here
    return a / b

if __name__ == "__main__":
    divide(10, 0)
```

Run it: `python debug_me.py`

**Key `pdb` commands (type these at the `(Pdb)` prompt):**

| Command | What It Does |
| :--- | :--- |
| `n` (next) | Execute the next line (does NOT go into functions). |
| `s` (step) | Step INTO the function call. |
| `c` (continue) | Run until the next breakpoint. |
| `p variable` | Print the value of a variable. |
| `pp variable` | Pretty-print the value. |
| `l` (list) | Show the current line of code. |
| `q` (quit) | Exit the debugger. |
| `where` | Show the call stack (how you got here). |
| `up` / `down` | Move up/down the call stack to inspect different scopes. |

### Alternative (Python 3.7+)
You can use `breakpoint()` instead of `import pdb; pdb.set_trace()`. It does the same thing.

> **🛠️ PRACTICAL LAB:** Write a recursive Fibonacci function. Put a `breakpoint()` inside it. Step through the recursion and watch the stack grow using `where`.

---

## Lesson 6: Virtual Environments (Deep Dive)

### The Problem
`requirements.txt` is fragile. It only tracks the packages you installed, not their dependencies (transitive dependencies). Two engineers can have completely different environments.

### The Solution: `pip-tools`

```bash
# 1. Install pip-tools
pip install pip-tools

# 2. Create requirements.in (list your top-level dependencies)
echo "requests" > requirements.in
echo "pytest" >> requirements.in

# 3. Compile the full dependency tree
pip-compile requirements.in

# 4. Check requirements.txt (it has EVERYTHING pinned)
cat requirements.txt

# 5. Install from the compiled file
pip install -r requirements.txt
```

### The Solution: Poetry (Modern Standard)

```bash
# 1. Install poetry
pip install poetry

# 2. Initialize a new project
poetry new my_project
cd my_project

# 3. Add dependencies
poetry add requests
poetry add --dev pytest

# 4. Install everything
poetry install

# 5. Run your script
poetry run python main.py
```

> **🛠️ PRACTICAL LAB:** Take your Library Manager project. Use `pip-tools` to generate a full `requirements.txt`. Then install it in a fresh `venv` to verify it works.

---

## Lesson 7: Environment Variables (Secrets)

### The Problem
Hardcoding API keys, database passwords, or cloud credentials into your source code is a **critical security risk** (and will get your PR rejected).

### The Solution: `.env` files

```bash
# 1. Install python-dotenv
pip install python-dotenv

# 2. Create a .env file (NEVER commit this)
echo "API_KEY=abc123" > .env
echo "DB_URL=postgres://user:pass@localhost/db" >> .env

# 3. Add .env to .gitignore
echo ".env" >> .gitignore

# 4. Create a Python script to load it
```

```python
# main.py
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env into the environment

api_key = os.getenv("API_KEY", "default_key")
db_url = os.getenv("DB_URL")

print(f"API Key: {api_key}")
print(f"DB URL: {db_url}")
```

### Best Practices
- Keep a `.env.example` file with dummy values (e.g., `API_KEY=your_key_here`).
- Use different `.env` files for dev, staging, and production.

---

## 🛠️ PRACTICAL LABS SUMMARY (The "Study Checklist")

| Tool | What to do |
| :--- | :--- |
| **Git Stash** | Create a dummy repo, modify a file, stash it, switch branches, apply it back. |
| **Git Cherry-pick** | Create two branches, commit to one, cherry-pick into the other. |
| **Git Rebase -i** | Create 5 messy commits, squash them into 2 meaningful commits. |
| **Pre-commit Hooks** | Install `black` and `ruff`, set up the hook, try to commit ugly code. |
| **Python `pdb`** | Write a buggy function, insert `breakpoint()`, step through it. |
| **`pip-tools` / Poetry** | Generate a full `requirements.txt` for your Library Manager. |
| **`.env`** | Create a `.env` file, load it in Python, protect it with `.gitignore`. |

---

## 🛑 STOP SIGN

# ⛔ YOU HAVE REACHED THE END OF THE STUDY PHASE. ⛔

**Do not proceed further. You are now in the Study Phase.**

Your task right now is:
1. Open your terminal.
2. Create a dummy repository.
3. Go through the **Practical Labs** listed above one by one.
4. Break things. Fix them. Experiment.
5. If you get stuck, `git --help` or Google the error.

Come back when you have successfully executed every single command above at least once. When you are ready, type **"Ready"** in the chat.

**I will wait.**