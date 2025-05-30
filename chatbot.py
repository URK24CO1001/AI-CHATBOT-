from nltk.chat.util import Chat, reflections


pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I'm a chatbot."]],
    ["how are you?", ["I'm fine, thank you!"]],
    ["what can you do?", ["I can answer simple questions."]],
    ["bye", ["Goodbye!", "See you later!"]],
]


chatbot = Chat(pairs, reflections)


def start_chat():
    print("Welcome! Type 'bye' to exit.")
    chatbot.converse()


start_chat()
