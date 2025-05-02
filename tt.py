import random
import json

agressive_replies=[]
with open('C:/Users/SashkaChugun/Desktop/unik/agressive_replies.json','r', encoding='UTF-8') as file:
    agressive_replies=json.load(file)

print(agressive_replies[random.randint(0,len(agressive_replies))-1])