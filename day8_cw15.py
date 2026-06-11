temperatures = [22.5, -1.0, 30.2, -999, 18.7, 25.0, -5.0]


valid_readings = []
for temp in temperatures:
    if temp < 0:
        print(f'⚠️  Skipping invalid reading: {temp}')
        continue   # Skip rest, go to next temp
    valid_readings.append(temp)
    print(f'✅ Recorded: {temp}°C')


avg = sum(valid_readings) / len(valid_readings)
print(f'\nAverage temperature: {avg:.1f}°C')
