import tkinter as tk
import random


def spawn_button():
    # Create a new button
    button = tk.Button(root, text="Click Me", command=lambda: button_clicked(button))
    
    # Generate random coordinates within the window's dimensions
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 50)
    
    # Place the button at the random coordinates
    button.place(x=x, y=y)


def button_clicked(button):
    # Get the button's coordinates
    x, y = button.winfo_x(), button.winfo_y()
    print(f"Button clicked at ({x}, {y})")
    # Remove the button
    button.destroy()
    spawn_button()

# Create the main window
root = tk.Tk()
root.title("Random Button Spawner")

# Set the window size
root.geometry("1300x1000")

spawn_button()

# Start the main event loop
root.mainloop()