import random

chosen_number = random.choice(list(range(1, 11)))
guessed_numbers = []
attempts = 0
max_attempts = 5

while attempts < max_attempts:
  guess_number = int(input('Enter any number from 1 to 10: '))
  if guess_number in guessed_numbers:
    print(f'{guess_number} is already guessed. Try another number')
    continue

  guessed_numbers.append(guess_number)

  attempts += 1

  if guess_number < chosen_number:
    print(f'{guess_number} is too low. Guess a higher number')
  elif guess_number > chosen_number:
    print(f'{guess_number} is too high. Guess a lower number')
  else:
    print('Your guess is correct. You win!!')
    break

  if attempts == max_attempts:
    print(f'Game over. The number chosen was {chosen_number}.')
