history = []
print("\nAdvanced Calculator | Type \"history\" or \"q\"\n")


while True:
    user_input = input(">> ").strip()
    if user_input == "q":
        print("Exiting..."); break
    if user_input == "history":
        print("\n--- Calculation History ---")
        for i, h in enumerate(history, 1):
            print(f"  {i}. {h}")
        continue
    try:
        result = eval(user_input)
        history.append(f"{user_input} = {result}")
        print(f"  = {result}")
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero!")
    except Exception as e:
        print(f"  Error: {e}")

