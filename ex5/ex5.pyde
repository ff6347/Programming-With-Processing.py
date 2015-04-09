# use a loop to draw something

def draw():
    # executed all the time.
    # But we call no Loop at the end
    #
    # Loop the x coordinates
    for  x in range(0, width, 5):
      #  loop the y coordinates
      #
      for y in range(0, height, 5):
        # watch the console
        println("X: " + str(x) + " || Y: " + str(y))
        #  draw smoething
        ellipse(x,y,5,5)
    #  this stops the programm but does not exit (like the exit command)
    noLoop()


