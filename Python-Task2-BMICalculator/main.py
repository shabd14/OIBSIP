"""Calculate BMI from weight in kilograms and height in metres."""

import math


def read_positive_number(prompt):
    """Keep asking until the user enters a finite number greater than zero."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Please enter a number, such as 68.5.")
            continue

        if not math.isfinite(value) or value <= 0:
            print("Please enter a number greater than zero.")
            continue

        return value


def read_height_metres():
    """Accept either metres (1.70) or centimetres (170) and return metres."""
    while True:
        raw_value = input(
            "Enter your height (metres, e.g. 1.70, or centimetres, e.g. 170): "
        ).strip()
        try:
            height = float(raw_value)
        except ValueError:
            print("Please enter a number, such as 1.70 or 170.")
            continue

        if not math.isfinite(height):
            print("Please enter a finite height value.")
            continue

        if 0.5 <= height <= 3:
            return height
        if 50 <= height <= 250:
            return height / 100

        print("Enter height in metres (0.5 to 3) or centimetres (50 to 250).")


def classify_bmi(bmi):
    """Return the category specified in the internship task checklist."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    print("BMI Calculator")
    weight_kg = read_positive_number("Enter your weight in kilograms: ")
    height_m = read_height_metres()

    bmi = weight_kg / (height_m ** 2)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is {bmi:.2f}.")
    print(f"Category: {category}")
    print("BMI is a general screening measure, not a medical diagnosis.")


if __name__ == "__main__":
    main()

