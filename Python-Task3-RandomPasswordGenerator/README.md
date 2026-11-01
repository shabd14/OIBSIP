# Random Password Generator

A command line python script which generates a password based on character types selected by the user. Uses python's built-in secrets library to generate random selections.

## Features

- User can select uppercase, lowercase, numbers and symbols.

- Password must have minimum 8 characters.

- At least 2 character types must be selected.

- At least 1 character from each selected character type.

- Can generate a new password without having to restart the program.

- Does not save passwords to a file.

## Requirements

- Python 3

- No external libraries.

## How to Run

On terminal in this directory run:

```bash

python main.py

```

or if your system uses python3:

```bash

python3 main.py

```

You will be prompted to answer each question with either y or n.

## How it works

A list is created based on your selected character types. The script will then randomly select 1 character from each type selected. The rest of the characters are selected from the full set of characters and then shuffled.

Python's secrets module is used instead of a general random module. This is because the secrets module is specifically for generating secure random values.

## What I Have Practised

- String manipulation and character sets.

- Loops and functions.

- Input validation.

- Using an imported built-in module.

## Security Note

The password will be displayed on the terminal so try not to take any screenshots or record any videos which show the password you plan to use. For important accounts, use a trusted password manager and take heed to the security advise given by the service.
