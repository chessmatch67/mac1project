import customtkinter as ctk
import tkinter as tk

# Setup window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x300")

# Load images
icon_image = tk.PhotoImage(file="icons8-hamburger-menu-50.png")  # This will be your OptionMenu replacement
option1_image = tk.PhotoImage(file="icons8-hamburger-menu-50.png")
option2_image = tk.PhotoImage(file="icons8-hamburger-menu-50.png")

# Function to open the menu
def open_menu():
    menu.post(image_button.winfo_rootx(), image_button.winfo_rooty() + image_button.winfo_height())

# Create a button with an image (acts like OptionMenu)
image_button = ctk.CTkButton(app, text="", image=icon_image, width=100, height=100, command=open_menu, fg_color="transparent", hover_color="lightgray")
image_button.pack(pady=50)

# Create the menu
menu = tk.Menu(app, tearoff=0)
menu.add_command(label="Option 1", image=option1_image, compound="left", command=lambda: select_option(option1_image))
menu.add_command(label="Option 2", image=option2_image, compound="left", command=lambda: select_option(option2_image))

# Function to change the image on button
def select_option(new_img):
    image_button.configure(image=new_img)

app.mainloop()
