import datetime
from dataclasses import dataclass
import sqlalchemy as sa
import xml.etree.ElementTree as ET
from typing import List


class Ingridient:
    def __init__(self, name:str):
        self.id = 0
        self.name = name
        self.recipes: List[Recipe] = []

    def to_xml(self)->ET.Element:
        ingridient_node = ET.Element('ingridient')
        ingridient_node.set('ingridient_id', str(self.id))
        name_node = ET.SubElement(ingridient_node, 'name')
        name_node.text = self.name
        return ingridient_node


class Recipe:
    def __init__(self, name:str, numbers_of_servings:int, cooking_time:int, description:str):
        self.id = 0
        self.name = name
        self.numbers_of_servings = numbers_of_servings
        self.cooking_time = cooking_time
        self.description = description
        self.ingridients: List[Ingridient] = []
        self.posts: List[Post] = []

    def to_xml(self)->ET.Element:
        recipe_node = ET.Element('recipe')
        recipe_node.set('recipe_id', str(self.id))
        name_node = ET.SubElement(recipe_node, 'name')
        name_node.text = self.name
        numbers_of_servings_node = ET.SubElement(recipe_node, 'numbers_of_servings')
        numbers_of_servings_node.text = str(self.numbers_of_servings)
        cooking_time_node = ET.SubElement(recipe_node, 'cooking_time')
        cooking_time_node.text = str(self.cooking_time)
        description_node = ET.SubElement(recipe_node, 'description')
        description_node.text = self.description
        ingridients_node = ET.SubElement(recipe_node, 'ingridients')
        for ingridient in self.ingridients:
            ingridients_node.append(ingridient.to_xml())
        return recipe_node      

class Category:
    def __init__(self, name:str):
        self.id = 0
        self.name = name
        self.posts: List[Post] = []

    def to_xml(self)->ET.Element:
        category_node = ET.Element('category')
        category_node.set('category_id', str(self.id))
        name_node = ET.SubElement(category_node, 'name')
        name_node.text = self.name
        return category_node

class Post:
    def __init__(self, name:str, author:str, description:str, category:Category):
        self.id = 0
        self.name = name
        self.author = author
        self.description = description
        self.recipe = None
        self.category = category
        self.comments: List[Comment] = []

    def __eq__(self, other):
        if isinstance(other, Post):
            return self.name == other.name and self.author == other.author and self.description == other.description and self.recipe == other.recipe and self.category == other.category and self.comments == other.comments
    
    def to_xml(self)->ET.Element:
        post_node = ET.Element('post')
        post_node.set('post_id', str(self.id))
        name_node = ET.SubElement(post_node, 'name')
        name_node.text = self.name
        author_node = ET.SubElement(post_node, 'author')
        author_node.text = self.author
        description_node = ET.SubElement(post_node, 'description')
        description_node.text = self.description
        recipe_node = ET.SubElement(post_node, 'recipe')
        recipe_node.text = str(self.recipe.id)
        category_node = ET.SubElement(post_node, 'category')
        category_node.text = str(self.category.id)
        return post_node

class Comment:
    def __init__(self, username:str, message:str, data_creating: datetime.date, post: Post):
        self.id = 0
        self.username = username
        self.message = message
        self.data_creating = data_creating
        self.post = post


    def __eq__(self, other):
        if isinstance(other, Comment):
            return self.user_name == other.user_name and self.message == other.message and self.data_creating == other.data_creating and self.post == other.post

    def to_xml(self)->ET.Element:
        comment_node = ET.Element('comment')
        comment_node.set('comment_id', str(self.id))
        username_node = ET.SubElement(comment_node, 'author_username')
        username_node.text = self.username
        message_node = ET.SubElement(comment_node, 'message')
        message_node.text = self.message
        data_node = ET.SubElement(comment_node, 'data_creating')
        data_node.text = str(self.data_creating)
        post_node = ET.SubElement(comment_node, 'post')
        post_node.text = str(self.post.id)
        return comment_node