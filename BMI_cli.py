"""
BMI Calculator - Command Line Version
======================================
Beginner-friendly Python script.
Run: python bmi_cli.py
"""


def get_float_input(prompt, min_val, max_val):
    """Prompt user for a float within a valid range, with error handling."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"  ⚠  Please enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("  ⚠  Invalid input. Please enter a number.")


def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """Classify BMI into WHO categories."""
    if bmi < 18.5:
        return "Underweight", "Consider consulting a nutritionist for a balanced diet plan."
    elif bmi < 25.0:
        return "Normal weight", "Great! Maintain your healthy lifestyle with balanced diet and exercise."
    elif bmi < 30.0:
        return "Overweight", "Consider moderate exercise and a balanced diet to reach a healthy weight."
    else:
        return "Obese", "Please consult a healthcare professional for personalised guidance."


def get_ideal_weight_range(height_m):
    """Return the healthy BMI weight range for a given height."""
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return min_weight, max_weight


def print_bmi_bar(bmi):
    """Print a simple ASCII BMI scale with a marker."""
    bar = "[----Underweight----|--Normal--|--Overweight--|-----Obese-----]"
    # Map BMI (10–40) to bar positions (0–62)
    pos = int(min(62, max(0, (bmi - 10) / 30 * 62)))
    marker = " " * pos + "^"
    print(f"\n  {bar}")
    print(f"  {marker}")
    print(f"  10   15   18.5       25       30                    40+\n")


def choose_unit():
    """Let user pick metric or imperial."""
    print("\n  Choose unit system:")
    print("  [1] Metric   (kg, meters)")
    print("  [2] Imperial (lbs, feet & inches)")
    while True:
        choice = input("\n  Enter 1 or 2: ").strip()
        if choice in ("1", "2"):
            return choice
        print("  ⚠  Please enter 1 or 2.")


def get_metric_inputs():
    """Collect weight in kg and height in meters."""
    weight_kg = get_float_input("  Weight (kg)   : ", 10, 500)
    height_m = get_float_input("  Height (m)    : ", 0.5, 2.7)
    return weight_kg, height_m


def get_imperial_inputs():
    """Collect weight in lbs and height in feet+inches, convert to metric."""
    weight_lb = get_float_input("  Weight (lbs)  : ", 22, 1100)
    feet = get_float_input("  Height (feet) : ", 1, 9)
    inches = get_float_input("  Height (inches, 0-11): ", 0, 11)
    weight_kg = weight_lb * 0.453592
    height_m = (feet * 12 + inches) * 0.0254
    return weight_kg, height_m


def run_calculator():
    """Main calculator loop."""
    print("\n" + "=" * 55)
    print("           BMI CALCULATOR — Health Tracker")
    print("=" * 55)

    while True:
        unit_choice = choose_unit()

        print()
        if unit_choice == "1":
            weight_kg, height_m = get_metric_inputs()
        else:
            weight_kg, height_m = get_imperial_inputs()

        bmi = calculate_bmi(weight_kg, height_m)
        category, advice = classify_bmi(bmi)
        ideal_min, ideal_max = get_ideal_weight_range(height_m)

        print("\n" + "-" * 55)
        print(f"  BMI Score    : {bmi:.1f}")
        print(f"  Category     : {category}")
        print(f"  Ideal weight : {ideal_min:.1f} kg – {ideal_max:.1f} kg  "f"({ideal_min / 0.453592:.0f}–{ideal_max / 0.453592:.0f} lbs)")
        print(f"\n  {advice}")
        print_bmi_bar(bmi)

        # BMI Categories reference
        print("  BMI Categories (WHO standard):")
        print("  ┌─────────────────────┬───────────────┐")
        print("  │ Category            │ BMI Range     │")
        print("  ├─────────────────────┼───────────────┤")
        print("  │ Underweight         │ < 18.5        │")
        print("  │ Normal weight       │ 18.5 – 24.9   │")
        print("  │ Overweight          │ 25.0 – 29.9   │")
        print("  │ Obese               │ ≥ 30.0        │")
        print("  └─────────────────────┴───────────────┘")

        print("\n" + "-" * 55)
        again = input("  Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Stay healthy! Goodbye. 👋\n")
            break


if __name__ == "__main__":
    run_calculator()
