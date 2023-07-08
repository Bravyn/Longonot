import turtle

from PIL import Image

def draw_square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def save_drawing():
    turtle.speed(1)
    turtle.penup()
    turtle.hideturtle()
    turtle.pendown()
    draw_square()
    
    # Get the turtle drawing as a PIL image
    canvas = turtle.getscreen().getcanvas()
    canvas.postscript(file="drawing.eps", colormode="color")
    turtle.done()
    
    # Save the image as PNG
    image = Image.open("drawing.eps")
    image.save("drawing.png", "PNG")
    
    

save_drawing()



