import datetime
from dataclasses import dataclass

@dataclass (frozen=True)
class Recipe:
    name: str
    numbers_of_servings: int
    cooking_time: int
    ingridients: []
    description: str

@dataclass (frozen=True)
class Category:
    name : str

class Post:
    def __init__(self, name:str, author:str, description:str, recipe:Recipe, category:Category):
        self.name = name
        self.author = author
        self.description = description
        self.recipe = recipe
        self.category = category

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.name == other.name and self.author == other.author and self.description == other.description and self.recipe == other.recipe and self.category == other.category
    
class Comment:
    def __init__(self, user_name:str, message:str, data_creating: datetime.date, post: Post):
        self.user_name = user_name
        self.message = message
        self.data_creating = data_creating
        self.post = post


    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.user_name == other.user_name and self.message == other.message and self.data_creating == other.data_creating and self.post == other.post
