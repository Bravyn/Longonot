import streamlit as st
import turtle
from PIL import Image
import io

def draw_square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def save_drawing(canvas):
    # Get the turtle drawing as a PIL image
    image = turtle.getscreen().getcanvas().postscript(colormode="color")
    turtle.done()
    
    # Save the image using Streamlit's save_as_png() function
    streamlit_image = Image.open(io.BytesIO(image.encode("utf-8")))
    canvas.image(streamlit_image)
    st.image(streamlit_image, use_column_width=True)
    st.write("Drawing saved!")


def main():
    st.title("Turtle Drawing App")
    
    with st.beta_container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Drawing")
            # Create a canvas for the turtle drawing
            canvas = st.empty()
        
        with col2:
            st.subheader("Save Drawing")
            # Save button to save the drawing as an image
            if st.button("Save"):
                save_drawing(canvas)
# Configure the Turtle module
turtle.speed(1)
turtle.penup()
turtle.hideturtle()
turtle.pendown()
    
    # Run the Streamlit app
main()
