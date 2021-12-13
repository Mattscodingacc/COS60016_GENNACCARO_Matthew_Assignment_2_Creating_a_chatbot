from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

with open('QnA_chatbot.json', 'r') as jfile:
    qa_data = jfile.read()

qa_json = json.loads(qa_data)
train = []

for k, r in enumerate(qa_json):
    train.append(r['question'])
    train.append(r['answer'])

qa_chatbot = ChatBot('Jarvis')
trainer = ListTrainer(qa_chatbot)

trainer.train(train)

while True:
    request = input("You: ")
    response = qa_chatbot.get_response(request)
    print("Jarvis: ", response)
