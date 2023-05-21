from abc import ABC, abstractmethod
from models import *
from sqlalchemy.orm import Session


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
