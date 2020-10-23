import random, fileinput
import tkinter as tk
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
    top.geometry=("100x100")
    top.title("Inspiration")
    def idea():
        textidea=None
        for line in fileinput.input('textlist.txt'):
            if random.randrange(fileinput.lineno())==0:
                textidea=line
        entrytext=tk.Text(top)
        entrytext.insert(INSERT, textidea)
        entrytext.insert(END, "Or press the Inspire Me button again for another idea!")
        entrytext.pack()
    idea()
        
    top.mainloop()

#add canvas text
cv.create_text(15,20,text="Hey there daydreamer.",fill="white",anchor='nw')
cv.create_text(15,40,text="Need help with something?", fill="white",anchor='nw')


#clear the text
def reset():
    for label in idea():
        label.destroy()

# get help
def needhelp():
    print('Coming soon')      
    
#add buttons
btn1 = tk.Button(cv, text="Inspire Me", command=inspirations)
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="I Need Help", command=needhelp)
btn2.pack(side='left',padx=10,pady=5,anchor='sw')
btn4 = tk.Button(cv, text="Quit", command=root.destroy)
btn4.pack(side='left',padx=10,pady=5,anchor='sw')
root.mainloop()

