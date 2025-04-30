import customtkinter as ctk
import tkinter as tk

# Setup window
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x300")

# Load images
icon_image = tk.PhotoImage(file="icons8-hamburger-menu-50.png")  # This will be your OptionMenu replacement

# Function to open the menu
def open_menu():
    menu.post(image_button.winfo_rootx(.01), image_button.winfo_rooty() + image_button.winfo_height())

# Create a button with an image (acts like OptionMenu)
image_button = ctk.CTkButton(app, text="", image=icon_image, width=100, height=100, command=open_menu, fg_color="transparent", hover_color="lightgray")
image_button.pack(pady=50)

# 
# 
# Create the menu

def car():
    print("car")

menu = tk.Menu(app, tearoff=0)
menu.add_command(label="Option 1", compound="left", command= car)
menu.add_command(label="Option 2", compound="left", command=lambda: select_option(option2_image))

# Function to change the image on button
def select_option(new_img):
    image_button.configure(image=new_img)


app.mainloop()
