# save images by keyPress
# you can either call keyPressed as boolean or use the
# void keyPressed method
# This sketch shows both


def draw():
    # executed until the programm ends
    #
    # check if a key is pressed
    if keyPressed == True:
        # set the backgroun to white
        background(255)
    else:
        # if no key is pressed set the background to black
        background(0)



# press the mouse (or trackpad)
def mousePressed():
    println("mouse pressed")


# executed when a key is pressed
# this is more acurate then looking for the keypressed boolean in the draw
# whatch the console output
# the keyPressed boolean in the draw can be executed several times

def keyPressed():
    # if it is S or s
    # save a black image (becuase the bg is black)
    if key == 'S' or key == 's':
        println("S or s pressed. Saving image black")
        saveFrame("image-black.png")
        # saveFrame("sequence-####.png")
    else:
        println("Not S or s pressed. Saving image white")
        background(255)
        # check if a key is pressed
        # If it is not S or s
        # save a white image
        println("Neither S nor s pressed. Saving image white")
        saveFrame("image-white.png")

