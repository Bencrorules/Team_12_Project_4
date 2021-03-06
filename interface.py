import os
import tkinter as tk
import tkinter.messagebox
import colorizer
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("B/W to RGB Image Converter")

canvas = Canvas(height="10000", width="10000", bg="#476A6F")

# Adds titles to the top of the GUI
title = Label(root, text="Black & White to Colored Image Converter", font=('Helvetica', 30, 'bold'), fg="#1F2633")
title.pack()
names = Label(root, anchor=CENTER, text="Project 3 by Team 12: Sam Aldeguer, Ben Crocker, Peter Lee, Jordan Cedeno",
              font=('Helvetica', 15), fg="#1F2633")
names.pack()

def bulksave():

    selectedpath = filedialog.askdirectory()
    newdirectory = selectedpath + "/Colored Photos"

    try:
        os.mkdir(newdirectory)
    except:
        tkinter.messagebox.showinfo("Notice", "Please Delete Old Conversion")
        return

    for filename in os.scandir(selectedpath):
        if filename.is_file():
            global img

            img = Image.open(filename.path)  # puts image path into variable
            colored_image_path = colorizer.colorize(filename.path)
            colored_image = Image.open(colored_image_path)

            newimagepath = newdirectory + "/" + os.path.basename(filename)
            colored_image.save(newimagepath)
    del newimagepath, colored_image, colored_image_path, img, newdirectory, selectedpath
    tkinter.messagebox.showinfo("Notice", "Conversion Complete!")

# Method that uploads the image from the button and places the images.
def upload():
    global img
    global bw_image
    global cl_image
    global resized_image
    global imageHeight
    global imageWidth
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(
    ("jpg files", "*.jpg"), ("png files", "*.png"), ("jpeg files", "*.jpeg"),
    ("all files", "*.*")))  # opens file browser
    img = Image.open(root.filename)  # puts image path into variable
    colored_image_path = colorizer.colorize(root.filename)
    colored_image = Image.open(colored_image_path)

    imageWidth, imageHeight = img.size  # gets width and height of image
    resized_image = img.resize(
        (800, int((imageHeight / imageWidth) * 800)))  # scales the image to make it fit on interface
    bw_image = ImageTk.PhotoImage(resized_image)  # turns image path into image

    imageLabel1 = Label(root, image=bw_image)
    imageLabel1.place(relx=0.100, rely=0.6, anchor=W)  # adds image to GUI

    imageWidth, imageHeight = colored_image.size  # gets width and height of image
    resized_image = colored_image.resize(
        (800, int((imageHeight / imageWidth) * 800)))  # scales the image to make it fit on interface
    cl_image = ImageTk.PhotoImage(resized_image)  # turns image path into image

    imageLabel2 = Label(root, image=cl_image)
    imageLabel2.place(relx=0.90, rely=0.6, anchor=E)  # adds image to GUI

    os.remove('finalImage.jpg')

# Method that functions same as normal upload but with stock picture
def stresstest():
    print("Backend Results:")
    global img
    global bw_image
    global cl_image
    global resized_image
    global imageHeight
    global imageWidth

    # tests if testimage.jpg can be loaded
    try:
        img = Image.open('testimage.jpg')  # puts image path into variable
        print("Successfully opened test black and white image")
    except:
        print("Failed to open test black and white image")

    # tests if the colorizer.py file returns successfully
    try:
        colored_image_path = colorizer.colorize('testimage.jpg')
        colored_image = Image.open(colored_image_path)
        print("Successfully produced colored image from nural network")
    except:
        print("Failed to produce colored image from nural network")

    # tests image resize
    try:
        imageWidth, imageHeight = img.size  # gets width and height of image
        resized_image = img.resize(
            (800, int((imageHeight / imageWidth) * 800)))  # scales the image to make it fit on interface
        print("Successfully resized black and white image")
    except:
        print("Failed to resize black and white image")

    # tests image reading functionality
    try:
        bw_image = ImageTk.PhotoImage(resized_image)  # turns image path into image
        print("Successfully read black and white image")
    except:
        print("Failed to read black and white image")

    # tests adding read image to canvas
    try:
        imageLabel1 = Label(root, image=bw_image)
        imageLabel1.place(relx=0.100, rely=0.6, anchor=W)  # adds image to GUI
        print("Successfully added black and white image to the canvas")
    except:
        print("Failed to add black and white image to the canvas")

    # testing for colored image:
    try:
        imageWidth, imageHeight = colored_image.size  # gets width and height of image
        resized_image = colored_image.resize(
            (800, int((imageHeight / imageWidth) * 800)))  # scales the image to make it fit on interface
        print("Successfully resized colored image")
    except:
        print("Failed to resize colored image")

    try:
        cl_image = ImageTk.PhotoImage(resized_image)  # turns image path into image
        print("Successfully read colored image")
    except:
        print("Failed to read colored image")

    try:
        imageLabel2 = Label(root, image=cl_image)
        imageLabel2.place(relx=0.90, rely=0.6, anchor=E)  # adds image to GUI
        print("Successfully added colored image to canvas")
    except:
        print("Failed to add colored image to canvas")

    os.remove('finalImage.jpg')

uploadButton = Button(root, text="Upload Image", width=18, height=5, bd='15', command=upload, bg="#e9f0ea", fg="#1F2633", font=('Helvetica', 16))  # creates button
uploadButton.place(relx=0.3, rely=0.15, anchor=CENTER)  # places button at top center of screen

massConversion = Button(root, text="Mass Conversion", width=18, height=5, bd='15', command=bulksave, bg="#e9f0ea", fg="#1F2633", font=('Helvetica', 16))  # creates button
massConversion.place(relx=0.5, rely=0.15, anchor=CENTER)  # places button at top center of screen

testButton = Button(root, text="Test System", width=18, height=5, bd='15', command=stresstest, bg="#e9f0ea", fg="#1F2633", font=('Helvetica', 16))  # creates button
testButton.place(relx=0.7, rely=0.15, anchor=CENTER)  # places button at top center of screen

bwLabel = Label(root, text="Black & White Photo", font=('Helvetica', 32, 'bold'), bg="#476A6F", fg="#1F2633")  # Black & White photo label
bwLabel.place(relx=0.175, rely=0.35, anchor=W)
colorLabel = Label(root, text="Colored", font=('Helvetica', 32, 'bold'), bg="#476A6F", fg="#1F2633")  # Colored photo label
colorLabel.place(relx=0.778, rely=0.35, anchor=E)

canvas.pack()  # Puts everything onto the GUI

root.mainloop()
