import sqlalchemy as sa
from engine import *
import datetime
from repositories import *
from uow import *
import view

uow = JSONUnitOfWork()

with uow:
    category = Category(name='Мясо')
    category.id = uow.category_repository.counter
    uow.category_repository.add(category)

    ingridient1 = Ingridient(name='Курица')
    ingridient1.id = uow.ingridient_repository.counter
    uow.ingridient_repository.add(ingridient1)

    ingridient2 = Ingridient(name='Приправа для курицы')
    ingridient2.id = uow.ingridient_repository.counter
    uow.ingridient_repository.add(ingridient2)

    ingridient3 = Ingridient(name='Перец')
    ingridient3.id = uow.ingridient_repository.counter
    uow.ingridient_repository.add(ingridient3)

    ingridient4 = Ingridient(name='Соль')
    ingridient4.id = uow.ingridient_repository.counter
    uow.ingridient_repository.add(ingridient4)

    ingridient5 = Ingridient(name='Базилик')
    ingridient5.id = uow.ingridient_repository.counter
    uow.ingridient_repository.add(ingridient5)


    recipe = Recipe(name='Курица гриль',numbers_of_servings=6,cooking_time=140,description='Мы поделимся простым рецептом блюда, которое готовится без особых усилий в домашних условиях.')
    recipe.id = uow.recipe_repository.counter
    recipe.ingridients = [ingridient1, ingridient2, ingridient3, ingridient4, ingridient5]
    uow.recipe_repository.add(recipe)

    post = Post(name='Сочная курочка гриль или как все сжечь', author='Павел', description='Какая-та история', category=category)
    post.id = uow.post_repository.counter
    post.recipe = recipe
    uow.post_repository.add(post)

    comment1 = Comment(username='Даша', message='Весело, но лучше такого не повторять', data_creating=datetime.date(2023,5,16),post=post)
    comment1.id = uow.comment_repository.counter
    uow.comment_repository.add(comment1)

    comment2 = Comment(username='Илья', message='Прикольно вышло, надо попробовать', data_creating=datetime.date(2023,5,15), post=post)
    comment2.id = uow.comment_repository.counter
    uow.comment_repository.add(comment2)
    uow.commit()

with uow:
    post = view.get_post_by_id(1, uow)
    print(post)

# xml_file = 'mrpo.xml'
# tree = ET.parse(xml_file, ET.XMLParser(encoding='UTF-8'))

# category_repository = CategoryXMLRepository(tree)
# ingridient_repository = IngridientXMLRepository(tree)
# recipe_repository = RecipeXMLRepository(tree, ingridient_repository)
# post_repository = PostXMLRepository(tree, recipe_repository, category_repository)
# comment_repository = CommentXMLRepository(tree, post_repository)

# category = Category(name='Выпечка')
# category.id = category_repository.counter
# category_repository.add(category)

# ingridient1 = Ingridient(name='Мука')
# ingridient1.id = ingridient_repository.counter
# ingridient_repository.add(ingridient1)

# ingridient2 = Ingridient(name='Тесто')
# ingridient2.id = ingridient_repository.counter
# ingridient_repository.add(ingridient2)

# ingridient3 = Ingridient(name='Вишня')
# ingridient3.id = ingridient_repository.counter
# ingridient_repository.add(ingridient3)


# recipe = Recipe(name='Пирожок с вишней',numbers_of_servings=6,cooking_time=140,description='Мы поделимся простым рецептом блюда, которое готовится без особых усилий в домашних условиях.')
# recipe.id = recipe_repository.counter
# recipe.ingridients = [ingridient1, ingridient2, ingridient3]
# recipe_repository.add(recipe)

# post = Post(name='Вкуснейший пирожок', author='Павел', description='Какая-та история', category=category)
# post.id = post_repository.counter
# post.recipe = recipe
# post_repository.add(post)

# comment1 = Comment(username='Даша', message='Весело, но лучше такого не повторять', data_creating=datetime.date(2023,5,16),post=post)
# comment1.id = comment_repository.counter
# comment_repository.add(comment1)

# comment2 = Comment(username='Илья', message='Прикольно вышло, надо попробовать', data_creating=datetime.date(2023,5,15), post=post)
# comment2.id = comment_repository.counter
# comment_repository.add(comment2)

# tree.write(xml_file, encoding='UTF-8')