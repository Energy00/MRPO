import datetime
from dataclasses import dataclass
import sqlalchemy as sa


class Ingridient:
    def __init__(self, name:str):
        self.name = name
        self.recipes = []

class Recipe:
    def __init__(self, name:str, numbers_of_servings:int, cooking_time:int, description:str):
        self.name = name
        self.numbers_of_servings = numbers_of_servings
        self.cooking_time = cooking_time
        self.description = description
        self.ingridients = []
        self.posts = []

class Category:
    def __init__(self, name:str):
        self.name = name
        self.posts: []

class Post:
    def __init__(self, name:str, author:str, description:str, category:Category):
        self.name = name
        self.author = author
        self.description = description
        self.recipe = None
        self.category = category
        self.comments = []

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.name == other.name and self.author == other.author and self.description == other.description and self.recipe == other.recipe and self.category == other.category and self.comments == other.comments
    
class Comment:
    def __init__(self, username:str, message:str, data_creating: datetime.date, post: Post):
        self.username = username
        self.message = message
        self.data_creating = data_creating
        self.post = post


    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.user_name == other.user_name and self.message == other.message and self.data_creating == other.data_creating and self.post == other.post
