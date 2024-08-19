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
    play_again_button.pack_forget()

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
                end_game()
        elif guess > num:
            lives -= 1
            if lives > 0:
                game_title.config(text=f"Too high! Guess Lower. Lives remaining: {lives}")
            else:
                game_title.config(text=f"You run out of lives. The number was {num}.")
                end_game()
        else:
            game_title.config(text=f"You got it right! The number is {num}.")
            end_game()
    except ValueError:
        game_title.config(text="Invalid input. Please enter a number.")

def end_game():
    guess_entry.pack_forget()
    guess_button.pack_forget()
    play_again_button.pack(pady=10)

def play_again():
    start_game()

def quit_game():
    root.destroy()

# GUI structure 
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("550x550")

# frame to group the title and buttons together
frame = tk.Frame(root)
frame.pack(pady=180, fill=tk.BOTH, expand=True)  

# GUI displays and buttons
game_title = tk.Label(frame, text="Welcome to Number Guessing Game!", font=('Helvetica', 18))
game_title.pack(pady=20) 
play_button = tk.Button(frame, text="Play Game", font=('Helvetica', 14), command=start_game)
play_button.pack(pady=10)  
guess_entry = tk.Entry(frame, font=('Helvetica', 14))
guess_button = tk.Button(frame, text="Submit Guess", font=('Helvetica', 14), command=check_guess)
play_again_button = tk.Button(frame, text="Play Again", font=('Helvetica', 14), command=play_again)
quit_button = tk.Button(root, text="Quit Game", font=('Helvetica', 14), command=quit_game)
quit_button.place(x=500, y=500, anchor=tk.SE)

root.mainloop()
