# BMI Calculator

A beginner-tier command-line BMI calculator written in Python. It asks for weight in kilograms and accepts height in either metres or centimetres, then prints the BMI to two decimal places and the category from the task checklist.

## Run it

Python 3 is required. From this folder, run:

```powershell
python main.py
```

Enter weight in kilograms. For height, enter either metres (for example, `1.70`) or centimetres (for example, `170`). The program converts centimetres to metres before calculating. If an entry is invalid, it explains the problem and asks again.

## Formula and categories

`BMI = weight_kg / (height_m * height_m)`

- Underweight: BMI below 18.5
- Normal: BMI from 18.5 up to (but not including) 25
- Overweight: BMI from 25 up to (but not including) 30
- Obese: BMI 30 or higher

This is a simple educational calculator. BMI is a general screening measure and is not a medical diagnosis.

