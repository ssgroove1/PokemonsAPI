from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer): # pokemon_trainer это и есть Pokemon(message.from_user.username)

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.shinyimg = self.get_shiny_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.weight = self.get_weight()

        self.poklevels = 1

        self.randomhp = randint(200,400)
        self.hp = self.randomhp
        self.reserhp = self.randomhp
        
        self.power = randint(30,60)


        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["sprites"]['other']['showdown']["front_default"]
        else:
            return "No image" # Если будет ошибка 404 или 505 и тд то пишет "no image"
        
    def get_shiny_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["sprites"]['other']['showdown']["front_shiny"]
        else:
            return "No shiny image" # Если будет ошибка 404 или 505 и тд то пишет "no image"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name']) # [0] - нулевой список
        else:
            return "Pikachu" # Если будет ошибка 404 или 505 и тд то пишет "Pikachu"
        
    def get_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]['ability']['name']) # [0] - нулевой список
        else:
            return "error"
        
    def get_weight(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["weight"])
        else:
            return "?"


    # Метод класса для получения информации
    def info(self):
        data = (
            f"Имя вашего покемона: {self.name}\n"
            f"Сила покемона: {self.power}\n"
            f"Здоровье покемона: {self.hp}\n"
            f"Уровень покемона: {self.poklevels}"
        )
        return data

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_shiny_img(self):
        return self.shinyimg
    
    def show_ability(self):
        return f"Способность: {self.ability}"
    
    def show_weight(self):
        return f"Вес: {self.weight} КГ"
    

    # Метод атаки покемона
    def attack(self, enemy):
        if isinstance(enemy, Wizzard):
            chance = randint(1,5)
            if chance == 3:
                return "Покемон-волшебник применил щит в сражение"

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        
        else:
            enemy.hp = 0
            self.hp = self.reserhp
            if self.poklevels >= 100:
                self.poklevels = 100
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\nВаш покемон достиг максимального уровня: {self.poklevels} "
            else:
                self.poklevels += randint(1,3)
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!\nНовый уровень вашего покемона: {self.poklevels} "
        

    # Метод комрления
    #def tofeed(self):
    #    if self.poklevels >= 100:
    #        return f"Ваш покемон достиг максимального уровня!\nУровень вашего покемона: {self.poklevels}"
    #    else:
    #        f = self.poklevels + randint(2,7)
    #        print(f)
    #        return f"Вы покормили вашего покемона!\nНовый уровень вашего покемона: {self.poklevels}"


class Wizzard(Pokemon):
    def attack(self, enemy):
        ghh1 = randint(1,2)
        if ghh1 == 1:
            magic_power = randint(3,14)
            self.power += magic_power
            result = super().attack(enemy)
            self.power -= magic_power
            totalpower = magic_power+self.power
            return result + f"\nМаг применил магический удар силою {totalpower}"
        else:
            result = super().attack(enemy)
            return result

class Fighter(Pokemon):
    def attack(self, enemy):
        ghh = randint(1,3)
        if ghh == 2:
            super_power = randint(7,23)
            self.power += super_power
            result = super().attack(enemy)
            self.power -= super_power
            totalpower = super_power+self.power
            return result + f"\nБоец применил супер-атаку силою {totalpower}"
        else:
            result = super().attack(enemy)
            return result



#if __name__ == '__main__':
    #wizard = Wizzard("username1")
    #fighter = Fighter("username2")

    #print(wizard.info())
    #print()
    #print(fighter.info())
    #print()
    #print(fighter.attack(wizard))