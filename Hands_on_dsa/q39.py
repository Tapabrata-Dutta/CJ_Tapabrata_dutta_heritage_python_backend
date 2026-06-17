logs = ["INFO", "ERROR", "WARNING", "ERROR", "INFO", "ERROR"]

count = 0

for i in logs:
    if i == "ERROR":
        count += 1

print("ERROR appears", count, "times")