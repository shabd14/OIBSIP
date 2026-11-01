# OIBSIP - Python Programming Internship

The content in this repository contains 3 Python projects that I completed as part of my internship tasks during my Python Programming Internship at Oasis Infobyte. I was able to practice creating short programs, taking user input, utilizing the standard library and learning about client-server interactions.

## Projects

### BMI Calculator

A command line program that allows the user to calculate their BMI using their weight and height. The user can enter their height in either meters or centimeters. The program also handles any invalid inputs and outputs the category of BMI they fall into.

Skills practiced: functions, validation, mathematical calculations, conditions.

[View Project Folder](Python-Task2-BMICalculator/)

### Random Password Generator

A command line program that will generate a password based on the characters chosen by the user. The program uses the secrets module from Python to generate a random selection.

Skills practiced: strings, loops, functions, user selections, secrets module.

[View Project Folder](Python-Task3-RandomPasswordGenerator/)

### Chat Application

A simple chat application that allows multiple clients to communicate within the same computer. The application uses sockets to send messages between clients and threading to allow sending and receiving messages simultaneously.

Skills practiced: sockets, threading, client-server interaction, exceptions.

[View Project Folder](Python-Task5-ChatApplication/)

## Technologies Used

- Python 3

- Standard Library

- Sockets & Threading (Chat Application)

No third party packages are required.

## Project Structure

```

OIBSIP/

├── README.md

├── Python-Task2-BMICalculator/

│  ├── README.md

│  └── main.py

├── Python-Task3-RandomPasswordGenerator/

│  ├── README.md

│  └── main.py

└── Python-Task5-ChatApplication/

├── README.md

├── client.py

└── server.py

```

## How to Run Projects

1. Download Python 3

2. Clone or download the repository

3. Navigate to the folder of the project you wish to run in your terminal

4. Follow the instructions in the Readme file

For example, to run the BMI Calculator:

```

python main.py

```

Depending on your system you may need to use python3.

## Skills Practiced

I was able to practice splitting the program into functions, validating user input, using standard libraries in Python and providing clear instructions to allow someone else to run the code. I also practiced using sockets and threading when creating the chat application.

## Notes

- BMI Calculator is for learning purposes only and should not be taken as a medical diagnosis.

- The password generator will show passwords in the terminal. Keep generated passwords private.

- Chat Application has been set to 127.0.0.1 and is for local testing only. Messages are not encrypted.

## Acknowledgements

These projects have been completed as part of my internship tasks during my Python Programming Internship at Oasis Infobyte.

---

If you try out any of the projects and encounter any issues, please feel free to raise an issue with steps to replicate.
