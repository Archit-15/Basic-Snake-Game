import turtle 
import random
import time

# This delay is the delay in animation and as we score it keeps on decreasing which means the 
# speed of animation is increasing
delay = 0.1
score = 0
High_score = 0

# Modifying the screen
wn = turtle.Screen()        #This returns the screen on which we are going to draw
wn.title("SNAKE GAME")     #sets tittle of turtle window
wn.bgcolor('blue')          #sets the color of the scrreen we are going to draw

wn.setup(width =600,height=600)
wn.tracer(0)                #This will turn off the animation, by default it is set to 1


#head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("white")             #This will set the pen color (will color head)
head.penup()            #This will put the pen up which means no drawing when it will move, But the 
#turtle will be visible
head.goto(0, 0)
head.direction = "Stop"           #making an instace attribute
 

#food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green'])           # will randomly pick one color
shapes = random.choice(['triangle', 'circle'])     #will randomly pick one shape
food.color(colors)
food.shape(shapes)
food.speed(0)           #This is the fastest speed
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)        #Fastest speed
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()            #Makes the turtle invisible
pen.goto(0,250)
#This will write the string given as argument at its position 
pen.write("Score: 0 High Score: 0",align = "center",font =("candara",24,"bold"))   


# We can't move backwards in the same direction becuase we cant coincide with ourselves, that would
# result inn our loss
def goup():
    if head.direction != 'down':
        head.direction = 'up'

def godown():
    if head.direction != 'up':
        head.direction = 'down'

def goleft():
    if head.direction != 'right':
        head.direction = 'left'

def goright():
    if head.direction != 'left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()                 #This fucntion returns the y coordinate of turtle
        head.sety(y+20)                 #will update the y coordinate and leave the x cor unchanged
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x = head.xcor()                 #retursns the x coordinate
        head.setx(x-20)                  #updates the x coordinate and levaes the y cor unchanged
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)


wn.listen()             #This will listen for events, which meansfocus will be set to turtle screen
#to collect key-events(keys being pressed)
wn.onkeypress(goup, "w")         #This function has binded the function with press key event
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []           #contains the new body parts of snake after eating food

# Main gameplay

while True:
    wn.update()          #Since the tracer is turned off that means the animation is also off and
    #using update will draw all the animmations that were supposed to be drawn when tracer was off

    # This if is to specify what will happen if we hit the boundary of the our table
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()    # This will clear the list
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, High_score), align="center", font=("candara", 24, "bold"))


    # If we consume the food then the food will be randomly alloted to a new coordinate
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        #Adding a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay = delay - 0.001
        score = score + 10
        if score>High_score:
            High_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, High_score), align="center", font=("candara", 24, "bold"))


        #MOVING THE SNAKE
        #THIS LOOP WONT EXECUTE AT ALL  IF THERE IS  NO SEGMENT
        # here if length is only 1 then loop wont execute as index value will become 0
    for index in range(len(segments)-1,0,-1): #Will start from the last index and go backwards till 1st index
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        #We move all the segments of the snake body in the above for loop and here we move the 0th segment
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y) 
    move()


    # Checking the colision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()    # This will clear the list
 
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, High_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay) #This will delay the execution of program by delay value which means after every
    #move the program's execution will stop for 0.1 seconds and it will keep on decreasing as we score
    # which means it will keep on becoming faster
 
wn.mainloop()   #writen at the end of every program it is used to pause the graphics window until
#we close it manually or the user does something

