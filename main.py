import tkinter as tk
import random

def start_game():
    global num, lives
    num = random.randint(1,100)
    print(num)
    lives = 5
    game_title.config(text="Guess a number from 1 to 100:")
    guess_entry.pack(pady=10)
    guess_button.pack(pady=10)
    play_button.pack_forget()

def check_guess():
    pass


# GUI structure 
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("550x550")

# Frame to group the title and button together
frame = tk.Frame(root)
frame.pack(pady=180)  

# GUI display when code is run
game_title = tk.Label(frame, text="Welcome to Number Guessing Game!", font=('Helvetica', 18))
game_title.pack(pady=20) 
play_button = tk.Button(frame, text="Play Game", font=('Helvetica', 14), command=start_game)
play_button.pack(pady=10)  
guess_entry = tk.Entry(frame, font=('Helvetica', 14))
guess_button = tk.Button(frame, text="Submit Guess", font=('Helvetica', 14), command=check_guess)

root.mainloop()
