import customtkinter
import tkinter as tk

root = customtkinter.CTk()
root.geometry('400x500')
opt = ['exit']
menuopt1 = tk.OptionMenu(root, *opt)
menuopt1.pack()
 menuopt1.config()







root.mainloop()