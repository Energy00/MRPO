from repositories import *

recipe1 = Recipe(name='Куринный суп', numbers_of_servings=7, cooking_time=1, ingridients=['Курица','Вода','Картошка','Морковка','Лук'], description='Нежный куринный бульон')
RecRep = RepiceRepository()
RecRep.add(recipe1)
category1 = Category(name='Супы')
CatRep = CategoryRepository()
CatRep.add(category1)
post1 = Post(name='Нежный куринный суп', author='Наталья', description='Что-то написано', recipe=recipe1, category=category1)
PostRep = PostRepository()
PostRep.add(post1)
PostRep.readAll()
