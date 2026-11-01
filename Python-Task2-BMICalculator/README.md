# BMI Calculator

This is a small command-line BMI calculator written in Python. Enter your weight in kilograms and your height in metres or centimetres, and the program calculates your BMI and prints a category.

## Features

- Accepts height in metres (for example, `1.70`) or centimetres (for example, `170`).
- Checks input and asks again if a value is invalid.
- Displays BMI rounded to two decimal places.
- Shows a category based on the BMI ranges used in this project.

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

## Example

```text
BMI Calculator
Enter your weight in kilograms: 68
Enter your height (metres, e.g. 1.70, or centimetres, e.g. 170): 170

Your BMI is 23.53.
Category: Normal
BMI is a general screening measure, not a medical diagnosis.
```

Your result will depend on the values you enter.

## Formula

```text
BMI = weight in kilograms / (height in metres × height in metres)
```

The program uses these categories:

- Underweight: BMI below 18.5
- Normal: BMI from 18.5 to below 25
- Overweight: BMI from 25 to below 30
- Obese: BMI of 30 or higher

## What this project helped me practise

- Writing and calling Python functions
- Validating user input
- Using `if` statements to classify a result
- Formatting a number for display

## Note

This is a basic educational calculator. BMI is a general screening measure and does not account for every factor related to a person's health.
