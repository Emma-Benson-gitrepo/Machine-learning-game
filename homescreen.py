import tkinter
from tkinter import PhotoImage
root2= tkinter.Tk()
root2.configure(background = "#7f66a4")

bg = PhotoImage(file= "header2.png")
howto = PhotoImage(file= "howto.png")
howtob = PhotoImage(file= "howtob.png")
canvas3 = tkinter.Canvas(root2, width = 500, height = 500)
startb = PhotoImage(file= "startbutton.png")
menub = PhotoImage(file= "menub.png")
canvas3.create_image(0,0,image = bg,anchor= "nw")
canvas3.grid(row =0, column =0 ,rowspan =2)     # The images used for the homescreen.
def gotomenu():
    global guide
    global start
    canvas3.delete("all")
    canvas3.config(width=500, height=500)
    canvas3.create_image(0, 0, image=bg, anchor="nw")
    canvas3.grid(row=0, column=0, rowspan=2)
    guide.configure(image= howtob,command= gotoguide)
    guide.grid(column=0, row=1, sticky="NE", padx=70)
    start.grid(row=1, column=0, sticky="NW", padx=70)   # Changes the tkinter canvas to display the menu images


def gotoguide():
    global start
    global guide
    canvas3.delete("all")
    canvas3.config(width=500, height=680)
    canvas3.create_image(0,0,image= howto,anchor= "nw")
    guide.configure(image= menub, command= gotomenu)
    guide.grid(column=0, row=2, sticky="E", padx=50)
    start.grid(column=0, row=2)
    # Changes the tkinter canvas to display the menu images
def gstart():
    root2.quit()
    game() # Closes the home screen and starts the game when the start button is pressed.

guide = tkinter.Button(root2,bg="black",text = "How to",image= howtob,width = 140,height= 35, command= gotoguide,relief= "groove")
guide.grid( column=0,row=1,sticky= "NE", padx= 70)
start = tkinter.Button(root2,bg="black",image= startb,width = 140,height= 35,relief= "groove",command=gstart)
start.grid(row=1, column=0,sticky= "NW", padx= 70)
root2.mainloop()    # The menu buttons, start and guide buttons

