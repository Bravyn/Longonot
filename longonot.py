import streamlit as st

st.set_page_config("Proffessor Zee", ":glasses:")

st.title(":blue[Learn Python For Kids :computer:]")
st.subheader("By the Professor. :eyeglasses:")

def python_definition():
    st.divider()
    st.caption(":orange[**Dr.Zee :eyeglasses:**]")
    st.info("Hello, my name is Dr. Zee.")
    name = st.text_input("What is your name")
    if name:
        name = name.capitalize()
        st.caption(":orange[**Dr.Zee :eyeglasses:**]")
        st.info(f"Nice to meet you {name}.")
        choices = ["Nice to meet you too", "Cool"]
        response = st.radio("Choose response :cat:", choices)
        if response == choices[0]:
            st.caption(f":blue[**{name} :eyeglasses:**]")
            st.info(choices[0])
            st.divider()
            st.caption(f":blue[**{name}** :]")

            st.info("Uh, hey Professor! You know, I've been hearing about this thing called Python. What is it?")
        else:
            st.caption(f":blue[**{name}** :]")
            st.info(choices[1])
            st.divider()
            st.caption("Episode 1: Into the Py Land")
            st.caption(f":blue[**{name}** :]")
            st.info("Uh, hey Professor! You know, I've been hearing about this thing called Python. What is it?")
            st.caption(":orange[**Dr.Zee :eyeglasses:**]")
            st.info(
                f"""
                    Oh, **{name}**! Python, huh? Python is like a programming language, 
                    buddy. It's a way for us humans to communicate with computers.
                    """)
            st.caption(f":blue[**{name}** :]")

            st.info(" Communicate with computers? Like, you mean we can talk to 'em?")
            st.caption(":orange[**Dr.Zee :eyeglasses:**]")
            
            st.info(f"""
                    Well, not exactly, **{name}**. It's more like giving them instructions, telling them what to do. 
                    You see, Python is a high-level language, which means it's designed to be easy for humans to read and write. 
                    It's like a fancy way of telling a computer what to do without getting all technical, buddy.
                """)
            st.caption(f":blue[**{name}** :]")
            resp = ["Oh, okay, I think I get it. So, what can you do with Python?", "I don't get it, please explain well."]
            resps = st.radio("Choose a response :cat:", resp)

python_definition()
