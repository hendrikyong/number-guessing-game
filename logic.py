import random
num = random.randint(1, 100)
lives = 5
print(f"You have {lives} lives.")
game_on = True

while game_on:
    try:
        guess = int(input("Guess a number between 1 and 100 (or enter 0 to quit): "))
        
        if guess == 0:
            print("Goodbye!")
            break
        
        if guess < 1 or guess > 100:
            print("Please guess a number within the range 1 to 100.")
            continue

        if guess < num:
            print("Too low, Guess Higher.")
        elif guess > num:
            print("Too high, Guess Lower.")
        else:
            print(f"Congratulations! You got it right! The number is {num}.")
            break

        lives -= 1
        if lives == 0:
            print(f"Sorry, you've run out of lives. The number was {num}.")
            break
        else:
            print(f"Lives remaining: {lives}")
    except ValueError:
        print("Invalid input. Please enter a number.")


