word = 'Python'
vowels = 0


for char in word:
    if char in 'aeiouAEIOU':
        vowels += 1
        print(f'Vowel found: {char}')


print('Total vowels:', vowels)
