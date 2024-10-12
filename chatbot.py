import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a simple AI chatbot."]
    ],
    [
        r"how are you?",
        ["I'm doing great, thank you! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no worries."]
    ],
    [
        r"quit",
        ["Goodbye! It was nice talking to you."]
    ],
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def chat():
    print("Hi! I am your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
