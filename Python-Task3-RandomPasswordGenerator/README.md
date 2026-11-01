# Random Password Generator

This command-line Python program creates a password using the character types selected by the user. It uses the standard-library `secrets` module for random selection.

## Features

- Lets the user choose uppercase letters, lowercase letters, numbers, and symbols.
- Requires a password length of at least 8 characters.
- Requires at least two character types to be selected.
- Includes at least one character from each selected type.
- Allows the user to generate another password without restarting the program.
- Does not write generated passwords to a file.

## Requirements

- Python 3
- No third-party packages

## Run the program

Open a terminal in this folder and run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

Follow the prompts and enter `y` or `n` for each character type.

## How it works

The program builds a list of the character groups you selected. It first chooses one character from each selected group, fills the remaining length from the combined set, and shuffles the result.

The program uses Python's `secrets` module rather than the general-purpose `random` module because `secrets` is intended for security-sensitive random values.

## What this project helped me practise

- Working with strings and character groups
- Using loops and functions
- Validating user choices
- Importing and using a standard-library module

## Safety note

The generated password is shown in the terminal, so avoid sharing screenshots or recordings that reveal a password you intend to use. For important accounts, use a trusted password manager and follow the service's security recommendations.
