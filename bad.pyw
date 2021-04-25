#Created by Flynn's Forge 2021, from https://flynnsforge.com/

#Imports
import sys
import PIL.Image
from tkinter import *
import cv2
import playsound

root = Tk()
root.option_add('*Font', 'Times 1') #setting font to small so the video fits into the screen

text = Text(root)
text.pack(expand='true', fill=BOTH)

detail = 83

def update_detail(event): #changes video detail
    global detail
    detail = w.get()
    print(detail)

w = Scale(root, from_=30, to=200, orient=HORIZONTAL, command=update_detail) #create slider to change detail
w.pack()

def generate_from_video():
    # get image and read it
    video_path = "C:\\Users\\chuca\\Desktop\\New folder\\bada.mp4" #add path to your mp4 file here
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        framerate = cap.get(cv2.CAP_PROP_FPS)
        framecount = 0
        #playsound.playsound("C:\\Users\\chuca\\Desktop\\New folder\\BadApple-Touhou_fvqd.mp3", False)
        
        while(True):
            # capture frame-by-frame
            success, image = cap.read()
            img = PIL.Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
            # resize the image
            width, height = img.size
            aspect_ratio = height/width
            new_width = width
            new_height = aspect_ratio * new_width * 0.55
            img = img.resize((new_width, int(new_height)))           


            # convert image to greyscale format
            img = img.convert('L')

            pixels = img.getdata()

            #convert to ASCII
            chars = ["B","S","#","&","@","$","%","*","!",":","."] #values taken from https://pythoncircle.com
            new_pixels = [chars[pixel//detail] for pixel in pixels]
            new_pixels = ''.join(new_pixels)
        
            new_pixels_count = len(new_pixels)
            ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
            ascii_image = "\n".join(ascii_image)
            f = open("C:\\Users\\chuca\\Desktop\\New folder\\BadTxt.txt", "a")
            f.write(ascii_image + '\n[-]\n')
            f.close()
            #show in Tkinter
            text.delete('1.0', END)
            text.insert(1.0, ascii_image)
            text.update()
    else:
        print("Not Opened!")

generate_from_video()
root.mainloop()
