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
        self.comments = []

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.name == other.name and self.author == other.author and self.description == other.description and self.recipe == other.recipe and self.category == other.category and self.comments == other.comments
    
class Comment:
    def __init__(self, user_name:str, message:str, data_creating: datetime.date, post: Post):
        self.user_name = user_name
        self.message = message
        self.data_creating = data_creating
        self.post = post
        post.comments.append(self)


    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.user_name == other.user_name and self.message == other.message and self.data_creating == other.data_creating and self.post == other.post


def len_description_post(post: Post):
    return len(post.description)

def count_ingridients_recipe(recipe: Recipe):
    return len(recipe.ingridients)

def count_comment_post(post: Post):
    return len(post.comments)

def sort_comment_on_date(post: Post, data: datetime.date, sign: str):
    sortComment = []
    if sign == '>':
        for c in post.comments:
            if c.data_creating > data: 
                sortComment.append(c)
    elif sign == '<':
        for c in post.comments:
            if c.data_creating < data: 
                sortComment.append(c)
    else: 
        for c in post.comments:
            sortComment.append(c)
    return sortComment
