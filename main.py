import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_video(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, f'{pokemon.show_ability()}\n{pokemon.show_weight()}')
        bot.send_message(message.chat.id, pokemon.show_link())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)

