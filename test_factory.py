from models import *
from serializer import ObjectSerializer

serializer = ObjectSerializer()
category = Category('Pizza')
category.id = 10
recipe = Recipe(name='Cheese Pizza',numbers_of_servings=8,cooking_time=120,description='We want to share with you')
recipe.id = 5
post = Post(name='BEST PIZZA', author='Kirill', description='Interesting description', category=category)
post.id = 4
post.recipe = recipe

format = 'JSON'
output = serializer.serialize(post, format)
print(output)
# for i in post.status('Delete Post'):
#     print(i)
print(next(post.status('Delete Post')))
