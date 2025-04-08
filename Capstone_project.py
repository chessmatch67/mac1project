import tkinter as tk 
import customtkinter 
import math 
from tkinter import END 


# variables area only 
width = 300
height = 400 
new_height = 40 
new_width = 50 
radius = 20 
font1 = ('Arial', 36) 
font2 = ('Arial', 17)
sequence = "" 
field_text = "" 
store = ""
display1 = ""

def field_to_add(sth): 
    global field_text 
    global display1
    display1 = field_text
    field_text= field_text+str(sth)
    print(field_text, sth)

    field.delete("1.0", "end") 
    field.insert("1.0", field_text) 


def calculate(): 
    global field_text 
    result = str(eval(field_text)) 
    field.delete("1.0", "end") 
    field.insert("1.0", result)
    hover_display_result()

def clear(): 
    global field_text 
    field_text = "" 
    field.delete("1.0", "end") 
    field.insert("1.0", field_text)

def delete():
    global field_text  
    if len(field_text) == 1:
        field_text = ""

    else:
        field_text = field_text[:-1]

    field.delete("1.0", "end") 
    field.insert("1.0", field_text)


def hover_display_result():
    global field_text
    global display1
    label_display.config(text= display1)



window = tk.Tk() 
window.geometry(f'{width}x{height}') 
window.resizable(False, False) 
window.config(background="#0e0f0f") 
window.title("Calculator") 



# frame 1 
field = customtkinter.CTkTextbox(window, height= 2, width= 12, font= font1, fg_color='#0e0f0f', text_color="white") 
field.place(relx= 0, rely= .1, relwidth= 5,) 

# frame 1 end 
# frame 2 
height_1 = 50 
width_2= 50 
button_colors = "#696969" 
button_semi = "#c78f02"
# menu = customtkinter.CTkOptionMenu(master= window, values= ["History"]) 
# menu.place(relx= 0, rely= 0) 
# History_frame = customtkinter.CTkFrame(master= window) 
# History_frame.place(relx=0, rely=0) 

un_lable2 = customtkinter.CTkFrame(window, fg_color='#0e0f0f') 
un_lable2.place(relx= .03, rely= .3, relheight= 400, relwidth= .94) 
button1 = customtkinter.CTkButton(un_lable2, text='9', command= lambda: field_to_add(9), 
height= height_1, 
width= width_2, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button1.grid(row= 0, column= 1) 
button2 = customtkinter.CTkButton(un_lable2, text='8', command= lambda: field_to_add(8), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button2.grid(row= 0, column= 2, padx= 4) 
button3 = customtkinter.CTkButton(un_lable2, text='7', command= lambda: field_to_add(7), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button3.grid(row= 0, column= 3,) 
button4 = customtkinter.CTkButton(un_lable2, text='6',
command= lambda: field_to_add(6), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button4.grid(row= 1, column= 1, pady= 5) 
button5 = customtkinter.CTkButton(un_lable2, text='5', command= lambda: field_to_add(5), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button5.grid(row= 1, column= 2,) 
button6 = customtkinter.CTkButton(un_lable2, text='4', command= lambda: field_to_add(4), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button6.grid(row= 1, column= 3,) 
button6 = customtkinter.CTkButton(un_lable2, text='5', command= lambda: field_to_add(5), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button6.grid(row= 1, column= 2) 
button7 = customtkinter.CTkButton(un_lable2, text='3', command= lambda: field_to_add(3), 
height= 50,
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button7.grid(row= 2, column= 1) 
button7 = customtkinter.CTkButton(un_lable2, text='2', command= lambda: field_to_add(2), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button7.grid(row= 2, column= 2) 
button7 = customtkinter.CTkButton(un_lable2, text='1', command= lambda: field_to_add(1), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button7.grid(row= 2, column= 3,) 
button8 = customtkinter.CTkButton(un_lable2, text='/', command= lambda: field_to_add('/'), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button8.grid(row= 3, column= 1, pady= 5) 
button8 = customtkinter.CTkButton(un_lable2, text='x', command= lambda: field_to_add('*'), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors,
hover_color= "gray") 
button8.grid(row= 3, column= 2,) 
button9 = customtkinter.CTkButton(un_lable2, text='(', command= lambda: field_to_add('('), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button9.grid(row= 4, column= 1,) 
button9 = customtkinter.CTkButton(un_lable2, text=')', command= lambda: field_to_add(')'), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button9.grid(row= 4, column= 2,) 
# img = Image.open("!-Photoroom.copy.png").resize((50, 55)) 
# fhoto_1 = ImageTk.PhotoImage(img) 
# adding and subtracting buttons 
add_button1 = customtkinter.CTkButton(un_lable2, text='+', command= lambda: field_to_add('+'), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_semi, 
hover_color= "#edb832" 
) 

add_button1.grid(row= 0, column= 4, padx= 15) 
add_button2 = customtkinter.CTkButton(un_lable2, text='-', command= lambda: field_to_add('-'),
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_semi, 
hover_color= "#edb832" 
) 

now = 12 
add_button2.grid(row= 1, column= 4) 
sub_button2 = customtkinter.CTkButton(un_lable2, text='Ac', command= lambda: clear(), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_semi, 
hover_color= "#edb832", 
) 


sub_button2.grid(row= 2, column= 4) 

equal_button3 = customtkinter.CTkButton(un_lable2, text='=', command= lambda: calculate(),
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_semi, 
hover_color= "#edb832"
) 
equal_button3.grid(row= 3, column= 4) 
equal_button3 = customtkinter.CTkButton(un_lable2, text='.', command= lambda: field_to_add('.'), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
equal_button3.grid(row= 3, column= 3)

button9 = customtkinter.CTkButton(un_lable2, text='Del', command= lambda: delete(), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button9.grid(row= 4, column= 3,) 

equal_display = tk.StringVar()

label_display = tk.Label(window, text= "", bg="#0e0f0f", fg="white", font= font2 )
label_display.place(relx= .03, rely=.06)
# frame end 
window.mainloop()
