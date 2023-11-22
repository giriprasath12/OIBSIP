def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        return "Invalid input. Please enter numeric values for weight and height."
    if weight <= 0 or height <= 0:
        return "Weight and height must be positive values."
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    if isinstance(bmi, float):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    else:
        return bmi


def main():
    weight = input("Enter your weight in kilograms: ")
    height = input("Enter your height in meters: ")

    result = calculate_bmi(weight, height)

    interpretation = interpret_bmi(result)
    print(f"Result: {interpretation}")


if __name__ == "__main__":
    main()
