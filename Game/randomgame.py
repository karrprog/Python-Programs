from random import randint
import sys
#generate a number 1-10
answer = randint(1, 15)
#input from user?

#check that input is a number 1-10
while True:
    try:
        guess = int(input('Guess a number 1-15: '))
        if 0 < guess < 16:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey bozo, I said 1 - 10')
    except ValueError:
        print('Please enter a number')
        continue
#check if number is the right guess. Otherwise ask again