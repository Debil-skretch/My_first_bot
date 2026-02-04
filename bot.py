from telebot.types import ReactionTypeEmoji
import random
import telebot
from bot_logic import flip_coin, gen_pass
TOKEN = "Write yiur TOKEN"
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
    bot.reply_to(message, "/start - нужна для того чтобы начать,/hello - нужна если хочешь поздоровоться с ботом,/bye - нужна если хочешь попрощаться с ботом,password- нужна если хочешь сгенирировать рандомный парольиз 10 символов")

@bot.message_handler(func=lambda message: True)
def send_reaction(message):
    emo = ["\U0001F525", "\U0001F917", "\U0001F60E", "\xF0\x9F\x98\x8D"]  
    bot.set_message_reaction(message.chat.id, message.id, [ReactionTypeEmoji(random.choice(emo))], is_big=False)

@bot.message_reaction_handler(func=lambda message: True)
def get_reactions(message):
    bot.reply_to(message, f"You changed the reaction from {[r.emoji for r in message.old_reaction]} to {[r.emoji for r in message.new_reaction]}")

bot.infinity_polling(allowed_updates=['message', 'message_reaction'])

bot.polling()
