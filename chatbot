# code in colab environment
# enter data cell by cell, with as few statements in one cell, as possible 

!pip install chatterbot
!pip install chatterbot_corpus
# Importing chatterbot
from chatterbot import ChatBot
# Create object of ChatBot class
bot = ChatBot('Buddy')
# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
'Buddy',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
'Buddy',  
    logic_adapters=[
'chatterbot.logic.BestMatch',
'chatterbot.logic.TimeLogicAdapter'],
)
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
# Train based on the english corpus
trainer.train("chatterbot.corpus.english")
# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")
# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")


name=input("Enter Your Name: ")
print("This is AITTA Chatbot Service. How can I help you...")

while True:
    request=input(name+':')
    if request=='Bye'or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)
