from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.weight = self.get_weight()
        self.link = self.get_link()

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
        
    def get_link(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['id'])
        else:
            return "bug"


    # Метод класса для получения информации
    def info(self):
        return f"Имя вашего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def show_ability(self):
        return f"Способность вашего покеомона: {self.ability}"
    
    def show_weight(self):
        return f"Вес вашего покеомона: {self.weight} КГ"
    
    def show_link(self):
        return f'Больше информации о вашем покеомоне тут: https://pokeapi.co/api/v2/pokemon/{self.link}'



