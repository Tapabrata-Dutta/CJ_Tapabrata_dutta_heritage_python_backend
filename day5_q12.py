from datetime import date
# ─── COLLECT USER DATA ──────────────────────
print("\n╔══════════ HEALTH DASHBOARD ══════════╗")
name   = input("  Full Name           : ")
year   = int(input("  Birth Year (YYYY)  : "))
month  = int(input("  Birth Month (1-12) : "))
day    = int(input("  Birth Day   (1-31) : "))
weight = float(input("  Weight in kg       : "))
height = float(input("  Height in cm       : "))


# ─── AGE CALCULATION ────────────────────────
dob   = date(year, month, day)
today = date.today()
age   = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


# ─── BMI CALCULATION ────────────────────────
h_m = height / 100
bmi = weight / (h_m ** 2)
if bmi < 18.5:   bmi_cat = "Underweight"
elif bmi < 25:   bmi_cat = "Normal Weight"
elif bmi < 30:   bmi_cat = "Overweight"
else:            bmi_cat = "Obese"


# ─── HEART RATE ZONE ────────────────────────
max_hr   = 220 - age
hr_zone  = f"{int(max_hr * 0.6)}–{int(max_hr * 0.8)} bpm"


# ─── FINAL REPORT ───────────────────────────
print(f"""
╔═══════════════════════════════════════╗
║       PERSONAL HEALTH DASHBOARD       ║
╠═══════════════════════════════════════╣
║ Name      : {name:<27}║
║ Age       : {age} years                      ║
╠═══════════════════════════════════════╣
║ Weight    : {weight} kg                     ║
║ Height    : {height} cm                     ║
║ BMI       : {bmi:.1f} ({bmi_cat})              ║
╠═══════════════════════════════════════╣
║ Target HR Zone: {hr_zone}              ║
╚═══════════════════════════════════════╝
""")
