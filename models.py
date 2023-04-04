import datetime

class Recipe:
    def __init__(self, name:str, numbers_of_servings:int, cooking_time:int, ingridients:[], description:str):
        self.name = name
        self.numbers_of_servings = numbers_of_servings
        self.cooking_time = cooking_time
        self.ingridients = ingridients
        self.description = description

class Category:
    def __init__(self, name:str):
        self.name = name

class Post:
    def __init__(self, name:str, author:str, description:str, recipe:Recipe, category:Category):
        self.name = name
        self.author = author
        self.description = description
        self.recipe = recipe
        self.category = category
    
class Comment:
    def __init__(self, user_name:str, message:str, data_creating: datetime.date, post: Post):
        self.user_name = user_name
        self.message = message
        self.data_creating = data_creating
        self.post = post

