import requests
from telebot.types import ReactionTypeEmoji
import random
import os
import telebot
from bot_logic import flip_coin, gen_pass
TOKEN = 
bot = telebot.TeleBot(TOKEN)

    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я первый Telegram бот своего создателя. Напиши что-нибудь!")
   
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/start - нужна для того чтобы начать,/hello - нужна если хочешь поздоровоться с ботом,/bye - нужна если хочешь попрощаться с ботом,/password- нужна если хочешь сгенирировать рандомный парольиз 10 символов,/coin - нужна для того чтобы подбросить монетку,/mem - эта команда выдет один мем про програмистов,/God of War - эта команда выдает один мем про God of War,/duck - эта команда перекидывает на сайт с крутыми утками.")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['God of War'])
def send_mem(message):
    img_name = random.choice(os.listdir('animal_images'))
    with open(f'animal_images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)        

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['Eco'])
def eco(message):
    bot.reply_to(message, "Режим помощи в защите окружающей среды активирован")

facts = ["Стекло разлагается более 1000лет!!!!!", "В море в год от мусора погибает более 1м рыб!!!!","В некоторых местах мира на столько грязно что там сложно дышать"]
random_facts = random.choice(facts)

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    if message.text == "Как можно использовать пластиковые бутылки?":
        bot.reply_to(message,"Их можно использовать как многоразовую тару , сдать на переработку или в быту ")
    elif message.text == "Какие есть факты о экологии?":
         bot.reply_to(message,random_facts)
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E", "\xF0\x9F\x98\x8D"]  
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)

@bot.message_reaction_handler(func=lambda message: True)
def get_reactions(message):
    bot.reply_to(message, f"You changed the reaction from {[r.emoji for r in message.old_reaction]} to {[r.emoji for r in message.new_reaction]}")

bot.infinity_polling(allowed_updates=['message', 'message_reaction'])

bot.polling()






























