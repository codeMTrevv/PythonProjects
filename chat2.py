# import requests
import nltk
from nltk.chat.util import Chat, reflections

#List of patterns and their responses.
pairs = [
    [
        r"i am (.*)",
        ["Hello %2, How are you today?",]
    ],
    [
        
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you "]
    ],
     [
        r"(.*) your name ?",
        ["My name is Atreus, but you can just call me robot and I'm a chatbot."]
    ],
    [
        r"(.*) how are you ?",
        ["I'm doing very well", "i am great!"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that"]
    ],
    [
        r"i am (.*) (good|well|okay|ok)",
        ["Nice to hear that %2","Alright, great!"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
        
    ],
    [
        r"(.*)created(.*)",
        ["My master's name is The Great Trevlon.He created me using Python's NLTK library and some code he stole from the internet. ","top secret ;)"]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India']
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health "]
    ],
    [
        r"What is your favorite sport (.*)?",
        ["i don't have a facorite sport %2"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        [' I am sorry, there is no response to that in my programming. Updating...']
    ]
]
#Output
reflections = {'i am': 'you are','i was': 'you were','i': 'you',
"i'm": 'you are',
"i'd": 'you would',
"i've": 'you have',
"i'll": 'you will',
'my': 'your',
'you are': 'I am',
'you were': 'I was',
"you've": 'I have',
"you'll": 'I will',
'your': 'my',
'yours': 'mine',
'you': 'me',
'me': 'you'}

#default message at the start of chat
print("Hi, I'm Atreus and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

#Start conversation
chat.converse()