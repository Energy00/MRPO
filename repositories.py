from abc import ABC, abstractmethod
from models import *
from sqlalchemy.orm import Session
from typing import Optional
import os
import json


class abstract_repository(ABC):
    @abstractmethod
    def add(self, someobject):
        pass

    @abstractmethod
    def delete_by_id(self, someobject):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass


#JSON
class CategoryJSONRepository(abstract_repository):
    def __init__(self, data, file):
        self.data = data
        self.dict_data = []
        self.json_file = file
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, category: Category):
        if len(self.get_all()) > 0:
            categories = self.get_all()
            categories.append(category)
            self.dict_data = categories
            self.counter += 1
        else:
            self.dict_data.append(category)
            categories = self.dict_data
            self.counter += 1 
        self._save_data(categories)
        
    def delete_by_id(self, id: int):
        categories = self.get_all()
        categories = [category for category in categories if category.id != id]
        self._save_data(categories)

    def get_by_id(self, id:int)->Optional[Category]:
        categories = self.get_all()
        for category in categories:
            if category.id == id:
                return category
        return None

    def get_all(self)->List[Category]:
        if os.stat(self.json_file).st_size == 0:
            return []
        with open(self.json_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            categories_data = data.get("categories", [])
            categories = [Category.from_dict(category_data) for category_data in categories_data]
            return categories
        
    def _save_data(self, categories: List[Category]):
        self.data["categories"] = [category.to_dict() for category in categories]   


class IngridientJSONRepository(abstract_repository):
    def __init__(self, data, file):
        self.data = data
        self.dict_data = []
        self.json_file = file
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, ingridient: Ingridient):
        if len(self.get_all()) > 0:
            ingridients = self.get_all()
            ingridients.append(ingridients)
            self.dict_data = ingridients
            self.counter += 1
        else:
            self.dict_data.append(ingridient)
            ingridients = self.dict_data
            self.counter += 1
        self._save_data(ingridients)
        
    def delete_by_id(self, id: int):
        ingridients = self.get_all()
        ingridients = [ingridient for ingridient in ingridients if ingridient.id != id]
        self._save_data(ingridients)

    def get_by_id(self, id:int)->Optional[Ingridient]:
        ingridients = self.get_all()
        for ingridient in ingridients:
            if ingridient.id == id:
                return ingridient
        return None

    def get_all(self)->List[Ingridient]:
        if os.stat(self.json_file).st_size == 0:
            return []
        with open(self.json_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            ingridients_data = data.get("ingridients", [])
            ingridients = [Ingridient.from_dict(ingridient_data) for ingridient_data in ingridients_data]
            return ingridients
        
    def _save_data(self, ingridients: List[Ingridient]):
        self.data["ingridients"] = [ingridient.to_dict() for ingridient in ingridients]  


class RecipeJSONRepository(abstract_repository):
    def __init__(self, data, file):
        self.data = data
        self.dict_data = []
        self.json_file = file
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, recipe: Recipe):
        if len(self.get_all()) > 0:
            recipes = self.get_all()
            recipes.append(recipe)
            self.dict_data = recipes
            self.counter += 1
        else:
            self.dict_data.append(recipe)
            recipes = self.dict_data
            self.counter += 1
        self._save_data(recipes)
        
    def delete_by_id(self, id: int):
        recipes = self.get_all()
        recipes = [recipe for recipe in recipes if recipe.id != id]
        self._save_data(recipes)

    def get_by_id(self, id:int)->Optional[Recipe]:
        recipes = self.get_all()
        for recipe in recipes:
            if recipe.id == id:
                return recipe
        return None

    def get_all(self)->List[Recipe]:
        if os.stat(self.json_file).st_size == 0:
            return []
        with open(self.json_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            recipes_data = data.get("recipes", [])
            recipes = [Recipe.from_dict(recipe_data) for recipe_data in recipes_data]
            return recipes
        
    def _save_data(self, recipes: List[Recipe]):
        self.data["recipes"] = [recipe.to_dict() for recipe in recipes]  


class PostJSONRepository(abstract_repository):
    def __init__(self, data, file):
        self.data = data
        self.dict_data = []
        self.json_file = file
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, post: Post):
        if len(self.get_all()) > 0:
            posts = self.get_all()
            posts.append(post)
            self.dict_data = posts
            self.counter += 1
        else:
            self.dict_data.append(post)
            posts = self.dict_data
            self.counter += 1
        self._save_data(posts)
        
    def delete_by_id(self, id: int):
        posts = self.get_all()
        posts = [post for post in posts if post.id != id]
        self._save_data(posts)

    def get_by_id(self, id:int)->Optional[Post]:
        posts = self.get_all()
        for post in posts:
            if post.id == id:
                return post
        return None

    def get_all(self)->List[Post]:
        if os.stat(self.json_file).st_size == 0:
            return []
        with open(self.json_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            posts_data = data.get("posts", [])
            posts = [Post.from_dict(post_data) for post_data in posts_data]
            return posts
        
    def _save_data(self, posts: List[Post]):
        self.data["posts"] = [post.to_dict() for post in posts]  


class CommentJSONRepository(abstract_repository):
    def __init__(self, data, file):
        self.data = data
        self.dict_data = []
        self.json_file = file
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, comment: Comment):
        if len(self.get_all()) > 0:
            comments = self.get_all()
            comments.append(comment)
            self.dict_data = comments
            self.counter += 1
        else:
            self.dict_data.append(comment)
            comments = self.dict_data
            self.counter += 1
        self._save_data(comments)
        
    def delete_by_id(self, id: int):
        comments = self.get_all()
        comments = [comment for comment in comments if comment.id != id]
        self._save_data(comments)

    def get_by_id(self, id:int)->Optional[Comment]:
        comments = self.get_all()
        for comment in comments:
            if comment.id == id:
                return comment
        return None

    def get_all(self)->List[Comment]:
        if os.stat(self.json_file).st_size == 0:
            return []
        with open(self.json_file, "r", encoding='utf-8') as file:
            data = json.load(file)
            comments_data = data.get("comments", [])
            comments = [Comment.from_dict(comment_data) for comment_data in comments_data]
            return comments
        
    def _save_data(self, comments: List[Comment]):
        self.data["comments"] = [comment.to_dict() for comment in comments]   


