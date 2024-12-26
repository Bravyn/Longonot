import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API Key (replace 'your-openai-api-key' with your actual key)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.secrets["openai"]["api_key"]

# Streamlit page configuration
st.set_page_config("Professor Zee", ":glasses:")
st.title(":blue[Learn Python For Kids :computer:]")
st.subheader("Professor Zee. :eyeglasses:")

# Display introductory message to engage users
st.markdown("""
    Welcome to **Learn Python For Kids**! :snake:  
    Here, you'll get to explore Python in a fun way. Ask me anything about Python, 
    and I'll be your guide through the amazing world of programming.
""")

# Function to get GPT-4 response for user queries
def get_gpt_response(query):
    try:
        # Make a request to the OpenAI API
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are a python teacher.Teach me about {query}"
                    ),
                },
            ],
            max_tokens=500,
            temperature=0.7,
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"Sorry, something went wrong: {e}"

# Function to handle user interaction and learning about Python
def python_definition():
    st.divider()
    st.caption(":orange[**Dr. Zee :eyeglasses:**]")
    st.info("Hello, my name is Dr. Zee. I am the Python :snake: Master  ")
    
    # Get user's name
    name = st.text_input("What is your name?")
    if name:
        name = name.capitalize()
        st.caption(":orange[**Dr. Zee :eyeglasses:**]")
        st.info(f"Nice to meet you, {name}. Let's get started!")
        
        # GPT-4: Ask user to introduce themselves or ask any question about Python
        st.caption(f":blue[**{name}** :]")
        user_question = st.text_input(f"Hi, {name}! What would you like to learn or ask about Python?")

        if user_question:
            # Send the user's query to GPT-4 for a dynamic response
            gpt_response = get_gpt_response(f"{name} is a beginner and asks: {user_question}. Explain it in simple terms.")
            st.caption(":orange[**Dr. Zee :eyeglasses:**]")
            st.info(gpt_response)

            # Follow-up: Ask the user if they want to learn more
            follow_up = st.radio("Would you like to learn more or ask another question?", ["Yes, tell me more!", "No, I'm good for now."])

            if follow_up == "Yes, tell me more!":
                # Provide the option to continue exploring or ask new questions
                python_definition()
            else:
                st.info(f"Great job, {name}! You've made progress. See you next time!")

# Call the function to start the Python learning interaction
python_definition()
