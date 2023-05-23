from uow import *


def create_ingridients(
    uow: AbstractUnitOfWork,
    name: str,
):
    with uow:
        ingridient = Ingridient(name)
        uow.ingridient_repository.add(ingridient)
        uow.commit()
        return ingridient.id


def create_category(uow: AbstractUnitOfWork, name: str):
    with uow:
        category = Category(name)
        uow.category_repository.add(category)
        uow.commit()
        return category.id

def create_recipe(
    uow: AbstractUnitOfWork,
    name: str,
    numbers_of_servings:int, 
    cooking_time:int, 
    description:str,
    ingridients: List[Ingridient]
):
    with uow:
        recipe = Recipe(name, numbers_of_servings, cooking_time, description)
        recipe.ingridients = ingridients
        uow.recipe_repository.add(recipe)
        uow.commit()
        return recipe.id

def create_post(
    uow: AbstractUnitOfWork,
    name:str, 
    author:str, 
    description:str, 
    category: Category,
    recipe: Recipe
):
    with uow:
        post = Post(name, author, description, category)
        post.recipe = recipe
        uow.post_repository.add(post)
        uow.commit()
        return post.id

def create_comment(
    uow: AbstractUnitOfWork,
    username:str, 
    message:str, 
    data_creating: datetime.date, 
    post: Post
):
    with uow:
        comment = Comment(username, message, data_creating, post)
        uow.comment_repository.add(comment)
        uow.commit()
        return comment.id