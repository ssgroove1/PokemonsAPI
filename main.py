import telebot
from random import randint
from config import token

from logic import Pokemon
from logic import Wizzard
from logic import Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username) # Покемон от юзера
            bot.send_message(message.chat.id, f'Класс вашего покемона: Стандартный')
        elif chance == 2:
            pokemon = Wizzard(message.from_user.username)
            bot.send_message(message.chat.id, f'Класс вашего покемона: Маг')
        else:
            pokemon = Fighter(message.from_user.username)
            bot.send_message(message.chat.id, f'Класс вашего покемона: Боец')
        
        if pokemon.get_weight() >= 1000:
            pokemon.power += randint(45,95)
            pokemon.hp += randint(95,225)
            bot.send_message(message.chat.id, f"{pokemon.info()}\nВам выпал <b>ЛЕГЕНДАРНЫЙ</b> покемон!", parse_mode='HTML')
            bot.send_video(message.chat.id, pokemon.show_shiny_img())

        elif pokemon.get_weight() >= 500 and pokemon.get_weight() < 1000:
            pokemon.power += randint(25,45)
            pokemon.hp += randint(65,85)
            bot.send_message(message.chat.id, f"{pokemon.info()}\nВам выпал <b>РЕДКИЙ</b> покемон!", parse_mode='HTML')
            bot.send_video(message.chat.id, pokemon.show_img())
        else:
            bot.send_message(message.chat.id, f'{pokemon.info()}\nВам выпал <b>ОБЫЧНЫЙ</b> покемон!', parse_mode='HTML')
            bot.send_video(message.chat.id, pokemon.show_img())

        bot.send_message(message.chat.id, f'{pokemon.show_ability()}\n{pokemon.show_weight()}')
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

#@bot.message_handler(commands=['feed'])
#def feed(message):
#    pokemon = Pokemon(message.from_user.username)
#    pokemon = Wizzard(message.from_user.username)
#    pokemon = Fighter(message.from_user.username)
#    if message.from_user.username not in Pokemon.pokemons.keys():
#        bot.send_message(message.chat.id, f"У вас нету покемона!")
#    else:
#        bot.send_message(message.chat.id, f"{pokemon.tofeed()}")



# Показ покеомона
@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username] # Покемон от игрока
        
        if isinstance(pok, Fighter):
            bot.send_message(message.chat.id, f'Класс вашего покемона: Боец')
        elif isinstance(pok, Wizzard):
            bot.send_message(message.chat.id, f'Класс вашего покемона: Маг')
        else:
            bot.send_message(message.chat.id, f'Класс вашего покемона: Стандартный')

        if pok.get_weight() >= 1000:
            bot.send_message(message.chat.id, f"{pok.info()}\nУ вас <b>ЛЕГЕНДАРНЫЙ</b> покемон!", parse_mode='HTML')
            bot.send_video(message.chat.id, pok.show_shiny_img())

        elif pok.get_weight() >= 500 and pok.get_weight() < 1000:
            bot.send_message(message.chat.id, f"{pok.info()}\nУ вас <b>РЕДКИЙ</b> покемон!", parse_mode='HTML')
            bot.send_video(message.chat.id, pok.show_img())
        else:
            bot.send_message(message.chat.id, f'{pok.info()}\nУ вас <b>ОБЫЧНЫЙ</b> покемон!', parse_mode='HTML')
            bot.send_video(message.chat.id, pok.show_img())

        #bot.send_message(message.chat.id, message.from_user.username)
        bot.send_message(message.chat.id, f'{pok.show_ability()}\n{pok.show_weight()}')
    else:
        bot.send_message(message.chat.id, "Создайте вашего покемона!")



@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            if message.from_user.username:
                if enemy.hp <= 0:
                    bot.send_message(message.chat.id, f"{res}\nВраг потерял весь свой уровень, хп!")
                    enemy.poklevels = 1
                    enemy.hp = enemy.reserhp
                else:
                    bot.send_message(message.chat.id, f"{res}\nУ врага осталось {enemy.hp} единиц здоровья")
            else:
                bot.send_message(message.chat.id, f"{res}\nУ врага осталось {enemy.hp} единиц здоровья")
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

bot.infinity_polling(none_stop=True)