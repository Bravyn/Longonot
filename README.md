# Learn Python For Kids: Professor Zee 🐍

Welcome to **Learn Python For Kids**! This fun and interactive application is designed to help young learners understand the basics of Python programming through a friendly guide, Professor Zee! With the help of OpenAI's GPT-4, the app provides explanations and answers to Python-related queries in simple, easy-to-understand terms.

## Project Overview

This project features a Streamlit app that:
- Provides a friendly environment for kids to learn Python.
- Utilizes OpenAI's GPT-4 to answer Python-related questions in a conversational manner.
- Guides users through interactive learning sessions, making it an engaging experience.

Professor Zee, the Python expert, is always ready to explain programming concepts and answer questions in a fun and supportive way.

## Features

- **Interactive Python Learning**: Users can interact with Professor Zee by asking questions and receiving simple explanations about Python programming.
- **Personalized Experience**: The app asks for the user's name and tailors responses accordingly, creating a more personalized experience.
- **Continuous Learning**: Users can ask follow-up questions or choose to learn more about various Python topics.
  
## Technologies Used

- **Streamlit**: Used for creating the interactive user interface.
- **OpenAI GPT-4**: Powers the conversational responses and explanations.
- **dotenv**: Used to manage environment variables securely (e.g., OpenAI API key).

## Installation

### Prerequisites

- Python 3.7 or later.
- An OpenAI API key (Sign up at [OpenAI](https://platform.openai.com/) to get your key).

### Steps to Set Up

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/yourusername/learn-python-for-kids.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your-api-key-here
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501` to start interacting with Professor Zee!

## How It Works

- The user is greeted by Professor Zee and can input their name.
- The app then prompts the user to ask a question or request help with learning Python.
- The user's query is sent to OpenAI's GPT-4, which responds with a simple, kid-friendly explanation of the topic.
- The user can continue asking questions or choose to end the session.

## Example Interaction

- **User:** "What is a variable in Python?"
- **Professor Zee:** "A variable in Python is like a box where you can store information. You can give the box a name and put something inside it, like a number or a word. Later, you can open the box and use that information in your program."

## Contributing

Feel free to fork this project, improve it, and submit pull requests. If you have any ideas for new features or improvements, we'd love to hear them!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Enjoy learning Python with Professor Zee! 🎉
```

This README provides clear instructions on setting up and running the app, along with details about its functionality, technologies used, and an example interaction.