from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
from django.conf import settings

# with open('M:\Python projects\Assignment_2\Django_Week4\A_Django_Project\chatbot\QnA_chatbot.json', 'r') as f:
with open('chatbot/QnA_chatbot.json', 'r') as f:
    qa_data = f.read()

# Store the json data in variable.
qa_json = json.loads(qa_data)

# Create blank list and store in train variable.
train = []

# Append questions and answers in json data to train list.
for k, r in enumerate(qa_json):
    train.append(r['question'])
    train.append(r['answer'])

# Create CHatBot object called Jarvis, assign to chatbot variable.
chatbot = ChatBot('Jarvis')
# Use ListTrainer as the trainer for the chatbot.
trainer = ListTrainer(chatbot)
# Train the chatbot.
trainer.train(train)

# Create talk function to be used. Allows chatbot to respond to question.
def talk(msg):
    return chatbot.get_response(msg)
