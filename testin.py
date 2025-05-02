import tkinter as tk
from PIL import Image, ImageTk  


# may have to install PILLOW
#      File > Settings > Project Interpreter > + > Search for 		   
#      and install PILLOW

def resizeImage(img, new_width, new_height): 
    old_width = img.width 
    old_height = img.height 
    newPhotoImage = tk.PhotoImage(width=new_width, height=new_height) 
    for x in range(new_width): 
        for y in range(new_height): 
            x_old = int(x*old_width/new_width)
            y_old = int(y*old_height/new_height) 
            rgb = '#%02x%02x%02x' % img.get(x_old, y_old)             
            newPhotoImage.put(rgb, (x, y)) 
    return newPhotoImage

def size_img(name, width, height):
    img = Image.open(f'{name}.png')
    img = img.resize((width, height))
    img = ImageTk.PhotoImage(img)
    return img



# # convert to make Tkinter compatible format
# # make sure the image file is in the project
# image = Image.open("icons8-menu-500.png")
# photo = ImageTk.PhotoImage(image)

# # Displaying and keeping a reference of the image to avoid being cleared
# label = tk.Label(root, image=photo)
# label.image = photo
# label.grid()

