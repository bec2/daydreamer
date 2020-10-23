
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
root.geometry("%dx%d+50+30" % (w, h))
cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0,0,image=bg_image,anchor='nw')

#add canvas text
cv.create_text(15,20,text="Hello World",fill="red",anchor='nw')

#add buttons
btn1 = tk.Button(cv, text="Click")
btn1.pack(side='left', padx=10, pady=5, anchor='sw')
btn2 = tk.Button(cv, text="Quit", command=root.destroy)
btn2.pack(side='left',padx=10,pady=5,anchor='sw')
root.mainloop()
