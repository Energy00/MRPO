from abc import ABC, abstractmethod
from models import *


class abstract_repository(ABC):
    @abstractmethod
    def add(self, someextension):
        pass

    @abstractmethod
    def delete_id(self, id):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def readAll(self):
        pass


class CategoryRepository(abstract_repository):
    def __init__(self):
        self.Categories = {}
        self.id_counter = 1

    def add(self, category: Category):            
        self.Categories[self.id_counter] = category
        self.id_counter += 1
        
    def delete_id(self, id: int):
        self.Categories.pop(id)

    def update(self, new_category: Category, id: int):
        self.Categories[id] = new_category

    def readAll(self):
        for c in self.Categories:
            print(c,self.Categories[c].name)


class RepiceRepository(abstract_repository):
    def __init__(self):
        self.Recipes = {}
        self.id_counter = 1

    def add(self, recipe: Recipe):            
        self.Recipes[self.id_counter] = recipe
        self.id_counter += 1
        
    def delete_id(self, id: int):
        self.Recipes.pop(id)

    def update(self, new_recipe: Recipe, id: int):
        self.Recipes[id] = new_recipe

    def readAll(self):
        for r in self.Recipes:
            print(r, self.Recipes[r].name, self.Recipes[r].numbers_of_servings, self.Recipes[r].cooking_time, self.Recipes[r].ingridients, self.Recipes[r].description)


class PostRepository(abstract_repository):
    def __init__(self):
        self.Posts = {}
        self.id_counter = 1

    def add(self, post: Post):            
        self.Posts[self.id_counter] = post
        self.id_counter += 1
        
    def delete_id(self, id: int):
        self.Posts.pop(id)

    def update(self, new_post: Post, id: int):
        self.Posts[id] = new_post

    def readAll(self):
        for p in self.Posts:
            return('id - ', p, '\nИмя - ', self.Posts[p].name, '\nАвтор - ', self.Posts[p].author, '\nОписание - ', self.Posts[p].description, '\nИмя категории - ', self.Posts[p].category.name, '\Имя рецепта -  ', self.Posts[p].recipe.name)


class CommentRepository(abstract_repository):
    def __init__(self):
        self.Comments = {}
        self.id_counter = 1

    def add(self, comment: Comment):            
        self.Comments[self.id_counter] = comment
        self.id_counter += 1
        
    def delete_id(self, id: int):
        self.Comments.pop(id)

    def update(self, new_comment: Comment, id: int):
        self.Comments[id] = new_comment

    def readAll(self):
        for c in self.Comments:
            print(c, self.Comments[c].user_name, self.Comments[c].message, self.Comments[c].data_creating, self.Comments[c].post.name)