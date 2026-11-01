# Random Password Generator

A beginner-tier command-line password generator with choices for uppercase letters, lowercase letters, numbers, and symbols. It uses `secrets` rather than `random` so the generated passwords use a security-focused random source.

## Features

- Requires a password length of at least 8 characters.
- Requires at least two selected character types.
- Guarantees at least one character from every selected type.
- Uses Python's `secrets` module for secure random selection and shuffling.
- Can generate another password without restarting.
- Does not save generated passwords to disk.

## Run it

Python 3 is required. The program uses only Python's standard library:

```powershell
python main.py
```

Choose `y` or `n` for each character type. Keep any generated password private and do not include real passwords in screenshots or demo recordings.

