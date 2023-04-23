import pygame
import tkinter
from tkinter.colorchooser import askcolor
from tkinter import PhotoImage
import random
from PIL import Image, ImageDraw
import numpy as np
import tensorflow as tf
import cv2


pygame.init()
window = pygame.display.set_mode((832, 470))
pygame.display.set_caption("game")

background = pygame.image.load("backg.jpg").convert()
forward = [pygame.image.load("for1.png"),pygame.image.load("for.png"),pygame.image.load("for2.png")]
back = [pygame.image.load("bac1.png"),pygame.image.load("bac-6.png"),pygame.image.load("bac2.png")]
walkleft = [pygame.image.load("lef1.png"),pygame.image.load("lef.png"),pygame.image.load("lef2.png")]
walkright = [pygame.image.load("rig1.png"),pygame.image.load("rig.png"),pygame.image.load("rig2.png")]
chara= pygame.image.load("for.png")
batdown = [pygame.image.load("bat1.png"), pygame.image.load("bat2.png"), pygame.image.load("bat3.png")]
batup = [pygame.image.load("bat3.png"), pygame.image.load("bat2.png"),pygame.image.load("bat1.png")]
ghostl = [pygame.image.load("ghost1.png"), pygame.image.load("ghost2.png"), pygame.image.load("ghost3.png")]
ghostr =  [pygame.image.load("ghostr1.png"), pygame.image.load("ghostr2.png"), pygame.image.load("ghostr3.png")]

# Game sprites and background images.




