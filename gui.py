import random, fileinput
import tkinter as tk

root = tk.Tk()
root.title('background image')
#fname should be the file name of the image in working directory
fname = "bg.gif"
bg_image = tk.PhotoImage(file=fname)

#get width and height of image
w = bg_image.width()
h = bg_image.height()

#size window correctly for image
root.geometry("500x400")
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0,0,image=bg_image,anchor='nw')

#add canvas text
cv.create_text(15,20,text="Hey there daydreamer.",fill="white",anchor='nw')
cv.create_text(15,40,text="Need help with something?", fill="white",anchor='nw')

# idea generator
def idea():
    textidea=None
    for line in fileinput.input('textlist.txt'):
        if random.randrange(fileinput.lineno())==0:
            textidea = line
    label = tk.Label(root, text=textidea)

#clear the text
def reset():
    for label in idea():
        label.destroy()

# get help
def needhelp():
    print('Coming soon')

        
    
#add buttons
btn1 = tk.Button(cv, text="Inspire Me", command=idea)
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="I Need Help", command=needhelp)
btn2.pack(side='left',padx=10,pady=5,anchor='sw')
btn4 = tk.Button(cv, text="Quit", command=root.destroy)
btn4.pack(side='left',padx=10,pady=5,anchor='sw')
root.mainloop()

