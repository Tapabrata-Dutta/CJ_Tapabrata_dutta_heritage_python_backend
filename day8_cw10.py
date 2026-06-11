import random


secret = random.randint(1, 100)
guess = 0
attempts = 0


print('🎮 Number Guessing Game (1 to 100)')


while guess != secret:
    guess = int(input('Your guess: '))
    attempts += 1
    if guess < secret:
        print('📈 Too low!')
    elif guess > secret:
        print('📉 Too high!')
    else:
        print(f'🎉 Correct! Found in {attempts} attempts!')
