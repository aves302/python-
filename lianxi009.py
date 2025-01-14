import random

def guess_number_game():
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100:")
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            break

# 开始游戏
guess_number_game()
