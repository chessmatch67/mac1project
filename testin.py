
import customtkinter
import tkinter as tk

root = tk.Tk()


root.geometry('400x500')
frame_1 = tk.Listbox(root, height= 9, width= 100, bg = 'blue')
frame_1.pack()

button_1 = tk.Button(root, text="close", bg= "blue", command= frame_1.destroy)
button_1.pack(pady= 100)







root.mainloop()