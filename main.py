import tkinter as tk

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
play_button = tk.Button(frame, text="Play Game", font=('Helvetica', 14))  # command=start_game)
play_button.pack(pady=10)  

root.mainloop()
