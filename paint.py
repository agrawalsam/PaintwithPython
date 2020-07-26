from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk
import pyscreenshot as ImageGrab
import PIL
import os

root = Tk()
root.title("Paint Program")
root.geometry("800x800")

brush_color = "black"

def paint(e):

    # Brush Parameters
    brush_width = '%0.0f' % float(my_slider.get())
    #brush_color = "green"
    #brush_type2 = brush_type.get()  # BUTT, ROUND, PROJECTING

    # Starting Position 
    x1 = e.x - 1
    y1 = e.y - 1

    # Ending Position
    x2 = e.x + 1
    y2 = e.y + 1

    # Draw on the Canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type.get(), smooth=True)

# Change the size of brush
def change_brush_size(e):
    slider_label.config(text='%0.0f' % float(my_slider.get()))


def change_brush_color():
    global brush_color 
    brush_color = "black"
    brush_color = colorchooser.askcolor(color=brush_color)[1]

def change_canvas_color():
    global bg_color 
    bg_color = "white"
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)

def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")

def save_image():
    result = filedialog.asksaveasfilename(initialdir=os.getcwd(), filetypes=(("png files", "*.png"),("all files","*.*")))
    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'
    if result:
        x = root.winfo_rootx() + my_canvas.winfo_x()
        y = root.winfo_rooty() + my_canvas.winfo_y()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)

        # Pop up box 
        messagebox.showinfo("Image Saved", "Your Image has been saved")

# Create Canvas 
w = 600
h = 400
my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# x1 = 0
# y1 = 100

# x2 = 300
# y2 = 100

# my_canvas.create_line(x1, y1, x2, y2, fill="red")

# Brush Options Frame 
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text="BRUSH SIZE")
brush_size_frame.grid(row=0, column=0, padx=50)

# Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to_=100, command = change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

# Brush Slider Label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)


# Brush Width 
brush_color_frame = LabelFrame(brush_options_frame, text="CHANGE COLOR")
brush_color_frame.grid(row=0, column=1, padx=50) 

brush_color_change = Button(brush_color_frame, text="BRUSH", command = change_brush_color)
brush_color_change.pack(pady=10)

canvas_color_change = Button(brush_color_frame, text="CANVAS", command = change_canvas_color)
canvas_color_change.pack(pady=10)


# Brush Type 
brush_type_frame = LabelFrame(brush_options_frame, text="BRUSH TYPE", height=300)
brush_type_frame.grid(row=0, column=2, padx=50) 

# Variable for brush type
brush_type = StringVar()
brush_type.set("round")

# Radio Buttons for Brush Types
brush_type_radio1 = Radiobutton(brush_type_frame, variable=brush_type, text="Round", value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, variable=brush_type, text="Slash", value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, variable=brush_type, text="Diamond", value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change Frame Options  
options_frame = LabelFrame(brush_options_frame, text="PROGRAM OPTIONS")
options_frame.grid(row=0, column=3, padx=50)

#Clear Screen Button
clear_button = Button(options_frame, text="Clear Screen", command = clear_screen)
clear_button.pack(padx=10, pady=10)

# Save button 
save_button = Button(options_frame, text="Save Image", command = save_image)
save_button.pack(padx=10, pady=10)

my_canvas.bind('<B1-Motion>', paint)

root.mainloop()