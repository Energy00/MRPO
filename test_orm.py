import sqlalchemy as sa
from engine import *
import datetime
from repositories import *


session = mapping()
category_repository = CategoryRepository(session)
ingridient_repository = IngridientRepository(session)
recipe_repository = RecipeRepository(session)
post_repository = PostRepository(session)
comment_repository = CommentRepository(session)

ingridient1 = Ingridient(name='Курица')
ingridient3 = Ingridient(name='Перец')
ingridient4 = Ingridient(name='Соль')
ingridient5 = Ingridient(name='Базилик')

ingridient_repository.add(ingridient1)
ingridient_repository.add(ingridient2)
ingridient_repository.add(ingridient3)
ingridient_repository.add(ingridient4)
ingridient_repository.add(ingridient5)

recipe = Recipe(name='Курица гриль',numbers_of_servings=6,cooking_time=140,description='Мы поделимся простым рецептом блюда, которое готовится без особых усилий в домашних условиях.')
needed_ingredients = session.query(Ingridient).filter(Ingridient.name.in_([ingridient1.name, ingridient2.name, ingridient3.name, ingridient4.name, ingridient5.name])).all()
recipe.ingridients = needed_ingredients
recipe_repository.add(recipe)

category = Category(name='Мясо')
category_repository.add(category)

needed_category = session.query(Category).filter_by(name = category.name).first()
post = Post(name='Сочная курочка гриль или как все сжечь', author='Павел', description='Какая-та история', category=needed_category)
post.recipe = recipe

comment1 = Comment(username='Даша', message='Весело, но лучше такого не повторять', data_creating=datetime.date(2023,5,16),post=post)
comment2 = Comment(username='Илья', message='Прикольно вышло, надо попробовать', data_creating=datetime.date(2023,5,15), post=post)

post.comments = [comment1, comment2]
post_repository.add(post)

comment_repository.add(comment1)
comment_repository.add(comment2)
