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

    def serialize(self, serializer):
        serializer.start_object('ingridient', str(self.id))
        serializer.add_property('name', self.name)

    def to_xml(self)->ET.Element:
        ingridient_node = ET.Element('ingridient')
        ingridient_node.set('ingridient_id', str(self.id))
        name_node = ET.SubElement(ingridient_node, 'name')
        name_node.text = self.name
        return ingridient_node

    def to_dict(self):
        return {
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        ingridient = cls(
            name=data["name"]
        )
        ingridient.id = data["id"]
        return ingridient


class Recipe:
    def __init__(self, name:str, numbers_of_servings:int, cooking_time:int, description:str):
        self.id = 0
        self.name = name
        self.numbers_of_servings = numbers_of_servings
        self.cooking_time = cooking_time
        self.description = description
        self.ingridients: List[Ingridient] = []
        self.posts: List[Post] = []

    def serialize(self, serializer):
        serializer.start_object('recipe', str(self.id))
        serializer.add_property('name', self.name)
        serializer.add_property('numbers_of_servings', str(self.numbers_of_servings))
        serializer.add_property('cooking_time', str(self.cooking_time))
        serializer.add_property('description', self.description)
        serializer.add_property('ingridients', self.ingridients)

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

    def to_dict(self):
        return {
            "name": self.name,
            "numbers_of_servings": self.numbers_of_servings,
            "cooking_time": self.cooking_time,
            "description": self.description,
            "ingridients_in_recipe": [ingridient.to_dict() for ingridient in self.ingridients]
        }

    @classmethod
    def from_dict(cls, data):
        recipe = cls(
            name=data["name"],
            numbers_of_servings=data["numbers_of_servings"],
            cooking_time=data["cooking_time"],
            description=data["description"]
        )
        recipe.id = data["id"]
        ingridients = [Ingridient.from_dict(ingridient_data) for ingridient_data in data["ingridients_in_recipe"]]
        recipe.ingridients = ingridients
        return recipe


class Category:
    def __init__(self, name:str):
        self.id = 0
        self.name = name
        self.posts: List[Post] = []

    def serialize(self, serializer):
        serializer.start_object('category', str(self.id))
        serializer.add_property('name', self.name)

    def to_xml(self)->ET.Element:
        category_node = ET.Element('category')
        category_node.set('category_id', str(self.id))
        name_node = ET.SubElement(category_node, 'name')
        name_node.text = self.name
        return category_node

    def to_dict(self):
        return {
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        category = cls(
            name=data["name"]
        )
        category.id = data["id"]
        return category


class Post:
    def __init__(self, name:str, author:str, description:str, category:Category):
        self.id = 0
        self.name = name
        self.author = author
        self.description = description
        self.recipe = None
        self.category = category
        self.comments: List[Comment] = []
        self.state = 'Created'

    def status(self, event):
        while True:
            if self.state == 'Created':
                if event == 'Delete Post':
                    self.state = 'Deleted'
                elif event == 'Update Post':
                    self.state = 'Updated'
            elif self.state == 'Updated':
                if event == 'Delete Post':
                    self.state = 'Deleted'
            elif self.state == 'Deleted':
                if event == 'Restore Post':
                    self.state = 'Created'
            yield self.state


    def serialize(self, serializer):
        serializer.start_object('post', str(self.id))
        serializer.add_property('name', self.name)
        serializer.add_property('author', self.author)
        serializer.add_property('description', self.description)
        serializer.add_property('recipe_id', str(self.recipe.id))
        serializer.add_property('category_id', str(self.category.id))

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

    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "description": self.description,
            "recipe": self.recipe.to_dict(),
            "category": self.category.to_dict(),
        }

    @classmethod
    def from_dict(cls, data):
        post = cls(
            name=data["name"],
            author=data["author"],
            description=data["description"],
            category=Category.from_dict(data["category"])
        )
        post.recipe = Recipe.from_dict(data["recipe"])
        return post


class Comment:
    def __init__(self, username:str, message:str, data_creating: datetime.date, post: Post):
        self.id = 0
        self.username = username
        self.message = message
        self.data_creating = data_creating
        self.post = post

    def serialize(self, serializer):
        serializer.start_object('recipe', str(self.id))
        serializer.add_property('author_username', self.username)
        serializer.add_property('message', self.message)
        serializer.add_property('data_creating', str(self.data_creating))
        serializer.add_property('post_id', self.post.id)

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

    def to_dict(self):
        return {
            "author_username": self.username,
            "message": self.message,
            "data_creating": str(self.data_creating),
            "post": self.post.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        comment = cls(
            username=data["author_username"],
            message=data["message"],
            data_creating=datetime.datetime.strptime(data["data_creating"], "%Y-%m-%d").date(),
            post=Post.from_dict(data["post"])
        )
        return comment
