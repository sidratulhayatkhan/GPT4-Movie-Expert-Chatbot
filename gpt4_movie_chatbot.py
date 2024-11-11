import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def get_movie_suggestion(user_input):
    """
    Sends user input to OpenAI GPT-4 model to get a movie suggestion.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in movies. Your role is to suggest movies based on user feelings, mood, or genre preference."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=100
    )
    return response['choices'][0]['message']['content']

def main():
    print("Welcome to the GPT-4 Movie Expert Chatbot!")
    print("Ask for a movie suggestion based on your mood or preference.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Enjoy your movie!")
            break
        suggestion = get_movie_suggestion(user_input)
        print("Chatbot:", suggestion)

if __name__ == "__main__":
    main()
