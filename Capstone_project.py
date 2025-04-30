import tkinter as tk 
import customtkinter 
import math 
from tkinter import END 
from PIL import Image



Humburger_option_image = customtkinter.CTkImage(light_image= Image.open('icons8-hamburger-menu-50.png'),
 dark_image= Image.open('icons8-hamburger-menu-50.png'))

delete_image = customtkinter.CTkImage(light_image= Image.open('delete.png'),
 dark_image= Image.open('delete.png'))

# variables area only 
width = 287
height = 400 
new_height = 40 
new_width = 50 
radius = 20 
font1 = ('Arial', 36) 
font2 = ('Arial', 17)
sequence = "" 
field_text = "" 
store = []




def field_to_add(sth): 
    global field_text 

    field_text= field_text+str(sth)
    print(field_text)

    field.delete("1.0", "end") 
    field.insert("1.0", field_text) 


def calculate(): 
    global field_text 
    global result
    global taken_value
    result = str(eval(field_text)) 
    field.delete("1.0", "end") 
    field.insert("1.0", result)
    hover_display_result()
    
    taken_value = History_caculation(field_text)


def clear(): 
    global field_text 
    field_text = "" 
    field.delete("1.0", "end") 
    field.insert("1.0", field_text)
    label_display.config(text= "")
    field.insert(END,'0')

def delete():
    global field_text  
    if len(field_text) == 1:
        field_text = ""

    else:
        field_text = field_text[:-1]

    field.delete("1.0", "end") 
    field.insert("1.0", field_text)
    field.insert(END,'')

    if field_text == "":
           field.insert(END,'0')



def hover_display_result():
    global field_text
    label_display.config(text= field_text)


def History_caculation(user):
    global result
    full = user + "=" +result
    store.append(full)
    return store


def history_setting(choice):
    global store_listbox

    if choice == "history":
        if store_listbox is None:
            store_listbox = tk.Listbox(window, width= 100, background="#1d2024", fg="white", border= None)
            store_listbox.delete(0, END)
            
            for histories in taken_value:
                store_listbox.insert(END, histories)
                store_listbox.place(relx= 0, rely= .7)
                store_listbox.lift()
    else:

        if store_listbox is not None:
            store_listbox.destroy()
            store_listbox = None
   
    


        

    


window = tk.Tk() 
window.geometry(f'{width}x{height}') 
window.resizable(False, False) 
window.config(background="#0e0f0f") 
window.title("Calculator") 



# frame 1 
field = customtkinter.CTkTextbox(window, height= 2, width= 12, font= font1, fg_color='#0e0f0f', text_color="white") 
field.place(relx= 0, rely= .15, relwidth= 5,) 

field.insert(END,'0')

image_labe = customtkinter.CTkLabel(window, text="", image= delete_image)
image_labe.pack(pady = 200)


first_menu = customtkinter.CTkOptionMenu(window, 
values=["history", "Exit", "settings"], command= history_setting                                                                             
)
first_menu.place(relx= .55, rely= 0)

# store_listbox = tk.Listbox(window, width= 100, background="#1d2024", fg="white", border= None)

# history_display = tk.Label(window, text="")
# history_display.pack()
store_listbox = None
scrollbar1 = None
# frame 1 end 
# frame 2 
height_1 = 50 
width_2= 50 
button_colors = "#36383b" 
button_semi = "#bd7108"


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

button8_h= customtkinter.CTkButton(window, text='0', command= lambda: field_to_add('0'), 
height= 50, 
width= 119, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button8_h.place(relx= .05, rely= .85) 

# button9 = customtkinter.CTkButton(un_lable2, text=')', command= lambda: field_to_add(')'), 
# height= 50, 
# width= 50, 
# corner_radius= 25, 
# fg_color= button_colors, 
# hover_color= "gray") 
# button9.grid(row= 4, column= 2,) 

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
sub_button2 = customtkinter.CTkButton(un_lable2, text='A', command= lambda: clear(), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_semi, 
hover_color= "#edb832", 
) 


sub_button2.grid(row= 2, column= 4) 

equal_button3 = customtkinter.CTkButton(window, text='=', command= lambda: calculate(),
height= 100, 
width= 50, 
corner_radius= 25, 
fg_color= button_semi, 
hover_color= "#edb832"
) 
equal_button3.place(relx= .75, rely= .73) 

equal_button3 = customtkinter.CTkButton(un_lable2, text='.',   command= lambda: delete(), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
equal_button3.grid(row= 3, column= 3)

button9 = customtkinter.CTkButton(un_lable2, text='.', command= lambda: field_to_add('.'), 
height= 50, 
width= 50, 
corner_radius= 25, 
fg_color= button_colors, 
hover_color= "gray") 
button9.grid(row= 4, column= 3,) 

equal_display = tk.StringVar()

label_display = tk.Label(window, text= "", bg="#0e0f0f", fg="#807f7e", font= font2 )
label_display.place(relx= .02, rely=.11)
# frame end 
window.mainloop()
