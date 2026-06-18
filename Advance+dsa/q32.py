numbers = [1, 2, 3, 2, 4, 2, 5, 3, 3, 3]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
most_frequent = None

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        most_frequent = key

print("Most Frequent Element:", most_frequent)