class player(object): # The player class for the player character
    def __init__(self,x,y,width,height):
        self.x = x
        self.y =y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpc = 4
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkc = 0
        self.hitb = (self.x , self.y, 30, 15 )





    def playerdraw(self, window):       # draws the players sprite depending on what movement is being made.
        if self.walkc + 1 >= 9:
            self.walkc= 0
        if self.down:
            window.blit(forward[self.walkc//3],(self.x,self.y))
            self.walkc+=1
        elif self.up:
            window.blit(back[self.walkc//3],(self.x,self.y))
            self.walkc+=1
        elif self.left:
            window.blit(walkleft[self.walkc//3],(self.x,self.y))
            self.walkc+=1
        elif self.right:
            window.blit(walkright[self.walkc//3],(self.x,self.y))
            self.walkc+=1
        else:
            window.blit(chara,(self.x,self.y))
            self.walkc=0
        self.hitb = (self.x , self.y +17, 30, 15 )

class ghost(object):      # Class that creates the ghost object
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkc= 0
        self.vel = 3
        self.right = True
        self.left = False
        self.movec = 0
        self.hitb = (self.x , self.y, 55, 55 )
        self.defeat = False


    def ghostdraw(self,window):     # Draws the ghost sprite depending on the direction of movement
        self.ghostmove()
        if self.walkc + 1 >= 9:
            self.walkc = 0

        if self.vel > 0 and self.right== True:
            window.blit(ghostr[self.walkc // 3], (self.x, self.y))
            self.walkc += 1
        else:
            window.blit(ghostl[self.walkc // 3], (self.x, self.y))
            self.walkc += 1
        self.hitb = (self.x , self.y , 55, 55 )


    def ghostmove(self): # Sets the velocity anf direction of movement for the ghost sprites
        if self.right == True:
            self.x += self.vel
            self.movec += 1
            if self.movec ==50:
                self.right = False
                self.left =True
        else:
            self.x -= self.vel
            self.movec -= 1
            if self.movec == 0:
                self.right = True
                self.left =False

ghostnum = 1
ghost1 = ghost(200, 315, 50, 50)
ghost2 = ghost(400, 315, 50, 50) # Creates two instances of the ghost class
def calltkinter():  # The Drawing pad where the player writes the number required to revive the ghost.

    root = tkinter.Tk()

    canvaswidth = 250
    canvasheight = 250
    AIsize = 250
    colour = "black"
    bgcolour = "white" # Sets up the tkinter canvas

    zero = tkinter.PhotoImage(file="0.png")
    one = tkinter.PhotoImage(file="1.png")
    two = tkinter.PhotoImage(file="2.png")
    three = tkinter.PhotoImage(file="3.png")
    four = tkinter.PhotoImage(file="4.png")
    five = tkinter.PhotoImage(file="5.png")
    six = tkinter.PhotoImage(file="6.png")
    seven = tkinter.PhotoImage(file="7.png")
    eight = tkinter.PhotoImage(file="8.png")
    nine = tkinter.PhotoImage(file="9.png")     # each image tells the player to draw a different digit.

    fail = tkinter.PhotoImage(file="fail.png")
    yay = tkinter.PhotoImage(file="welldone.png") # The image displayed if the user passes or fails

    def imchoose():
        images = [zero, one, two, three, four, five, six, seven, nine]
        image = random.choice(images)
        global digit
        if image == zero:
            digit = 0
        elif image == one:
            digit = 1
        elif image == two:
            digit = 2
        elif image == three:
            digit = 3
        elif image == four:
            digit = 4
        elif image == five:
            digit = 5
        elif image == six:
            digit = 6
        elif image == seven:
            digit = 7
        elif image == eight:
            digit = 8
        elif image == nine:
            digit = 9
        print(digit)
        return image  # This function randomly chooses a digit and returns the digit chosen.
                      # This function could be more efficient, without the if statement just randomly choosing an integer

    notepadt = tkinter.PhotoImage(file="notepad.png")
    notepadb = tkinter.PhotoImage(file="notepad2.png")
    canvas = tkinter.Canvas(root, width=canvaswidth, height=canvasheight, bg=bgcolour)
    canvas1 = tkinter.Canvas(root, width=canvaswidth, height=68)
    canvas1.pack()
    canvas1.create_image(0, 0, image=notepadt, anchor="nw")
    canvas.create_image(0, 0, image=notepadb, anchor="nw")
    canvas.pack()
    canvas2 = tkinter.Canvas(root, width=500, height=100, bg="pink")
    canvas2.create_image(0, 0, image=imchoose(), anchor="nw")
    canvas2.pack()  #Creates 3 canvases. The first displays the image for the top of the notepad. The second is the notepad and the third displays the image for which digit to draw


    mlimage = Image.new("RGB", (AIsize, AIsize), (255, 255, 255))
    draw = ImageDraw.Draw(mlimage)  #Creates an image to feed to the AI

    colour = "black"
    size = 18

    def colchangeb():
        global colour
        colour = "blue"

    def colchanger():
        global colour
        colour = "red"

    def colchangebl():
        global colour
        colour = "black"

    def getColor():
        color = askcolor()
        global colour
        colour = color[1]   # changes the pen colour

    def fillcol():
        color = askcolor()
        col = color[1]
        canvas.create_rectangle(0, 0, 1000, 1000, fill=col, outline=colour)     #   creates a rectangle of a chosen colour over the notpad

    def rubber():
        global colour
        colour = "#fde9a4"  # The rubber changes the pen colour to the background of the notepad

    def clear():
        canvas.delete("all")
        draw.rectangle((0, 0, 250, 250), fill=(255, 255, 255, 0))
        canvas.create_rectangle(0, 0, 1000, 1000, fill="#fde9a4", outline="#fde9a4")    # Creates a rectangle the colour of the notepad to clear the screen

    fillbuck = PhotoImage(file="fill.png")
    wheel = PhotoImage(file="wheel.png")
    trash = PhotoImage(file="trash.png")
    rub = PhotoImage(file="rub.png")
    go = PhotoImage(file="go.png")  # Creates the sprites for the fill, clear screen, rubber and go buttons

    def createcircle(self, x, y, r, **kwargs):
        self.create_oval(x - r, y - r, x + r, y + r, **kwargs)


    tkinter.Canvas.create_circle = createcircle # Draws a circle to be used by the pen

    def store_position(event) :
        global lastx
        global lasty
        lastx = event.x
        lasty = event.y # stores the position of the mouse on the screen

    def click(event):
        store_position(event)
        canvas.create_circle(event.x, event.y, size, fill=colour, outline=colour)
        draw.point([lastx, lasty], fill=colour)
        store_position(event)   # creates a circle where the canvas is clicked and stores the position of the click

    def drag(event):
        if size > 5:
            canvas.create_circle(event.x, event.y, size, fill=colour, outline=colour)
            draw.line([(lastx, lasty),(event.x, event.y)], fill=colour, width=24)
            store_position(event)   # if the pen size is bigger than 3 the mouse is dragged across the canvas

        else:
            canvas.create_line(lastx, lasty, event.x, event.y, fill=colour, width=size)
            draw.line([(lastx, lasty), (event.x, event.y)], fill=colour, width=24)
            store_position(event)   # if the pen size is smaller than 3 a line looks more effective than a circle but the same process as above is used.

    def destroywind():
        root.destroy()  # Closes the tkinter window

    def save(): #Saves the AI image and feeds it to the saved AI model.
        canvas.update()
        canvas.postscript(file="my_drawing.ps", colormode='color')
        filename = "my_drawing.jpg"
        mlimage.save(filename)
        load = cv2.imread("my_drawing.jpg", 0)
        load2 = cv2.resize(load, (28, 28))
        load = load2.reshape(28, 28, -1)
        load = load.reshape(1, 1, 28, 28)   # Resizes and reshapes the image to match the requirements of the AI model
        load = cv2.bitwise_not(load)
        load = load / 255   # Normalises the image ( Instead of 1-255 pixel values   0-1)
        print(load)
        newsequen = tf.keras.models.load_model("readnum.sequen")    # Loads the saved AI model
        result = newsequen.predict(load)    # Puts the reshaped image into the model to predict the digit.
        global finish
        finish = np.argmax(result)  # Assigns the predicted digit integer to a variable
        print(finish)
        if finish == digit: # If the predicted digit is the same as the digit the player was told to draw
            canvas2.create_image(0, 0, image=notepadt, anchor="nw")
            canvas2.pack()
            if ghostnum== 1:
                ghost1.defeat = True
            else:
                ghost2.defeat=True  # Set the defeat variable for the correct ghost instance to true
            canvas2.create_image(0, 0, image=yay, anchor="nw") # Display the win image over the canvas
            root.after(2000, destroywind)  # after 2000 miliseconds call the destroywind function to close the tkinter window
        else:
            canvas2.create_image(0, 0, image=fail, anchor="nw") # displays the fail image over the canvas.

    ru = tkinter.Button(root, width=130, command=save, image=go)
    ru.pack()

    redpen = tkinter.PhotoImage(file="red.png")
    bluepen = tkinter.PhotoImage(file="blue.png")
    blackpen = tkinter.PhotoImage(file="black.png")
    blackbord = tkinter.PhotoImage(file="blackbord.png")    # assigns the pen colour sprites to variables

    fill = tkinter.Button(root, image=fillbuck, bg="black", command=fillcol)
    fill.pack(side="left", ipadx=25)
    choosec = tkinter.Button(root, image=wheel, bg="black", command=getColor)
    choosec.pack(side="left")
    blue = tkinter.Button(root, bg="black", image=bluepen, command=colchangeb)
    blue.pack(side="left")
    red = tkinter.Button(root, bg="black", image=redpen, command=colchanger)
    red.pack(side="left")
    black = tkinter.Button(root, bg="black", image=blackpen, command=colchangebl)
    black.pack(side="left")
    borderblack = tkinter.Label(root, bg="black", image=blackbord)
    borderblack.pack(side="left")
    rubber = tkinter.Button(root, image=rub, bg="black", command=rubber)
    rubber.pack(side="left")
    cl = tkinter.Button(root, image=trash, bg="black", command=clear)
    cl.pack(side="left")        # packs all buttons onto the tkinter canvas

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", drag)
    root.mainloop()     # The end of the tkinter drawing pad
player1 = player(50, 345, 30, 30)   # creates an instance of the player class
def gamedraw():
    global window
    player1.playerdraw(window)
    pygame.display.update()     # Draws the game window and updates the display

def redrawghosts():
    ghost1 = ghost(player1.x + 200, 315, 50, 50)
    ghost2 = ghost(player1.x - 200, 315, 50, 50)        # Redraws the ghosts when they are defeated.

def game():
    run = True
    b1 = (0, 0, 109, 959)
    clock = pygame.time.Clock()

    up = False
    bgx = 0
    lastx = 0
    lasty = 0
    player1 = player(50, 345, 30, 30)
    global ghostnum
    global ghost1
    global ghost2       # Sets all game variables, the clock and background

    def gamedraw():

        player1.playerdraw(window)
        pygame.display.update()    # Could this be removed? It this is a duplicate.


    run = True
    while run== True:   # While the game is running..
        keyboard = pygame.key.get_pressed()     # Creates a variable for keyboard presses
        clock.tick(27)      # Sets the clock speed
        relx = bgx % background.get_rect().width
        print(relx - background.get_rect().width)
        print ("relx:" +str(relx))
        window.blit(background, ((relx- background.get_rect().width), 0))
        window.blit(background, ((relx), 0))    # This moves the background as the player moves

        if player1.x + 300> background.get_rect().width and keyboard[pygame.K_RIGHT]:
            player1.x = 532
            window.blit(background, ( (relx ), 0))
            bgx -= 5        # If the player reaches the end of the background image and is continuing to move right add another background image after the current image.

        window.blit(background, (bgx, 0))   # Draws the background image
        player1.playerdraw(window)      # Draws the player in the game window
        if ghostnum == 1:       # For the first ghost instance
            if ghost1.defeat== False:
                ghost1.ghostdraw(window)    # If the ghost has been defeated draw a new ghost
            if ghost1.hitb[1] - ghost1.hitb[3] < player1.hitb[1] + player1.hitb[3] and ghost1.hitb[1] + ghost1.hitb[3] > player1.hitb[
                1]:
                if ghost1.hitb[0] + ghost1.hitb[3] > player1.hitb[0] and ghost1.hitb[0] - ghost1.hitb[3] < player1.hitb[0] + player1.hitb[
                    2] and ghost1.defeat==False:        # If the player collides with an undefeated ghost
                    calltkinter()
                    ghostnum = 2     # Open the drawing pad so the ghost can be defeated
        else:
            if ghost2.defeat== False:
                ghost2.ghostdraw(window)    # If the ghost has been defeated draw a new ghost
            if ghost2.hitb[1] - ghost2.hitb[3] < player1.hitb[1] + player1.hitb[3] and ghost2.hitb[1] + ghost2.hitb[3] > player1.hitb[
                1]:
                if ghost2.hitb[0] + ghost2.hitb[3] > player1.hitb[0] and ghost2.hitb[0] - ghost2.hitb[3] < player1.hitb[0] + player1.hitb[
                    2] and ghost2.defeat==False:         # If the player collides with an undefeated ghost
                    calltkinter()
                    ghostnum = 1        # Open the drawing pad so the ghost can be defeated
        if ghost1.defeat == True and ghost2.defeat == True :
            if relx !=0 and relx <450 and relx>400:
                redrawghosts()
                ghost1.defeat=False
                ghost2.defeat = False
                print(ghostnum)

        print(ghost1.defeat)

        if keyboard[pygame.K_LEFT] and player1.x > player1.vel:
            player1.x -= player1.vel
            player1.left= True
            player1.right = False
            player1.up = False
            player1.down = False    # If the left key is pressed assign the player1.left variable to True

        elif keyboard[pygame.K_RIGHT] and player1.x < 960 - player1.vel - player1.width:
            player1.x += player1.vel
            player1.left = False
            player1.right = True
            player1.up = False
            player1.down = False    # If the right key is pressed assign the player1.right variable to True

        else:
            player1.left= False
            player1.right = False
            player1.up = False
            player1.down = False
            player1.walkc = 0       # If neither set all player1 variables to false

        if player1.isJump == False and up != False :
            if keyboard[pygame.K_UP]and player1.y > player1.vel  :
                player1.y -= player1.vel
                player1.down = False
                player1.right = False
                player1.left = False
                player1.up = True   # If the up key is pressed assign the player1.up variable to True
            if keyboard[pygame.K_DOWN] and player1.y <960 - player1.height - player1.vel :
                player1.y += player1.vel
                player1.down=True
                player1.right= False
                player1.left = False
                player1.up= False   # If the down key is pressed assign the player1.down variable to True

                # Are the up and down functions necessary ? This is a platform game.

        elif  up == False  and player1.isJump == False:
            if keyboard[pygame.K_SPACE]:
                player1.x += player1.vel
                player1.left = False
                player1.right = True
                player1.up = False
                player1.down = False
                player1.isJump = True   # If the space bar is pressed assign the player1.jump variable to True


        else :
            if player1.jumpc >= -4:
                player1.y -= (player1.jumpc * abs(player1.jumpc)) * 0.5
                player1.jumpc -= 1
            else:
                player1.jumpc= 4
                player1.isJump = False     # Makes the player jump for 4 counts

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     # If the game is quit then end the game


        pygame.display.update()     # Update the game display

    pygame.quit()

game()  # calls the game function.