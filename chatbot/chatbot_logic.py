from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
from django.conf import settings

# with open('M:\Python projects\Assignment_2\Django_Week4\A_Django_Project\chatbot\QnA_chatbot.json', 'r') as f:
with open('chatbot/QnA_chatbot.json', 'r') as f:
    qa_data = f.read()

qa_json = json.loads(qa_data)

train = []

for k, r in enumerate(qa_json):
    train.append(r['question'])
    train.append(r['answer'])

chatbot = ChatBot('Jarvis')
trainer = ListTrainer(chatbot)

trainer.train(train)


def talk(msg):
    return chatbot.get_response(msg)