#XML
class CategoryXMLRepository(abstract_repository):
    def __init__(self, tree):
        self.root = tree.getroot()
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, category: Category):
        categories_node = self.root.find('./categories')
        categories_node.append(category.to_xml())
        self.counter += 1
        
    def delete_by_id(self, id: int):
        xpath_expr = f".//category[@category_id='{id}']"
        categories_node = self.root.findall(xpath_expr)
        if categories_node is not None:
            for category_node in categories_node:
                self.root.remove(category_node)
                self.tree.write(self.xml_file)

    def get_by_id(self, id:int)->Optional[Category]:
        xpath_expr = f"./categories/category[@category_id='{id}']"
        category_node = self.root.find(xpath_expr)
        if category_node is None:
            return None
        return self._node_to_category(category_node)

    def get_all(self)->List[Category]:
        categories = []
        for category_node in self.root.findall('./categories/category'):
            categories.append(self._node_to_category(category_node))
        return categories

    def _node_to_category(self, category_node:ET.Element)->Category:
        category_id = int(category_node.get('category_id'))
        category_name = category_node.find('name').text
        category = Category(category_name)
        category.id = category_id
        return category
        

class IngridientXMLRepository(abstract_repository):
    def __init__(self, tree):
        self.root = tree.getroot()
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, ingredient: Ingridient):
        ingridients_node = self.root.find('./ingridients')
        ingridients_node.append(ingredient.to_xml())
        self.counter += 1
        
    def delete_by_id(self, id: int):
        xpath_expr = f".//ingridient[@ingridient_id='{id}']"
        ingridients_node = self.root.findall(xpath_expr)
        if ingridients_node is not None:
            for ingridient_node in ingridients_node:
                self.root.remove(ingridient_node)
                self.tree.write(self.xml_file)

    def get_by_id(self, id:int)->Optional[Ingridient]:
        xpath_expr = f"./ingridients/ingridient[@ingridient_id='{id}']"
        ingridient_node = self.root.find(xpath_expr)
        if ingridient_node is None:
            return None
        return self._node_to_ingridient(ingridient_node)

    def get_all(self)->List[Ingridient]:
        ingridients = []
        for ingridient_node in self.root.findall('./ingridients/ingridient'):
            ingridients.append(self._node_to_ingridient(ingridient_node))
        return ingridients

    def _node_to_ingridient(self, ingridient_node:ET.Element)-> Ingridient:
        ingridient_id = int(ingridient_node.get('ingridient_id'))
        ingridient_name = ingridient_node.find('name').text
        ingridient = Ingridient(ingridient_name)
        ingridient.id = ingridient_id
        return ingridient


