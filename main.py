from repositories import *
import datetime

# recipe1 = Recipe(name='Куринный суп', numbers_of_servings=7, cooking_time=1, ingridients=['Курица','Вода','Картошка','Морковка','Лук'], description='Нежный куринный бульон')
# RecRep = RepiceRepository()
# RecRep.add(recipe1)
# category1 = Category(name='Супы')
# CatRep = CategoryRepository()
# # CatRep.add(category1)
# post1 = Post(name='Нежный куринный суп', author='Наталья', description='Что-то написано', recipe=recipe1, category=category1)
# PostRep = PostRepository()
# PostRep.add(post1)
# PostRep.readAll()

recipe1 = Recipe(name='Куринный суп', numbers_of_servings=7, cooking_time=1, ingridients=['Курица','Вода','Картошка','Морковка','Лук'], description='Нежный куринный бульон')
recipe2 = Recipe(name='Куринный суп', numbers_of_servings=7, cooking_time=1, ingridients=['Курица','Вода','Картошка','Морковка','Лук'], description='Нежный куринный бульон')
category1 = Category(name='Супы')
post1 = Post(name='Нежный куринный суп', author='Наталья', description='Что-то написано', recipe=recipe1, category=category1)
post2 = Post(name='Нежный куринный суп', author='Наталья', description='Что-то написано', recipe=recipe2, category=category1)
comment1 = Comment('Natasha', 'Какой-то комментарий', datetime.date(2022, 11, 4), post1)
comment2 = Comment('Pavel', 'Какой-то комментарий', datetime.date(2020, 3, 1), post1)
comment3 = Comment('Dima', 'Какой-то комментарий', datetime.date(2021, 9, 26), post1)
comment4 = Comment('Misha', 'Какой-то комментарий', datetime.date(1943, 8, 1), post1)
comment5 = Comment('Miroslav', 'Какой-то комментарий', datetime.date(2023, 4, 25), post1)
sort_post1_comment = sort_comment_on_date(post1, datetime.date(2022, 3, 29), '>')
for c in sort_post1_comment:
    print(c.user_name, c.message, c.data_creating)
# for c in post1.comments:
#     print(c.user_name, c.message, c.data_creating)