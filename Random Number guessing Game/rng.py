import tkinter as tk 
import random
from tkinter import messagebox
from tkinter import simpledialog  # Add this import

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x200")

        self.initUI()

    def initUI(self):
       
        self.label = tk.Label(self.root, text="Enter your name:")
        self.label.pack(pady=10)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play Game", command=self.start_game)
        self.play_button.pack(pady=10)

    def start_game(self):
        name = self.name_entry.get()

        if not name:
            messagebox.showwarning("Warning", "Please enter your name.")
            return

        secret_number = random.randint(1, 100)
        attempts = 0

        messagebox.showinfo("Welcome", f"Hello, {name}! I'm thinking of a number between 1 and 100. Can you guess it within 10 attempts?")

        while attempts < 10:
            guess = self.get_guess()

            if guess is None:
                return

            attempts += 1

            if guess < secret_number:
                messagebox.showinfo("Hint", "Too low! Try again.")
            elif guess > secret_number:
                messagebox.showinfo("Hint", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations", f"Congratulations, {name}! You guessed the number ({secret_number}) in {attempts} attempts.")
                break

        if attempts == 10:
            messagebox.showinfo("Game Over", f"Sorry, {name}, you've used all your attempts. The secret number was {secret_number}.")

        play_again = messagebox.askquestion("Play Again", "Do you want to play again?")

        if play_again == "yes":
            self.name_entry.delete(0, tk.END)
        else:
            self.root.destroy()

    def get_guess(self):
        guess = simpledialog.askinteger("Guess a Number", "Enter your guess (1-100):", parent=self.root, minvalue=1, maxvalue=100)
        return guess

if __name__ == '__main__':
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
