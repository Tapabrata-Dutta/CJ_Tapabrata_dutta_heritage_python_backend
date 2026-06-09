name   = input("Your name         : ")
age    = int(input("Age               : "))
gender = input("Gender (M/F)       : ").upper()
weight = float(input("Weight (kg)       : "))
height = float(input("Height (cm)       : "))


h_m  = height / 100                  # convert cm to metres
bmi  = weight / (h_m ** 2)


ideal_min = 18.5 * (h_m ** 2)
ideal_max = 24.9 * (h_m ** 2)


if bmi < 18.5:
    cat, emoji = "Underweight", "⚠️"
elif bmi < 25:
    cat, emoji = "Normal Weight", "✅"
elif bmi < 30:
    cat, emoji = "Overweight", "⚠️"
else:
    cat, emoji = "Obese", "🔴"


# Visual BMI bar
filled = int(min(bmi / 40 * 20, 20))
bar    = "█" * filled + "░" * (20 - filled)


print(f"""
╔══════════════════════════════════╗
║        BMI HEALTH REPORT         ║
╠══════════════════════════════════╣
║ Name    : {name:<24}║
║ Age     : {age:<24}║
║ Gender  : {gender:<24}║
╠══════════════════════════════════╣
║ BMI     : {bmi:<24.2f}║
║ Status  : {emoji} {cat:<21}║
║ Bar     : [{bar}]  ║
║ Ideal   : {ideal_min:.1f} kg — {ideal_max:.1f} kg           ║
╚══════════════════════════════════╝
""")