class RecipeXMLRepository(abstract_repository):
    def __init__(self, tree, ingridient_repository: IngridientXMLRepository):
        self.root = tree.getroot()
        self.ingridient_repository = ingridient_repository
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, recipe: Recipe):
        recipe_node = self.root.find('./recipes')
        recipe_node.append(recipe.to_xml())
        self.counter += 1
        
    def delete_by_id(self, id: int):
        xpath_expr = f".//recipe[@recipe_id='{id}']"
        recipes_node = self.root.findall(xpath_expr)
        if recipes_node is not None:
            for recipe_node in recipes_node:
                self.root.remove(recipe_node)
                self.tree.write(self.xml_file)

    def get_by_id(self, id:int)->Optional[Recipe]:
        xpath_expr = f"./categories/category[@recipe_id='{id}']"
        recipe_node = self.root.find(xpath_expr)
        if recipe_node is None:
            return None
        return self._node_to_recipe(recipe_node)

    def get_all(self)->List[Recipe]:
        recipes = []
        for recipe_node in self.root.findall('./recipes/recipe'):
            recipes.append(self._node_to_recipe(recipe_node))
        return recipes

    def _node_to_recipe(self, recipe_node:ET.Element)->Recipe:
        recipe_id = int(recipe_node.get('recipe_id'))
        recipe_name = recipe_node.find('name').text
        recipe_number_of_serving = int(recipe_node.find('numbers_of_servings').text)
        recipe_cooking_of_time = int(recipe_node.find('cooking_time').text)
        recipe_description = recipe_node.find('description').text
        ingridients_nodes = recipe_node.findall("ingridients/ingridient")
        ingridients = [self.ingridient_repository.get_by_id(int(ingridients_node.get('id')) for ingridients_node in ingridients_nodes)]
        recipe = Recipe(recipe_name, recipe_number_of_serving, recipe_cooking_of_time, recipe_description)
        recipe.id = recipe_id
        recipe.ingridients = ingridients
        return recipe


class PostXMLRepository(abstract_repository):
    def __init__(self, tree, recipe_repository:RecipeXMLRepository, category_repository: CategoryXMLRepository):
        self.root = tree.getroot()
        self.recipe_repository = recipe_repository
        self.category_repository = category_repository
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, post: Post):
        posts_node = self.root.find('./posts')
        posts_node.append(post.to_xml())
        self.counter += 1
        
    def delete_by_id(self, id: int):
        xpath_expr = f".//post[@post_id='{id}']"
        posts_node = self.root.findall(xpath_expr)
        if posts_node is not None:
            for post_node in posts_node:
                self.root.remove(post_node)
                self.tree.write(self.xml_file)

    def get_by_id(self, id:int)->Optional[Post]:
        xpath_expr = f"./posts/post[@post_id='{id}']"
        post_node = self.root.find(xpath_expr)
        if post_node is None:
            return None
        return self._node_to_post(post_node)

    def get_all(self)->List[Post]:
        posts = []
        for post_node in self.root.findall('./posts/post'):
            posts.append(self._node_to_post(post_node))
        return posts

    def _node_to_post(self, post_node:ET.Element)->Post:
        post_id = int(post_node.get('post_id'))
        post_name = post_node.find('name').text
        post_author = post_node.find('author').text
        post_description = post_node.find('description').text
        post_recipe = self.recipe_repository.get_by_id(int(post_node.find('recipe').text))
        post_category = self.category_repository.get_by_id(int(post_node.find('category').text))
        post = Post(post_name, post_author, post_description, post_category)
        post.recipe = post_recipe
        return post


