# OIBSIP – Python Programming Internship

This repository contains three Python projects completed as part of my Python programming internship tasks with Oasis Infobyte. I used these projects to practise writing small programs, handling user input, working with Python's standard library, and understanding basic client-server communication.

## Projects

### 1. BMI Calculator
A command-line program that calculates Body Mass Index (BMI) from weight and height. It accepts height in metres or centimetres, checks invalid input, and displays a BMI category.

**Concepts practised:** functions, input validation, numeric calculations, conditional statements.

[Open project folder](Python-Task2-BMICalculator/)

### 2. Random Password Generator
A command-line tool that generates passwords based on the character types selected by the user. It uses Python's `secrets` module for random selection.

**Concepts practised:** strings, loops, functions, user choices, Python's `secrets` module.

[Open project folder](Python-Task3-RandomPasswordGenerator/)

### 3. Chat Application
A simple command-line chat application for multiple clients on the same computer. It uses sockets to exchange messages and threads to handle sending and receiving at the same time.

**Concepts practised:** sockets, threads, client-server communication, exception handling.

[Open project folder](Python-Task5-ChatApplication/)

## Technologies

- Python 3
- Python standard library
- Sockets and threading (Chat Application)

No third-party packages are required for these projects.

## Repository structure

```text
OIBSIP/
├── README.md
├── Python-Task2-BMICalculator/
│   ├── README.md
│   └── main.py
├── Python-Task3-RandomPasswordGenerator/
│   ├── README.md
│   └── main.py
└── Python-Task5-ChatApplication/
    ├── README.md
    ├── client.py
    └── server.py
```

## Running the projects

1. Install Python 3 if it is not already installed.
2. Clone or download this repository.
3. Open a terminal in the folder for the project you want to run.
4. Follow the run instructions in that project's README.

For example, to run the BMI Calculator from its folder:

```bash
python main.py
```

On some systems, you may need to use `python3` instead of `python`.

## What I practised

While working on these tasks, I practised breaking a program into functions, validating user input, using built-in Python modules, and writing instructions so another person can run the code. The chat project also gave me practice with sockets and threads.

## Notes

- The BMI Calculator is an educational example, not a medical diagnosis.
- The password generator displays passwords in the terminal. Keep generated passwords private.
- The Chat Application is configured for `127.0.0.1` and is intended for local testing. Messages are not encrypted.

## Acknowledgement

These projects were completed as part of my Python programming internship tasks with Oasis Infobyte.

---
If you try one of the projects and notice an issue, feel free to open an issue with steps to reproduce it.
