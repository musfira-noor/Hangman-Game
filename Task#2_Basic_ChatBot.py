import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random   

# Initialize NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Define a dictionary of responses
responses = {
    'greeting': ['Hello!', 'Hi!', 'Hey!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Farewell!'],
    'thanks': ['You\'re welcome!', 'No problem!', 'Anytime!'],
    'weather': ['Weather', 'Forecast', 'Temperature'],
    'unknown': ['I didn\'t understand that.', 'Can you please rephrase?', 'Sorry, I\'m not sure what you mean.'],
    'joke': ['You are so intelligent:)'],
    'news': ['I don\'t have news updates, but you can check a news website for the latest headlines.'],
    'sports': ['I\'m not up-to-date with sports scores, but you can check a sports website for the latest scores.'],
    'music': ['I love music too! What’s your favorite genre?'],
    'movie': ['I enjoy movies! What genre do you like?'],
    'name': ['Chatbot', 'I\'m chatbot'],
    'talk1': ['Fine, What about you?', 'Fine', 'I\'m ok.'],
    'talk2' :['I\'m chatting with you.'],
    'talk3':['For chatting with you', 'Help to you'],
    'goal':['I am here to help you'],
    'dev':['Musfira developed me','Musfira'],
    'talk5':['OK', 'Alright'],
    


}

# Define a dictionary of intents
intents = {
    'greeting': ['hello', 'hi', 'hey', 'hi there'],
    'goodbye': ['goodbye', 'bye', 'see you later', 'farewell'],
    'thanks': ['thanks', 'thank you', 'appreciate it'],
    'weather': ['weather', 'forecast', 'temperature'],
    'joke': ['tell me a joke', 'joke'],
    'news': ['what\'s the news?', 'news', 'headlines'],
    'sports': ['sports', 'score', 'game'],
    'music': ['music', 'song', 'band'],
    'movie': ['movie', 'film', 'cinema'],
    'name': ['who are you', 'who'],
    'talk1': ['how are you', 'how'],   
    'talk2': ['what are you doing','what'],
    'talk3': ['what is your purpose','purpose'],
    'goal': ['your goal','goal'],
    'dev': ['Your developer','developer'],
    'talk5':['ok','alright']
    
}

# Define a lemmatizer
lemmatizer = WordNetLemmatizer()

# def get_weather():
#     return "The current weather is Sunny."

# Define a function to tokenize and lemmatize user input
def process_input(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

# Define a function to determine the intent of the user input
def determine_intent(lemmas):
    for intent, keywords in intents.items():
        for keyword in keywords:
            if any(keyword in lemmas for lemmas in lemmas):
                return intent
    return 'unknown'

# Define a function to respond to the user
def respond(intent):
    # if intent == 'weather':
    #     return get_weather()
    responses_list = responses.get(intent, responses['unknown'])
    return random.choice(responses_list)

# Define a main function to run the chatbot
def main():
    print('Welcome to the chatbot!')
    while True:
        user_input = input('You: ')
        lemmas = process_input(user_input)
        print(f"Debug: Lemmas - {lemmas}")
        intent = determine_intent(lemmas)
        print(f"Debug: Detected Intent - {intent}")
        response = respond(intent)
        print('Chatbot:', response)

if __name__ == '__main__':
    main()