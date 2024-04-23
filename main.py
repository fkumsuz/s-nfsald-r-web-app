import os
from tkinter import Tk, Canvas, Button, PhotoImage
from PIL import Image, ImageTk

BACKGROUND_COLOR ="#5F6F52"
TEXT_COLOR ="#FEFAE0"
image_folder = "images/inputs"
# Get the list of image files in the folder
image_files = [file for file in os.listdir(image_folder) if file.endswith((".png", ".jpg"))]

# Initialize the index of the current image
image_index = 0 

 

def load_image(): 
    global image_index, image_files, canvas, image_item 
    # Load the next image from the folder
    image_path = os.path.join(image_folder, image_files[image_index])
    print(image_path)
    image_name = os.path.basename(image_path)
    image_name =os.path.splitext(image_name)[0]
    new_image = Image.open(image_path)
    desired_width = 300  # Set the desired width
    desired_height = 300  # Set the desired height
    resized_image = new_image.resize((desired_width, desired_height), Image.LANCZOS)
    new_image_tk = ImageTk.PhotoImage(resized_image)
    
    # Update the image displayed on the canvas item
    canvas.itemconfig(image_item, image=new_image_tk)
    # Keep a reference to avoid garbage collection
    canvas.image = new_image_tk
    
    # Increment the image index for the next iteration
    image_index = (image_index + 1) % len(image_files)
    canvas.itemconfig(item_text, text=image_name)

def wrong_button():
    # print("wrong")
    load_image()

def right_button():
    # print("right")
    load_image()

window = Tk()
window.title("Sinifsal")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=576, background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Initial loading of the first image
image_path = os.path.join(image_folder, image_files[image_index])
original_image = Image.open(image_path)
print("original image",image_path)
desired_width = 300  # Set the desired width
desired_height = 300  # Set the desired height
resized_image = original_image.resize((desired_width, desired_height), Image.LANCZOS)
image = ImageTk.PhotoImage(resized_image)
image_item=canvas.create_image(400, 276, image=image)
canvas.image = image
image_name = os.path.basename(image_path)
image_name =os.path.splitext(image_name)[0]
image_index+=1
# Buttons
cross_image = PhotoImage(file="images/background_filled_no.png")
unknown_button = Button(image=cross_image, bd=0, highlightthickness=0, command=wrong_button)
unknown_button.grid(row=1, column=1)
 
check_image = PhotoImage(file="images/background_filled_yes.png")
unknown_button = Button(image=check_image, bd=0, highlightthickness=0, command=right_button)
unknown_button.grid(row=1, column=0)
 
item_text = canvas.create_text( 400, 50, text=image_name, font=("Ariel", 30, "italic"), fill=TEXT_COLOR) 
word_text = canvas.create_text(
    400, 500, text="Sınıfsaldır", font=("Ariel", 30, "italic"), fill=TEXT_COLOR)


window.mainloop()
