from bs4 import BeautifulSoup
import json
import telebot
import random

admid=open("C:/Users/SashkaChugun/Desktop/unik/admid.txt","r")
best_id=admid.read().split(', ')

jertvalist=[]
jertvaname=[]

agressive=6

replies=[]
with open('C:/Users/SashkaChugun/Desktop/unik/replies.json','r', encoding='UTF-8') as file:
    replies=json.load(file)
    
agressive_replies=[]
with open('C:/Users/SashkaChugun/Desktop/unik/agressive_replies.json','r', encoding='UTF-8') as file:
    agressive_replies=json.load(file)

filetoken = open("C:/Users/SashkaChugun/Desktop/unik/token.txt","r")
bot = telebot.TeleBot(filetoken.read())

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """ЧЕ""")
    
@bot.message_handler(commands=['mrpenis'])
def sendstick(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEOz8BoFOm4t90jS9ZDIUx3hBKr3IA2iAACgjMAAne6YEpQ0Iqq-eXZxjYE')

@bot.message_handler(commands=['jertva','jertvi'])
def jertva(message):
    bot.reply_to(message, f"Жертвы бота в данный момент: {jertvaname}")
    
@bot.message_handler(commands=['agressive'])
def agress(message):
    bot.reply_to(message, f"Агрессивность бота в данный момент: {agressive}")
    
@bot.message_handler(commands=['del'])
def jertvadel(message):
    try:
        jertva=message.reply_to_message.from_user.id
        jertvanick = message.reply_to_message.from_user.username
    except:
        print('Не удалось получить id/username')
        
    if jertva in jertvalist:
        if str(message.from_user.id) not in best_id:
            bot.reply_to(message, "Заячью губу поправь")
        else:
            jertvalist.remove(jertva)
            jertvaname.remove(jertvanick)
            bot.reply_to(message, f"{jertvanick} отныне не проклят")
    else:
        bot.reply_to(message, f"{jertvanick} нету в списке жертв")
        
@bot.message_handler(commands=['curse'])
def jertvaset(message):
    
    try:
        jertva=message.reply_to_message.from_user.id
        jertvanick = message.reply_to_message.from_user.username
    except:
        print('Не удалось получить id/username')
        
    if jertva in jertvalist:
        bot.reply_to(message, f"Этот бро уже в списке")
    else:
        if str(message.from_user.id) not in best_id:
            bot.reply_to(message, "Заячью губу поправь")
        else:
            jertvalist.append(jertva)
            jertvaname.append(jertvanick)
            bot.reply_to(message, f"В жертвы бота добавлен: {jertvanick}")
            
@bot.message_handler(commands=['setagressive'])
def agressiveset(message):
    global agressive
    if str(message.from_user.id) not in best_id:
        bot.reply_to(message, "Заячью губу поправь")
    else:
        args = message.text.split()[1:]
        text = ' '.join(args)
        agressive=int(text)
        bot.reply_to(message, f"Агрессивность бота установленна на {agressive}")

@bot.message_handler(func=lambda message: message.from_user.id in jertvalist)
def handle_specific_user(message):
    global agressive
    if agressive>7:
        if random.randint(0,10-agressive)==0:   
            bot.reply_to(message, agressive_replies[random.randint(0,len(agressive_replies))-1])
    else:
        if random.randint(0,10-agressive)==0:   
            bot.reply_to(message, replies[random.randint(0,len(replies))-1])
            
if __name__=='__main__':
    bot.infinity_polling() 