# BMI Calculator Project

Two complete implementations — beginner CLI and advanced GUI.

---

## Files

| File | Description |
|------|-------------|
| `bmi_cli.py` | Beginner-friendly Python command-line version |
| `bmi_advanced.html` | Full-featured advanced web app (no install needed) |

---

## bmi_cli.py — Command Line (Python)

### Requirements
- Python 3.6 or higher
- No external libraries needed

### Run
```bash
python bmi_cli.py
```

### Features
- Metric (kg / m) and Imperial (lbs / ft+in) support
- Input validation with helpful error messages
- BMI classification into 4 categories
- ASCII visual scale with pointer
- Ideal weight range display
- WHO reference table printed on each result
- Loop to calculate multiple times

---

## bmi_advanced.html — Web App

### How to open
Just double-click the file, or open it in any modern browser:
```
File → Open → bmi_advanced.html
```
No server, no install, no dependencies — works completely offline.

### Features
- **Calculator tab** — Metric & Imperial, input validation, animated BMI scale pointer, health advice
- **History tab** — Save entries with name/date, delete individual rows, clear all
- **Trends tab** — Stats (latest, average, min, max), Chart.js line graph with healthy range bands
- **Reference tab** — WHO BMI categories table, formula explanation
- **Dark mode** — Automatically follows system theme
- **Local storage** — History persists across browser sessions

---

## BMI Formula

```
BMI = weight (kg) / height (m)²
```

| Category       | BMI Range   |
|----------------|-------------|
| Underweight    | < 18.5      |
| Normal weight  | 18.5 – 24.9 |
| Overweight     | 25.0 – 29.9 |
| Obese          | ≥ 30.0      |

---

> **Disclaimer**: BMI is a screening tool, not a diagnostic measure. Consult a healthcare professional for personalised advice.