class CommentXMLRepository(abstract_repository):
    def __init__(self, tree, post_repository: PostXMLRepository):
        self.root = tree.getroot()
        self.post_repository = post_repository
        if len(self.get_all()) > 0:
            self.counter = len(self.get_all()) + 1
        else:
            self.counter = 1

    def add(self, comment: Comment):
        comment_node = self.root.find('./comments')
        comment_node.append(comment.to_xml())
        self.counter += 1
        
    def delete_by_id(self, id: int):
        xpath_expr = f".//comment[@comment_id='{id}']"
        categories_node = self.root.findall(xpath_expr)
        if categories_node is not None:
            for category_node in categories_node:
                self.root.remove(category_node)
                self.tree.write(self.xml_file)

    def get_by_id(self, id:int)->Optional[Comment]:
        xpath_expr = f"./comments/comment[@comment_id='{id}']"
        comment_node = self.root.find(xpath_expr)
        if comment_node is None:
            return None
        return self._node_to_comment(comment_node)

    def get_all(self)->List[Comment]:
        comments = []
        for comment_node in self.root.findall('./comments/comment'):
            comments.append(self._node_to_comment(comment_node))
        return comments

    def _node_to_comment(self, comment_node:ET.Element)->Comment:
        comment_id = int(comment_node.get('comment_id'))
        comment_username = comment_node.find('author_username').text
        comment_message = comment_node.find('message').text
        comment_data_creating = datetime.datetime.strptime(comment_node.find('data_creating').text, "%Y-%m-%d").date()
        comment_post = self.post_repository.get_by_id(int(comment_node.find('post').text))
        comment = Comment(comment_username, comment_message, comment_data_creating, comment_post)
        comment.id = comment_id
        return comment


#SQLAlchemy
class CategoryRepository(abstract_repository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, category: Category):
        exsisting_category = self.session.query(Category).filter_by(name = category.name).first()
        if exsisting_category is None:          
            self.session.add(category)
            self.session.commit()
        
    def delete_by_id(self, id: int):
        category = self.session.query(Category).get(id)
        self.session.delete(category)
        self.session.commit()

    def update(self, new_category: Category, id: int):
        pass

    def get_by_id(self, id:int):
        return self.session.query(Category).get(id)

    def get_all(self):
        return self.session.query(Category).all()

class RecipeRepository(abstract_repository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, recipe: Recipe):            
        self.session.add(recipe)
        self.session.commit()
        
    def delete_by_id(self, id: int):
        recipe = self.session.query(Recipe).get(id)
        self.session.delete(recipe)
        self.session.commit()

    def get_by_id(self, id:int):
        return self.session.query(Recipe).get(id)

    def get_all(self):
        return self.session.query(Recipe).all()


class PostRepository(abstract_repository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, post: Post):            
        self.session.add(post)
        self.session.commit()
        
    def delete_by_id(self, id: int):
        post = self.session.query(Post).get(id)
        self.session.delete(post)
        self.session.commit()

    def get_by_id(self, id:int):
        return self.session.query(Post).get(id)

    def get_all(self):
        return self.session.query(Post).all()


class CommentRepository(abstract_repository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, comment: Comment):            
        self.session.add(comment)
        self.session.commit()
        
    def delete_by_id(self, id: int):
        comment = self.session.query(Comment).get(id)
        self.session.delete(comment)
        self.session.commit()

    def get_by_id(self, id:int):
        return self.session.query(Comment).get(id)

    def get_all(self):
        return self.session.query(Comment).all()


class IngridientRepository(abstract_repository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, ingredient: Ingridient):            
        existing_ingridient = self.session.query(Ingridient).filter_by(name = ingredient.name).first()
        if existing_ingridient is None:          
            self.session.add(ingredient)
            self.session.commit()
        
    def delete_by_id(self, id: int):
        ingridient = self.session.query(Ingridient).get(id)
        self.session.delete(ingridient)
        self.session.commit()

    def get_by_id(self, id:int):
        return self.session.query(Ingridient).get(id)

    def get_all(self):
        return self.session.query(Ingridient).all()