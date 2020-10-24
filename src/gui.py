import random, fileinput
import tkinter as tk
import webbrowser
from tkinter import *

root = tk.Tk()
root.title('Daydreamer')
#fname should be the file name of the image in working directory
fname = "bg.gif"
bg_image = tk.PhotoImage(file=fname)

#get width and height of image
w = bg_image.width()
h = bg_image.height()

#size window correctly
root.geometry("500x400")
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0,0,image=bg_image,anchor='nw')

#add a frame for text
mainframe=tk.Frame(root)

#new window for inspirations
def inspirations():
    top = Toplevel(root)
    top.title("Inspiration")
    w2 = 500
    h2 = 300
    fname2="bg2.gif"
    bg_image2= tk.PhotoImage(file=fname2)
    top.geometry("%dx%d+50+30"%(w2,h2))
    cv2 = tk.Canvas(master=top, width=w2, height = h2)
    cv2.create_image(0,0,image=bg_image2, anchor='nw')
    cv2.pack(side='top', fill='y', expand='no')
    def idea():
        textidea=None
        for line in fileinput.input('textlist.txt'):
            if random.randrange(fileinput.lineno())==0:
                textidea=line
        cv2.create_text(15,20,text=textidea, fill="black", anchor='nw')
        cv2.create_text(15,40,text='Or press the button again for a new idea!', fill="black", anchor='nw')
    idea()
    top.mainloop()

#new directory window
def directory():
    webbrowser.open('https://www.nhs.uk/conditions/stress-anxiety-depression/mental-health-helplines/')
    
#add canvas text
cv.create_text(15,20,text="Hey there daydreamer.",fill="#32335E",anchor='nw')
cv.create_text(15,40,text="Need help with something?", fill="#32335E",anchor='nw')

# get help
def needhelp():
    print('Coming soon')      
    
#add buttons
btn1 = tk.Button(cv, text="Inspire Me", command=inspirations)
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="I Need Help", command=directory)
btn2.pack(side='left',padx=10,pady=5,anchor='sw')
btn4 = tk.Button(cv, text="Quit", command=root.destroy)
btn4.pack(side='left',padx=10,pady=5,anchor='sw')
root.mainloop()

