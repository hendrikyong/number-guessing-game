import tkinter as tk
import random

def start_game():
    global num, lives
    num = random.randint(1,100)
    lives = 5
    game_title.config(text="Guess a number from 1 to 100:")
    guess_entry.pack(pady=10)
    guess_button.pack(pady=10)
    play_button.pack_forget()

def check_guess():
    global lives
    try:
        guess = int(guess_entry.get())

        if guess < 1 or guess > 100:
            game_title.config(text="Please guess a number within the range 1 to 100.")
        elif guess < num:
            lives -= 1
            if lives > 0:
                game_title.config(text=f"Too low! Guess Higher. Lives remaining: {lives}")
            else:
                game_title.config(text=f"You've run out of lives. The number was {num}.")
                guess_button.config(state="disabled")
        elif guess > num:
            lives -= 1
            if lives > 0:
                game_title.config(text=f"Too high! Guess Lower. Lives remaining: {lives}")
            else:
                game_title.config(text=f"You run out of lives. The number was {num}.")
                guess_button.config(state="disabled")
        else:
            game_title.config(text=f"You got it right! The number is {num}.")
            guess_button.config(state="disabled")
    except ValueError:
        game_title.config(text="Invalid input. Please enter a number.")

# GUI structure 
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("550x550")

# Frame to group the title and button together
frame = tk.Frame(root)
frame.pack(pady=180)  

# GUI displays and buttons
game_title = tk.Label(frame, text="Welcome to Number Guessing Game!", font=('Helvetica', 18))
game_title.pack(pady=20) 
play_button = tk.Button(frame, text="Play Game", font=('Helvetica', 14), command=start_game)
play_button.pack(pady=10)  
guess_entry = tk.Entry(frame, font=('Helvetica', 14))
guess_button = tk.Button(frame, text="Submit Guess", font=('Helvetica', 14), command=check_guess)

root.mainloop()
